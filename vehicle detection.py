#!/usr/bin/env python
# coding: utf-8

# In[17]:


import cv2
import numpy as np

cap = cv2.VideoCapture("C:\Project_outdoor video1.mov")

while(cap.isOpened()):
    ret, img1 = cap.read()
    ret,img2 = cap.read()
    ret,img3 = cap.read()
    if ret:
        hsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        hsv2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        hsv3 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
        
        diff1 = cv2.absdiff(hsv1,hsv2)
        diff2 = cv2.absdiff(hsv2,hsv3)
        
        ret,diff1 = cv2.threshold(diff1,20,255,cv2.THRESH_BINARY)
        ret,diff2 = cv2.threshold(diff2,20,255,cv2.THRESH_BINARY)
        
        diff = cv2.bitwise_and(diff1,diff2)
        diff = cv2.resize(diff,(700,600))
        img1 = cv2.resize(img1,(700,600))
        cv2.imshow("Original",img1)
        cv2.imshow("Vehicle Detection",diff)
        
    if cv2.waitKey(350) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




