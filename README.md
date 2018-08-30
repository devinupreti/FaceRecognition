# FaceRecognition
Contains code for Face Recognition Project

## Objective
The project aims to create a smart system capable of autonomously detecting and recognizing faces. 

## Dataset
The dataset was created by clicking pictures from a mobile camera and resizing them to a standard resolution of 200x266 pixels. The dataset contain images of 12 people. Each person has approximately 10 images.

## Introduction
This project is a facial recognition program in python that recognizes a face on giving an image as an input. A face recognizer object has been utilized in the project. For facial recognition it requires training the face recognizer object with images of the face of the person that is expected to recognize. Supervised learning is used to train the face recognizer object.  

The steps for this project are summarized as :  
1. Create dataset of images
2. Convert images to Grayscale
3. Detect face in image using Haarcascade
4. Create image array from these faces and create corresponding label array
5. Send image array and label array as parameters to face recognizer object (LBPH - local binary patterns histogram)
6. Calculate LBP value for each pixel and create LBP histogram for all images of a label (LBP values are features of an image object)
7. The recognizer is now able to predict label for face in a new image
8. After the prediction is obtained in a variable, using haarcascade and opencv a rectangle is drawn on the region of image that contains a face

## Dependencies  
OS, Numpy, Pillow, OpenCV, Tkinter and Flask.

