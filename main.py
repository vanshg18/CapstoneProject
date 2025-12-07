import os
import cv2
import cupy as cp
import numpy as np
import argparse
from utils import resize_image_gpu, apply_grayscale

SRC_DIR = 'input'
DEST_DIR = 'output'

def setup_output_directory():
    """Create or clear the output folder."""
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
        print(f"Output directory created: {DEST_DIR}")
    else:
        for item in os.listdir(DEST_DIR):
            os.remove(os.path.join(DEST_DIR, item))
        print(f"Cleaned old images from {DEST_DIR}")

def get_file_bytes(filepath):
    """Return the file size in bytes."""
    return os.path.getsize(filepath)

def handle_images(scale_ratio):
    """Process each image: grayscale + GPU resize."""
    setup_output_directory()

    for filename in os.listdir(SRC_DIR):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        source_path = os.path.join(SRC_DIR, filename)
        target_path = os.path.join(DEST_DIR, filename)

        print(f"Working on {filename}...")

        initial_size = get_file_bytes(source_path)
        image = cv2.imread(source_path)

        if image is None:
            print(f"Skipping {filename}: Unable to load the image.\n")
            continue

        # Step 1: convert to grayscale
        grayscale_img = apply_grayscale(image)

        # Step 2: compute new dimensions based on percentage
        height, width = grayscale_img.shape[:2]
        resize_factor = (scale_ratio) ** 0.5
        target_w = max(int(width * resize_factor), 64)
        target_h = max(int(height * resize_factor), 64)

        # Step 3: resize using GPU acceleration
        resized_img = resize_image_gpu(grayscale_img, (target_w, target_h))

        # Step 4: save result
        cv2.imwrite(target_path, resized_img, [cv2.IMWRITE_JPEG_QUALITY, 80])

        final_size = get_file_bytes(target_path)
        print(f"Size reduced: {initial_size // 1024} KB → {final_size // 1024} KB\n")

    print(f"Processing completed with {int(scale_ratio * 100)}% scaling factor.\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="GPU-accelerated image resizer with grayscale preprocessing.")
    parser.add_argument("--percent", type=float, default=0.1,
                        help="Scaling target as a fraction of original file size (e.g., 0.1 = 10%)")
    opts = parser.parse_args()
    handle_images(opts.percent)
