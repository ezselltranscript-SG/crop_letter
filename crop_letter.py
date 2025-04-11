from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from PIL import Image
import os
import zipfile
import io

app = FastAPI()

# Enable CORS
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

    # Create a ZIP in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        zip_file.write(header_path, arcname="image_header.png")
        zip_file.write(body_path, arcname="image_body.png")
    zip_buffer.seek(0)

    return StreamingResponse(zip_buffer, media_type="application/zip", headers={
        "Content-Disposition": "attachment; filename=cropped_images.zip"
    })
