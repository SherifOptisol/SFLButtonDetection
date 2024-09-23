import os
import cv2 

from utils import detect_pink_spring_gold_knob

video_capture = cv2.VideoCapture('assests/sfl requirement.mp4')
video_saver = cv2.VideoWriter(
                    f"assests/inference.mp4",
                    cv2.VideoWriter_fourcc(*'MJPG'), 
                    10, (500, 700) )
while True:
    flag, frame = video_capture.read()
    if not flag:
        break
    
    resized_frame = cv2.resize(frame, (500, 700))
    processed_frame = detect_pink_spring_gold_knob(resized_frame)
    video_saver.write(processed_frame)
    cv2.imshow("Camera", resized_frame)
    cv2.imshow("Detection", processed_frame)
    if cv2.waitKey(1) == ord('q'):
        break

video_capture.release()
video_saver.release()
