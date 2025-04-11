# Image Cropper for Letter Scans

This script is designed to crop scanned letter images into two parts:
1. The **header** section containing the name, address, and date.
2. The **body** section containing the handwritten message.

## 🧾 How It Works

The script uses Python's `PIL` library to:
- Load the original image.
- Define and extract two regions:
  - The header (top portion).
  - The body (rest of the letter).
- Save both parts as separate image files.

## 📁 Files

- `image.png`: The input image to be processed.
- `image_header.png`: The cropped header section.
- `image_body.png`: The cropped body section.

## ▶️ Usage

1. Make sure you have Python installed.
2. Install the required package:
   ```bash
   pip install Pillow


Place image.png in the same folder as the script.

Run the script:

bash
Copiar
Editar
python crop_letter.py
Two new image files will be created:

image_header.png

image_body.png

✏️ Customize
If your images have a different layout, you can adjust the cropping coordinates in the script:

python
Copiar
Editar
header_box = (0, int(height * 0.12), width, int(height * 0.30))
body_box = (0, int(height * 0.31), width, height)
These values represent percentages of the image height and can be fine-tuned to match your needs.