
# coding: utf-8

# In[1]:

import numpy as np
import cv2
path = r'C:\Users\admin\Documents\Potholes\images\potholes_image3.jpg'

image = cv2.imread(path)

window_name = 'image'

cv2.imshow(window_name, image) 
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(17,17),0)
canny = cv2.Canny(blurred,60,150)
(cnts,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("The number of potholes in the image is : {}" .format(len(cnts)))
potholes = image.copy()
cv2.drawContours(potholes, cnts,-1, (255,0,0),3)
cv2.imshow("Contours",potholes)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:



