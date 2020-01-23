import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image_name = 'roboimage.jpg'
image = mpimg.imread(image_name)

def color_thresh(img, rgb_thresh=(0, 0, 0)):
    color_select = np.zeros_like(img[:,:,0])
    above_threshold=((img[:,:,0]>rgb_thresh[0])&(img[:,:,1]>rgb_thresh[1])&(img[:,:,2]>rgb_thresh[2])) # Get values above threshold
    color_select[above_threshold]=1 #convert True values to 1
    return color_select
    
red_threshold = 145
green_threshold = 145
blue_threshold = 145
rgb_threshold = (red_threshold, green_threshold, blue_threshold)
colorsel = color_thresh(image, rgb_thresh=rgb_threshold)
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(21, 7), sharey=True)
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=40)

ax2.imshow(colorsel, cmap='gray')
ax2.set_title('Threshold', fontsize=40)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show() 