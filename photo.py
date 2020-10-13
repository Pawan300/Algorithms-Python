# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 08:10:25 2018

@author: pawan_300
"""

from skimage.io import imread 
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

demo=(r"C:\Users\pawan_300\Desktop\demo.jpg")
image=imread(demo,as_gray=True)  #for access image 
plt.imshow(image,cmap=cm.gray)
plt.show()
print("data type : %s, shape : %s " %(type(image),image.shape))
image_crop=image[5:170,0:170] # for cropping image
plt.imshow(image_crop,cmap=cm.gray)
plt.show()

image_resize=resize(image,(60,60),mode='wrap')
plt.imshow(image_resize,cmp=cm.gray)
plt.show()