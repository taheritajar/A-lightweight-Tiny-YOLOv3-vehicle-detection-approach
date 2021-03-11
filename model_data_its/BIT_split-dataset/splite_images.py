
import cv2 as cv
import shutil
import os


out1 = "D:\yolov3\keras-yolo3\model_data_its\split-dataset/BIT_train.txt"
out2 = "D:\yolov3\keras-yolo3\model_data_its\split-dataset/BIT_test.txt"
dest1 =  "D:\yolov3\keras-yolo3\model_data_its\split-dataset/train_image/"
dest2 =  "D:\yolov3\keras-yolo3\model_data_its\split-dataset/test_image/"

#
#with open(out1,'r') as f:
#    lines = f.readlines()
#    print(len(lines))
#



for line in open(out2):
    line = line.split(' ')
    print(line[0])
  #frame = cv.imread(line[0])
  #cv.imshow("result", frame)
  #if cv.waitKey(0) & 0xFF == ord('q'):
  #  cv.destroyWindow("result")
#

    shutil.move(line[0],dest2)











