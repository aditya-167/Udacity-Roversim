# Udacity-Roversim
Sample and search rover autonomous exploration from roversim- Udacity. This repository contains implementation of Perception, Decision and autonomous navigation of the rover.

# 1. Perception 
The first step involves reading in images from the rover camera. In order to navigate autonomously through the environment, we need to use these 320x160 pixel camera images to determine where it is possible to drive. Throughout the environment, the sand on the ground is very light in color and everything else in the environment is dark. All you have to do to determine where you can drive is to figure out where the areas of lighter color are.

![image](https://user-images.githubusercontent.com/47297221/72996914-82f29400-3e21-11ea-9b88-f7776f61cb7d.png)

Mountains are relatively dark (low intensity values) in all three color channels, both the ground and the sky are brighter (higher intensity) in the red, green and blue channels. However, in all cases it looks like the ground is a bit brighter than the sky, such that it should be possible to identify pixels associated with the ground using a simple color threshold. 
A function that takes as its input a color image and a 3-tuple of color threshold values (integer values from 0 to 255), and outputs a single-channel binary image, which is to say an image with a single color channel where every pixel is set to one or zero. In this case, all pixels that were above the threshold should be assigned a value of 1, and those below a value of 0,

![image](https://user-images.githubusercontent.com/47297221/72997170-f3011a00-3e21-11ea-9f2a-09be9077359d.png)
image after thresholding at ((R,G,B)>=145) = 1
