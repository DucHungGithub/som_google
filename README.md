# SoM: Set-of-Mark Prompting for Visual Grounding

This repository presents an implementation of **Set-of-Mark (SoM) Prompting**, a novel approach to enhance visual grounding in the strongest large multimodal model (LMM) — GPT-4V. By overlaying spatial and speakable marks on images, SoM unleashes the visual grounding capabilities of GPT-4V through visual prompting. 

## 🚀 Key Idea
**Visual Prompting for Vision**: SoM enhances GPT-4V’s ability to ground text in images by:
- Using a **set of masks** on images to focus the model's attention.
- Combining **images and text** in a prompt to achieve superior understanding and reasoning.

### Original Method
In the original paper ([SoM: Set-of-Mark Prompting](https://arxiv.org/pdf/2310.11441.pdf)), multiple large models were employed to generate precise masks for images.

### Simplified Approach in This Repository
This implementation simplifies the process by:
- Utilizing **Google OCR** to generate image masks.
- Enabling easy setup and application of SoM prompting.

## 📄 Reference
- **Paper**: [SoM: Set-of-Mark Prompting](https://arxiv.org/pdf/2310.11441.pdf)
- **Code**: [Official SoM GitHub](https://github.com/microsoft/SoM)

## 💡 Applications
- **Visual Question Answering (VQA)**
- **Image Captioning**
- **Interactive Image Analysis**
- **AI-Assisted Design**

## 🛠️ Customization
You can replace Google OCR with other OCR tools or modify the masking logic to fit your specific use case.

## 🎯 Future Work
- Explore more efficient OCR techniques.
- Integrate additional pre-trained models for mask generation.
- Optimize performance for real-time applications.

## 🙌 Acknowledgments
This project builds on the groundbreaking work presented in the SoM paper and leverages GPT-4V's exceptional multimodal capabilities. Special thanks to the original authors and contributors.

---

Start using **SoM Prompting** today and unlock the full potential of GPT-4V for visual understanding! 🚀
