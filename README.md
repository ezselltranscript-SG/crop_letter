# 🖼️ FastAPI Image Cropper

This FastAPI application allows you to upload an image (e.g., a handwritten letter), automatically crops it into two sections (header and body), and provides download links for the resulting PNG images.

---

## 🚀 Features

- Upload an image via a POST request.
- Automatically crops:
  - The **header** (top portion).
  - The **body** (main content).
- Returns direct download links for both cropped images.

---

## 📦 Requirements

Install all dependencies with:

```bash
pip install fastapi uvicorn pillow python-multipart


project/
│
├── main.py             # FastAPI application
├── image.png           # (Uploaded input image - optional)
├── image_header.png    # (Cropped header - auto-generated)
├── image_body.png      # (Cropped body - auto-generated)
└── README.md

Activate your virtual environment (optional but recommended):
.\venv\Scripts\activate

Run the FastAPI app using Uvicorn:
uvicorn main:app --reload

🔄 API Endpoints
POST /crop-image/
Upload a PNG image and receive links to download the cropped sections.

Form field:
file: The image file (PNG recommended)

Response:
{
  "header_download_url": "/download/header",
  "body_download_url": "/download/body"
}
GET /download/header
Downloads the cropped header section as image_header.png.

GET /download/body
Downloads the cropped body section as image_body.png.

📌 Notes
Cropping is based on fixed relative height percentages:

Header: 12% to 30%

Body: 31% to bottom

These values can be customized in the main.py file.

🧰 Dependencies Used
FastAPI

Uvicorn

Pillow (PIL)

python-multipart

