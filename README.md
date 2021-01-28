# Jetbot Labs

## Description

Official hands-on course materials for Jetbot course. Get teaching material here. [Google Drive](https://drive.google.com/drive/folders/1kouNSwzXxB1WmOn5PEQBK9Xc_rnNbilq?usp=sharing)

## Projects

## Day 1

#### 1) [Basic Motion using functions](/notebooks/Day_1/Basic_Motion/1-Basic_motion_using_Functions.ipynb)

In this example we will control the Jetbot by programming from our web browser some basic motor controls using functions.

#### 2) [Basic Motions using UI](/notebooks/Day_1/Basic_Motion/2-Basic_motion_using_UI.ipynb)

In this example we will control the Jetbot by programming from our web browser some basic motor controls using User Interfaces such as sliders and buttons.

#### 3) [Controlling Jetbot using Gamepad controller](/notebooks/Day_1/Remote_Control)

In this example we will control the Jetbot remotely by using a gamepad controller and display the live video stream using our Jetbot camera.

## Day 2

#### 1) [Python Exercise](/notebooks/Day_2/Python_Exercise)

- Exercise for Python basic course.
- Learn how to import library, use classes and inheritance, syntax and data containers

#### 2) [Classification Exercise](/notebooks/Day_2/Classification_Exercise)

- Introduction to classification with PyTorch.
- Build simple classification fr0m scratch to understand the process of building models.

#### 3) [Collision Avoidance](/notebooks/Day_2/Collision_Avoidance)

In this example we will train the Jetbot to avoid collisions in a variety of scenarios. The following steps are required:

- **Data Collection** - Collect image classification dataset which consists of two classes, Blocked and Free.  
- **Train the model** - Perform model training using Transfer Learning technique to detect the two classes and help Jetbot to avoid collisions.  
- **Optimize the model** - Optimize the trained model using TensorRT for faster inference on the Jetson Nano.  
- **Live demo** - Finally, we run the collision avoidance live inference on the Jetbot.

## Day 3

#### 1) [Image Augmentation Exercise](/notebooks/Day_3/ImageAugmentation_Exercise)

In this example we will apply various image augmentations on a dataset by using PyTorch packages and display the results.

#### 2) [Convolutional Neural Network Exercise](/notebooks/Day_3/CNN_Exercise)

- Learn how to define CNN model for computer vision
- Learn how to use pretrained CNN model for transfer learning
  - [Download hymenoptera_data](https://drive.google.com/file/d/1Jt_zB0wixgwNqnCmsk44bjjArAMH80ZI/view?usp=sharing)

#### 3) [Regression Exercise](/notebooks/Day_3/Regression_Exercise)

- Build Regression Model from scratch with Pytorch
- Learn the differences when training Classification and Regression model

#### 4) [Road Following](/notebooks/Day_3/Road_Following)

In this example we will train the Jetbot to follow a path on a track. The following steps are required:

- **Data Collection** - Collect image regression dataset which consists of image coordinate target points x and y. 
- **Train the model** - Perform model training using Transfer Learning technique to predict two continuous values x and y corresponding to a target point.  
- **Optimize the model** - Optimize the trained model by using TensorRT for faster inference on the Jetson Nano.  
- **Live demo** - Finally, we run the road following live inference on the Jetbot. 

## Day 4

#### 1) [TensorRT Example](/notebooks/Day_4/Examples/Example_1_TensorRt.ipynb)

- Learn optimization process with TensorRt
- Learn the trade-off of TensorRt optimization

#### 2) [OnnxRuntime Example](/notebooks/Day_4/Examples/Example_2_OnnxRuntime.ipynb)

- Learn optimization process with OnnxRuntime
- Learn how to convert pytorch model to Onnx
- Learn the trade-off of OnnxRuntime optimization

#### 3) [Road Following + Collision Avoidance](/notebooks/Day_4/RoadFollowing+CollisionAvoidance.ipynb)

In this example we will be combining both Road Following and Collision Avoidance models into one notebook so that we can perform *Road Following* as well as enable *Collision Avoidance* at the same time so that our Jetbot will be able to follow a specific path on the track and avoid any collision with obstacles that may come on its way.

## JetPack Image

Jetbot-labs related scripts have been tested on SD image "jetbot_JP4.3_JL1.24_PT1.30_0115.img"

## Reference

Hardware is using third party Waveshare Jetbot Kit

Sources: https://github.com/NVIDIA-AI-IOT/jetbot
