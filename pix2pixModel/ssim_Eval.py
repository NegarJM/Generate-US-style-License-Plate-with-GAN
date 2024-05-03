# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:22:43 2024

@author: pmeshkiz
"""

import os
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.io import imread


# Set Data Directory

Dd = r'.\results\LP_pix2pix\test_latest\images'

# Dictionary to hold pairs of images
targets = []

# Scan directory and group image pairs
for filename in os.listdir(Dd):
    if filename.endswith(".png"):
        parts = filename.split('_')
        if len(parts) == 3:  # Make sure filename splits into exactly three parts
            base_name = parts[0]
            suffix = parts[2]
            if suffix == 'B.png' and base_name not in targets :
                targets.append(base_name)
                

# List to store SSIM values
ssim_values = []

# Calculate SSIM for each pair
for base_name in targets:
    image_path_fake = os.path.join(Dd, base_name + "_fake_B.png")
    img_fake_B = imread(image_path_fake)
    image_path_real = os.path.join(Dd, base_name + "_real_B.png")
    img_real_B = imread(image_path_real)
    ssim_value = ssim(img_fake_B, img_real_B, channel_axis=-1, win_size=127, data_range=img_real_B.max() - img_real_B.min())
    ssim_values.append(ssim_value)

# Calculate the average SSIM
average_ssim = np.mean(ssim_values) if ssim_values else 0

print("Average SSIM:", average_ssim)