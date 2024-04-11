import os
import numpy as np
import cv2

# Define your arguments
fold_A = "./LicensePlateDatasetOutlines/"
fold_B = "./LicensePlateDataset/"
fold_AB = "./Combined/"
num_imgs = 1000000
use_AB = False  # Set this to True if you want to use '_A' images

# List the splits in the input directory
splits = os.listdir(fold_A)

print(splits[:10])
print(fold_A)

for sp in splits:
    img_fold_A = os.path.join(fold_A, sp)
    img_fold_B = os.path.join(fold_B, sp)

    # # Check if img_fold_A is a file or a directory
    # if os.path.isfile(img_fold_A):
    #     print(f"Skipping {img_fold_A} - it's a file, not a directory")
    #     continue  # Skip if it's a file

    img_list = os.listdir(img_fold_A)

    if use_AB:
        img_list = [img_path for img_path in img_list if "_A." in img_path]

    num_imgs = min(num_imgs, len(img_list))
    print("split = %s, use %d/%d images" % (sp, num_imgs, len(img_list)))
    img_fold_AB = os.path.join(fold_AB, sp)

    if not os.path.isdir(img_fold_AB):
        os.makedirs(img_fold_AB)
    print("split = %s, number of images = %d" % (sp, num_imgs))

    for n in range(num_imgs):
        name_A = img_list[n]
        path_A = os.path.join(img_fold_A, name_A)

        if use_AB:
            name_B = name_A.replace("_A.", "_B.")
        else:
            name_B = name_A
        path_B = os.path.join(img_fold_B, name_B)

        if os.path.isfile(path_A) and os.path.isfile(path_B):
            name_AB = name_A
            if use_AB:
                name_AB = name_AB.replace("_A.", ".")  # remove _A
            path_AB = os.path.join(img_fold_AB, name_AB)
            im_A = cv2.imread(
                path_A, 1
            )  # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_B = cv2.imread(
                path_B, 1
            )  # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_AB = np.concatenate([im_A, im_B], 1)
            cv2.imwrite(path_AB, im_AB)
