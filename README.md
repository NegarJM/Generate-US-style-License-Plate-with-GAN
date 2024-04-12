![Test_fig](https://github.com/NegarJM/Generate-US-style-License-Plate-with-GAN/assets/97193844/77074108-072b-41a8-997a-f4a043c66c7d)# Generate-US-style-License-Plate-with-GAN

## Abstract

Training efficient license plate detection models, applicable in different machine vision fields such as autonomous driving, requires inputting many actual license plate images, which demands significant resources and raises privacy issues. This project aims to create synthetic license plates to tackle the cost of providing real data. However, this causes difficulty, as the quality of these synthetic plates tends to be very high, which could affect the model's performance under real-world conditions. In order to address this challenge, the project implements Generative Adversarial Networks (GANs) to generate synthetic license plates with different quality levels that closely replicate authentic plates. The objective of this methodology is to provide a practical and privacy-preserving alternative to traditional training methods. It accomplishes this by facilitating the generation of diverse and authentic synthetic datasets useful for training license plate detection models.

## License Plate Synthesis with Generative Adversarial Networks

### Data Collection and Preprocessing

To generate synthetic license plates, we adopted the approach suggested in an open-source project [1]. The methodology involves creating a dataset of hundreds of randomly generated US-style license plates. By generating hundreds of random letters and digits in the license plates' style (There are different styles over used different states of the United States), we obtained a diverse set of outlines representing the characteristic features of US license plates which can be inputted into the pix2pix model to generate our realistically fake plates.

### Pix2Pix Model

Pix2Pix, short for "Image-to-Image Translation with Conditional Adversarial Networks," is a type of generative adversarial network (GAN) designed for image translation tasks [2]. Pix2Pix is particularly effective for tasks with one-to-one mapping between input and output images.

The Pix2Pix model, like all other GAN models, consists of a generator and a discriminator. The generator employs a U-Net-like architecture, well-suited for retaining the fine details in image translations. On the other hand, the discriminator is a Convolutional Neural Network (CNN) responsible for discerning between pairs of input images—real and generated.

Training Pix2Pix necessitates a dataset containing pairs of input and target images. For instance, in the context of image colorization, the input images may be grayscale, with their corresponding targets being the same images but in color.

During training, Pix2Pix utilizes a dual-loss approach to guide the learning process effectively: 
- Adversarial Loss (GAN Loss): Encourages the generator to produce outputs that are indistinguishable from real data.
- L1 Loss: Measures the pixel-wise difference between the generated output and the ground truth. This loss helps in maintaining structural similarity between input and output.

In summary, the Pix2Pix model excels in transforming input images into desired output formats by pairing an intricate generator architecture with a discriminative network, all within the context of a carefully curated dataset and dual loss functions for compelling image translation results.

### Training Dataset Preparation

We utilized our real license plate images consisting of 500 images of license plates for training, validating, and testing our generative model. As the pix2pix model requires paired images for training, we conducted a preprocessing step. Specifically, We used an outline extractor, primarily relying on the Canny function, a built-in feature in the OpenCV library, to detect the edges in the license plate images. The Canny algorithm employs gradient operations and thresholding to identify edges, resulting in a binary image where edges appear as white lines against a black background. We integrated these outlines with the original images to create pairs that were subsequently employed in the training of our pix2pix model. This step facilitated the learning process for the generative model, allowing it to understand the relationship between the license plate image and its corresponding outline.

![Training dataset preparation block](https://github.com/NegarJM/Generate-US-style-License-Plate-with-GAN/assets/97193844/5932299d-ce4d-4af8-8c5f-257b0ed037e1)


### Testing Dataset Generation
To produce our authentic-looking counterfeit license plates, we first needed to create a dataset of outline images representing fake license plates. To accomplish this, we wrote a code that randomly generated synthetic license plates in the style and font typical of US license plates, focusing on one of the primary styles that consist of six characters (three letters and three digits). Our code generated license plates with blue backgrounds, selecting three random letters and three random digits. We then processed these plates through our outline detector to extract the outlines. Leveraging our trained pix2pix model, we used these extracted outlines from the synthetic license plates to generate new, realistically fake plates. This procedure involved testing the model by inputting the synthetic outlines, resulting in the creation of fake plates with backgrounds similar to those in the initial dataset used for model training.

![Testing dataset generation block](https://github.com/NegarJM/Generate-US-style-License-Plate-with-GAN/assets/97193844/feae7f93-58e5-4d3e-8f02-f3b8777f5b0e)


[1] Mingbo Cui, "License Plate Generation", https://github.com/MinboCui/license-plate-generation

[2] Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, and Alexei A. Efros. "Image-to-Image Translation with Conditional Adversarial Networks." In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2017.
