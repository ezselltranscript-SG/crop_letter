from PIL import Image

# Load the original image
input_path = "image.png"
img = Image.open(input_path)
width, height = img.size

# Define crop coordinates for the top (header) and bottom (body) sections
header_box = (0, int(height * 0.12), width, int(height * 0.30))  # adjusted to skip the title

# Bottom part: the handwritten letter
body_box = (0, int(height * 0.31), width, height)

# Crop and save
header = img.crop(header_box)
body = img.crop(body_box)

header.save("image_header.png")
body.save("image_body.png")

print("✅ Cropped images saved as image_header.png and image_body.png")
