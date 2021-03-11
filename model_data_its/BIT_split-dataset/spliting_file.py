import random

file = "D:\yolov3\keras-yolo3\model_data_its\split-dataset/BIT_new_size.txt"
outfilename1 = "D:\yolov3\keras-yolo3\model_data_its\split-dataset/BIT_test.txt"
outfilename2= "D:\yolov3\keras-yolo3\model_data_its\split-dataset/BIT_train.txt"



with open(file,'r') as f:
    lines = f.readlines()

random.shuffle(lines)
numlines = int(len(lines)*0.25)

with open(outfilename1, 'w') as f:
    f.writelines(lines[:numlines])
with open(outfilename2, 'w') as f:
    f.writelines(lines[numlines:])

















