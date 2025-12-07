#!/bin/bash

# Navigate to the Pixelate project folder
cd Pixelate/ || { echo "Pixelate folder not found"; exit 1; }

# Step 1: Install dependencies
echo -e "\nInstalling requirements..."
pip install -r requirements.txt

# Step 2: Generate input images
echo -e "\nGenerating random input images..."
python3 generate_images.py

# Step 3: Run the GPU image processor
echo -e "\nRunning GPU-accelerated image processing..."
python3 main.py --percent 0.1

echo -e "\nAll images processed successfully!"
