# Monitoring-Social-Distancing-AI
A software module in python which contains pre trained model (SSD-mobilenet) for person detection, homographic transformation function of OpenCV and the website for displaying violation statistics. 


## Brief of Project
  1. **Person Detection** - Initially, the trained neural networks for person detection are imported and added to the *model* folder. The model that I prefered was SSDMobileNet, which gave me decent accuracy and runtime. The model detects a person and returns the co-ordinates of its bounding box. 
  2. **Bird-Eye-View tranform** - This portion is important to have a good distance estimation compared to the naive pixel based distance calculation. 
  The whole co-ordinate system is converted to BEV. The *bird_view_transform_functions.py* file has the OpenCV function which does the job. This [link](https://docs.opencv.org/3.4.0/d9/dab/tutorial_homography.html#tutorial_homography_Demo3) contains more about homography transform concept which is what's happening behind the scenes in this bird eye view transform. 
  3. **Violation Analysis** - Now that we have the information of bounding box (person's position) and a good distance estimate from BEV, we can do violation analysis frame-by-frame. Each frame predicts the bounding boxes, performs homography transformation, estimates distance between each persons and alets abou the violators.A good feature that is added is - cluster detection. Apart from marking the violators, clusters are also marked with some color. This distincts them into groups. 
## How to run
  1. **Calibate first** - The *calibrate_with_mouse.py* function should be called to create a region in the video to be monitored. Default values are there if this is nt initialised.
  2. **Run *social_distanciation_video_detection.py*** - Run this file. First you choose which model to use from the list of models in the *model* folder. Second step is choosing the video file on which you need to perform the violation analysis. Third step is calibrating the distance beyond which you classify as a violation. Now, the processing starts and after sometime you can see the output file in the *output* folder. 
