import base64
import json
import os
from io import BytesIO

from PIL import ImageDraw, ImageFont
from PIL import Image as PImage

from google.cloud import vision
from google.cloud.vision_v1.types.image_annotator import Image as GImage

from src.schemas.feature_type import FeatureType




class GoogleVision:
    def __init__(self):
        
        credentials = base64.b64decode(
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        ).decode("utf-8")
        json_content = json.loads(credentials)

        self.google_client = vision.ImageAnnotatorClient.from_service_account_info(
            json_content
        )

        
    def extract_logo(self, image: GImage):
        response = self.google_client.logo_detection(image=image)
        logos = response.logo_annotations
        return logos
    
    def render_doc_text(self, image: PImage) -> PImage:
        t_image = image.copy()
        
        g_image = self.convert_PI2GI(image)
        
        bounds = self._get_document_bounds(g_image, FeatureType.BLOCK)
        self._draw_boxes(t_image, bounds, "blue")
        
        bounds = self._get_document_bounds(g_image, FeatureType.PARA)
        self._draw_boxes(t_image, bounds, "red", True)
        
        return t_image
    
    def get_note_annotation(self, image: GImage) -> str:
        response = self.google_client.text_detection(image=image)
        para_list = response.text_annotations[0].description.split('\n')
        
        result = []
        for i, p in enumerate(para_list):
            result.append(f"{str(i)}: {p}")
            
        return "\n".join(result)
    
    def convert_PI2GI(self, image: PImage) -> GImage:
        buffer = BytesIO()
        image.save(buffer, format="PNG")

        byte_array = buffer.getvalue()
        encoded_image = base64.b64encode(byte_array).decode('utf-8')
        image = vision.Image(content=encoded_image)
        
        return image
    
    def _draw_boxes(self, image: PImage, bounds, color, draw_index = False):
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("fonts/arial.ttf", 20)
        
        for i, bound in enumerate(bounds):
            draw.polygon(
                [
                    bound.vertices[0].x,
                    bound.vertices[0].y,
                    bound.vertices[1].x,
                    bound.vertices[1].y,
                    bound.vertices[2].x,
                    bound.vertices[2].y,
                    bound.vertices[3].x,
                    bound.vertices[3].y,
                ],
                None,
                color,
                4
            )
            
            if draw_index:
                bot_right = (bound.vertices[2].x + 2, bound.vertices[2].y-2)
                draw.text(bot_right, str(i), fill="yellow", font=font)
                
        return image
    
    def _get_document_bounds(self, image: GImage, feature: FeatureType):
        bounds = []
        
        response = self.google_client.document_text_detection(image=image)
        document = response.full_text_annotation
        
        for page in document.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            if feature == FeatureType.SYMBOL:
                                bounds.append(symbol.bounding_box)

                        if feature == FeatureType.WORD:
                            bounds.append(word.bounding_box)
                            

                    if feature == FeatureType.PARA:
                        bounds.append(paragraph.bounding_box)

                        

                if feature == FeatureType.BLOCK:
                    bounds.append(block.bounding_box)

        return bounds
    
    
        
        
    
    

        
        
        
        
        
        
        
        
        