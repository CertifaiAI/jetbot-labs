# Jetbot Labs

## Description

Official hands-on course materials for Jetbot course. Get teaching material here. [Google Drive](https://drive.google.com/drive/folders/1kouNSwzXxB1WmOn5PEQBK9Xc_rnNbilq?usp=sharing)

## Projects

## Day 1

### 1) Basic Motion using functions

In this example we will control the Jetbot by programming from our web browser some basic motor controls using functions.

### 2) Basic Motions using UI

In this example we will control the Jetbot by programming from our web browser some basic motor controls using User Interfaces such as sliders and buttons.

### 3) Controlling Jetbot using Gamepad controller

In this example we will control the Jetbot remotely by using a gamepad controller and display the live video stream using our Jetbot camera.

## Day 2

### 1) Numpy, Pillow and OpenCV

In this example we will learn the common functions used to operate on the Numpy, Pillow and OpenCV libraries.   

### 2) Linear Regression

In this example we will train a simple neural network on a regression task.

 ### 3) Collision Avoidance

In this example we will train the Jetbot to avoid collisions in a variety of scenarios. The following steps are required:

- **Data Collection** - Collect image classification dataset which consists of two classes, Blocked and Free.  
- **Train the model** - Perform model training using Transfer Learning technique to detect the two classes and help Jetbot to avoid collisions.  
- **Optimize the model** - Optimize the trained model using TensorRT for faster inference on the Jetson Nano.  
- **Live demo** - Finally, we run the collision avoidance live inference on the Jetbot.

## Day 3

### 1) Image Augmentation

In this example we will apply various image augmentations on a dataset by using PyTorch packages and display the results.

### 2) MnistClassifier

In this example we will train a deep neural network on a classification task using the Mnist Dataset 

### 3) Road Following

In this example we will train the Jetbot to follow a path on a track. The following steps are required:

- **Data Collection** - Collect image regression dataset which consists of image coordinate target points x and y. 
- **Train the model** - Perform model training using Transfer Learning technique to predict two continuous values x and y corresponding to a target point.  
- **Optimize the model** - Optimize the trained model by using TensorRT for faster inference on the Jetson Nano.  
- **Live demo** - Finally, we run the road following live inference on the Jetbot. 

## Day 4

### 1) Road Following + Collision Avoidance

In this example we will be combining both Road Following and Collision Avoidance models into one notebook so that we can perform *Road Following* as well as enable *Collision Avoidance* at the same time so that our Jetbot will be able to follow a specific path on the track and avoid any collision with obstacles that may come on its way.

## JetPack Image

Jetbot-labs related scripts have been tested on SD image "jetbot_JP4.3_JL1.24_PT1.30_0115.img"

## Reference

Hardware is using third party Waveshare Jetbot Kit

Sources: https://github.com/NVIDIA-AI-IOT/jetbot
