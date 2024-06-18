# MNIST Digit Classification with TensorFlow and Keras

This project demonstrates my initial venture into Machine Learning by building, training, and evaluating a neural network model to classify handwritten digits from the MNIST dataset using the Keras library from TensorFlow.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Work](#future-work)
- [License](#license)

## Overview

The objective of this project is to accurately classify digits (0-9) from the MNIST dataset. The dataset contains a total of 70,000 grayscale images, divided into 60,000 training images and 10,000 testing images.

## Dataset

The MNIST dataset is a collection of 70,000 handwritten digit images:
- 60,000 training images
- 10,000 testing images

## Model Architecture

The neural network model is constructed using the Sequential API in Keras and includes the following layers:
- **Flatten Layer:** Converts each 28x28 image into a 1D array of 784 pixels.
- **Dense Layer 1:** Fully connected layer with 128 neurons and ReLU activation.
- **Dense Layer 2:** Fully connected layer with 128 neurons and ReLU activation.
- **Dense Layer 3:** Output layer with 10 neurons (one for each digit) and softmax activation for classification.

The model is compiled with the Adam optimizer, sparse categorical cross-entropy as the loss function, and accuracy as the evaluation metric.

## Installation

To run this project, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/sansh72/mnist-digit-classification.git
