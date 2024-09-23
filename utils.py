import os
import cv2
import numpy as np

path = 'assests/Media.jpeg'
image = cv2.imread(path)
image = cv2.resize(image, (300, 500))

gold_head_lower =  np.array([12, 131, 119], dtype=np.uint8)
gold_head_upper = np.array([32, 151, 199], dtype=np.uint8)

pink_spring_lower = np.array([161, 186, 29], dtype=np.uint8)
pink_spring_upper = np.array([181, 206, 109], dtype=np.uint8)

pink_lower = np.array([160, 100, 100], dtype=np.uint8)
pink_upper = np.array([180, 255, 255], dtype=np.uint8)

knob_area_threshold = 50
spring_area_threshold = 1000
pink = (203, 192, 255)
gold = (0, 215, 255)

def detect_pink_spring_gold_knob(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # for gold knob
    mask = cv2.inRange(hsv_image, gold_head_lower, gold_head_upper)

    kernel = np.ones((5,5), dtype=np.uint8)
    dilated = cv2.dilate(mask, kernel, iterations=6)
    contours, hierarchy = cv2.findContours(image=dilated, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    image_copy = image.copy()
    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)
        area = cv2.contourArea(cont)
        print(area)
        if area > knob_area_threshold:        
            image_copy = cv2.rectangle(image_copy,(x,y),(x+w,y+h),gold,2)
            cv2.putText(image_copy, "gold knob", (x+w,y+h), 2, 0.7,gold, 1)
            # cv2.imshow('result1', image_copy)
            # cv2.waitKey(0)

    print('knob'+'-'*100)
    spring_mask = cv2.inRange(hsv_image, pink_lower, pink_upper)
    kernel = np.ones((6,6), dtype=np.uint8)
    dilated = cv2.dilate(spring_mask, kernel, iterations=2)
    contours, hierarchy = cv2.findContours(image=dilated, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    # image_copy = image.copy()
    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)
        area = cv2.contourArea(cont)
        print(area)
        if area > spring_area_threshold:        
            image_copy = cv2.rectangle(image_copy,(x,y),(x+w,y+h),pink,2)
            cv2.putText(image_copy, "Pink spring", (x-10,y-10), 2, 0.7, pink, 1)
            # cv2.imshow('result1', image_copy)
            # cv2.waitKey(0)

    return image_copy

