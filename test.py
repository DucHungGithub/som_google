from src.google_vision_extract.google_vision import GoogleVision
from PIL import Image

pimage = Image.open("images/before.jpg")

google_vision = GoogleVision()

gimage = google_vision.convert_PI2GI(pimage)

# logos = google_vision.extract_logo(gimage)

# for logo in logos:
#     print(logo.description)
    
    
# print(google_vision.get_note_annotation(gimage))

t_image = google_vision.render_doc_text(pimage)

t_image.save("image.png", "PNG")
    

