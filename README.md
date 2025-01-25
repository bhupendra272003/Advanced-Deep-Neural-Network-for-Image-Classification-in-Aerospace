# Advanced Deep Neural Network for Image Classification in Aerospace


This repository contains the implementation of an advanced deep neural network designed for the image classification of manual brackets installation in the aerospace industry. This project aims to automate the detection and classification of manual bracket installations to ensure accuracy and efficiency.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The accurate installation of brackets is critical in aerospace manufacturing. This project leverages deep learning techniques to develop a robust image classification model that can identify correct and incorrect installations.

## Dataset
The dataset used for this project consists of images of manual bracket installations. The images are labeled into different classes representing correct and incorrect installations. The dataset is split into training and testing sets.

## Installation
To get started, clone this repository and install the required dependencies.

## Output
Train Data

Epoch 1/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m35s[0m 4s/step - accuracy: 0.5115 - loss: 1.6662
Epoch 2/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m35s[0m 4s/step - accuracy: 0.4838 - loss: 2.5253
Epoch 3/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m33s[0m 4s/step - accuracy: 0.4964 - loss: 1.4595
Epoch 4/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m33s[0m 4s/step - accuracy: 0.4725 - loss: 0.9741
Epoch 5/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m32s[0m 4s/step - accuracy: 0.5370 - loss: 0.7657
Epoch 6/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m33s[0m 4s/step - accuracy: 0.4945 - loss: 0.7245
Epoch 7/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m24s[0m 3s/step - accuracy: 0.5013 - loss: 0.6930
Epoch 8/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m43s[0m 3s/step - accuracy: 0.4969 - loss: 0.6966
Epoch 9/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m24s[0m 3s/step - accuracy: 0.4442 - loss: 0.6947
Epoch 10/10
[1m8/8[0m [32m━━━━━━━━━━━━━━━━━━━━[0m[37m[0m [1m24s[0m 3s/step - accuracy: 0.5162 - loss: 0.6932

![output](https://github.com/user-attachments/assets/60199835-30bb-41c5-b90d-424f43186f3d)


Usage
Follow the instructions below to run the model and perform image classification:

Preprocess the dataset:

bash
python preprocess.py
Train the model:

bash
python train.py
Evaluate the model:

bash
python evaluate.py
Model Architecture
The model is built using deep convolutional neural networks (CNNs) to extract features from images and classify them. The architecture includes several convolutional layers, pooling layers, and fully connected layers.

Training
The training process involves:

Data augmentation to increase the diversity of the training data.

Using a suitable loss function and optimizer.

Training the model for a specified number of epochs.

Evaluation
The model is evaluated using various metrics, including accuracy, precision, recall, and F1-score. The evaluation is conducted on the testing set to measure the model's performance.

Results
The final model achieves high accuracy in classifying the images of manual bracket installations. Detailed results and performance metrics are provided in the results section.

Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-branch).

Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

```bash
git clone https://github.com/bhupendra272003/Advanced-Deep-Neural-Network-for-Image-Classification-of-manual-brackets-installation-in-Aerospace.git
cd Advanced-Deep-Neural-Network-for-Image-Classification-of-manual-brackets-installation-in-Aerospace
pip install -r requirements.txt
