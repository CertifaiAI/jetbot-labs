# Jetbot Labs

## Description

Official hands-on course materials for Jetbot course

## Projects

## Day 1: Basic Motion

In this example we will control the Jetbot by programming from our web browser some basic motor controls

## Day 2: Road Following

In this example we will train the Jetbot to follow a line. The following steps are required:

**Data Collection** - We collect image regression dataset which will allow the Jetbot to follow the line.  
**Train the model** - We perform model training by using a famous technique known as Transfer Learning.  
**Optimize the model** - We optimize our trained model using TensorRT for better performance on the Jetson Nano.  
**Live demo** - Finally, we run the road following live inference on the Jetbot.  

## Day 3: Collision Avoidance

In this example we will train the Jetbot to avoid collisions in a variety of scenarios. The following steps are required:

**Data Collection** - We collect image classification dataset which will allow the Jetbot to identify whether the road is blocked or free.  
**Train the model** - We perform model training by using an AI classifier to prevent the Jetbot from entering into dangeroud territory.  
**Optimizing the model** - We optimize our trained model using TensorRT for better performance on the Jetson Nano.  
**Live demo** - Finally, we run the collision avoidance live inference on the Jetbot.

## Day 4: Road Following + Collision Avoidance

In this example we will combine both Road Following and Collision Avoidance tasks so that the Jetbot will be able to follow the road and avoid any obstacles. The following steps are required:


## JetPack Image

Jetbot-labs related scripts have been tested on SD image "jetbot_JP4.3_JL1.24_PT1.30_0115.img"

## Reference

Hardware is using third party Waveshare Jetbot Kit

Sources: https://github.com/NVIDIA-AI-IOT/jetbot
