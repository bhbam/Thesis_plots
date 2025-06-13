import os
from PIL import Image

# Disable PIL safety check for large images
Image.MAX_IMAGE_PIXELS = None

# Directories
input_dir = 'fig_econ'
output_dir = 'fig_econ_pdf'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all PNG files in input_dir
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.png'):
        try:
            # Load image
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path).convert('RGB')

            # Define output PDF path
            pdf_filename = os.path.splitext(filename)[0] + '.pdf'
            pdf_path = os.path.join(output_dir, pdf_filename)

            # Save as PDF
            img.save(pdf_path, 'PDF')
            print(f"Converted {filename} -> {pdf_filename}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
