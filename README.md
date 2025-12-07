# Pixelate: GPU-Powered Image Processor 

## Overview

**Pixelate** is a lightweight, GPU-accelerated image processing pipeline designed to run efficiently in **Google Colab** or on local CUDA-enabled systems. It automatically downloads sample images, applies grayscale filtering, resizes them using GPU acceleration, and saves the processed outputs. The goal is to demonstrate how **GPU computing** can significantly speed up batch image transformations.

---

## Features

* **CUDA Acceleration:** Uses **CuPy** to perform image operations directly on the GPU.
* **Automated Image Generation:** Fetches random sample images from the internet.
* **Batch Processing:** Handles all images in the `input/` directory automatically.
* **Image Processing Steps:**

  1. **Grayscale Conversion** – Converts RGB images to grayscale for simplicity.
  2. **GPU Resizing** – Scales image dimensions based on a user-defined percentage.
* **Colab + Drive Integration:** Fully compatible with Google Colab and Google Drive for cloud execution.

---

## Tech Stack

* **Language:** Python 3
* **Core Libraries:**

  * `CuPy` – GPU-accelerated NumPy computations
  * `OpenCV` – Image reading, writing, and resizing
  * `NumPy` – Numerical operations
  * `Pillow` – Image file handling
* **Environment:** Google Colab (GPU runtime) or local CUDA setup

---

## Project Structure

| File                 | Description                                                                     |
| -------------------- | ------------------------------------------------------------------------------- |
| `main.py`            | Main processing pipeline that reads, filters, and resizes images using the GPU. |
| `utils.py`           | Utility functions for grayscale conversion and GPU-based resizing.              |
| `generate_images.py` | Script that downloads sample images into the `input/` directory.                |
| `requirements.txt`   | Contains required Python dependencies.                                          |
| `MAKEFILE`           | Provides simple automation commands for setup and cleanup.                      |
| `README.md`          | Documentation file explaining setup and usage.                                  |

---

## Installation & Setup

### Option 1 — Run in Google Colab (Recommended)

#### Step 1: Upload to Google Drive

Upload the full `Pixelate` folder into your **My Drive** directory.

#### Step 2: Open Google Colab

1. Open a new notebook on [Google Colab](https://colab.research.google.com/).
2. Go to **Runtime → Change runtime type → GPU (T4)**.
3. Mount your Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

#### Step 3: Run the Script

Copy this entire block into a Colab cell and execute it:

```python
import os

# Set up project path
project_folder = "Pixelate"
project_path = os.path.join("/content/drive/MyDrive", project_folder)
os.chdir(project_path)
print(f"Working directory set to: {os.getcwd()}")

# Step 1: Install dependencies
print("\nInstalling requirements...")
!pip install -r requirements.txt -q

# Step 2: Generate input images
print("\nGenerating random input images...")
!python3 generate_images.py

# Step 3: Run the GPU image processor
print("\nRunning GPU-accelerated image processing...")
!python3 main.py --percent 0.1

print("\n All images processed successfully!")
```

---

### Option 2 — Run Locally (With CUDA)

```bash
# Clone repository
git 
cd Pixelate

# Install dependencies
pip install -r requirements.txt

# Generate input images
python generate_images.py

# Process images (default: resize to 10%)
python main.py --percent 0.1
```

---

##  Output

After execution, all processed images (grayscale + resized) will be saved in the `/output` folder.
Example transformation:

```
Original: 512x512 → Processed: 160x160 (approx)
```

---

##  Notes

* The percentage value passed via `--percent` defines the target file size ratio.
  Example: `--percent 0.1` = reduce image dimensions to ~10% of their original pixel area.
* Ensure GPU runtime is active in Colab; otherwise, the process will fall back to CPU.

---

## Example Use Cases

* Dataset preprocessing for ML models
* GPU acceleration tutorials
* Image compression research
* Demonstrating CUDA-powered Python workflows

---

## License

This project is open-source and available under the **MIT License**.
Feel free to use, modify, and share.

---

## Author

**Vansh Goyal**
IIIT Delhi 
Contact: vansh23577@iiitd.ac.in

=======
# Pixelate
**Pixelate** is a lightweight, GPU-accelerated image processing pipeline designed to run efficiently in **Google Colab** or on local CUDA-enabled systems. It automatically downloads sample images, applies grayscale filtering, resizes them using GPU acceleration, and saves the processed outputs.

