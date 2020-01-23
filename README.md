# Udacity-Roversim
Sample and search rover autonomous exploration from roversim- Udacity. This repository contains implementation of Perception, Decision and autonomous navigation of the rover.

# 1. Perception 
The first step involves reading in images from the rover camera. In order to navigate autonomously through the environment, we need to use these 320x160 pixel camera images to determine where it is possible to drive. Throughout the environment, the sand on the ground is very light in color and everything else in the environment is dark. All you have to do to determine where you can drive is to figure out where the areas of lighter color are.
