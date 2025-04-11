from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import os

app = FastAPI()

# Enable CORS (optional for testing in browser)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/crop-image/")
async def crop_image(file: UploadFile = File(...)):
    input_path = "image.png"
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Load the image
    img = Image.open(input_path)
    width, height = img.size

    # Crop coordinates
    header_box = (0, int(height * 0.12), width, int(height * 0.30))
    body_box = (0, int(height * 0.31), width, height)

    # Crop and save
    header_path = "image_header.png"
    body_path = "image_body.png"
    img.crop(header_box).save(header_path)
    img.crop(body_box).save(body_path)

    # You can return one or both images here — let's return the body for now
    return {
        "header_download_url": "/download/header",
        "body_download_url": "/download/body"
    }

@app.get("/download/header", response_class=FileResponse)
def download_header():
    return FileResponse("image_header.png", media_type="image/png", filename="image_header.png")

@app.get("/download/body", response_class=FileResponse)
def download_body():
    return FileResponse("image_body.png", media_type="image/png", filename="image_body.png")
