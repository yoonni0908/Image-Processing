#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import cv2

low = (0,35,100)
high = (20,255,255)

cap = cv2.VideoCapture("C:\Hand Video2.mov")

kernel = np.ones((9,9),np.uint8)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_mask = cv2.inRange(hsv, low, high)
        color_mask = cv2.dilate(color_mask,kernel,iterations=1)
        re_1 = cv2.resize(color_mask,(700,600))
        re_2 = cv2.resize(frame,(700,600))
        cv2.imshow('hand detection',re_1)
        cv2.imshow('original',re_2)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




