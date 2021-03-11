import random
import cv2
import os
import shutil
#
size = (287,288)



output_folder = "D:\yolov3\keras-yolo3\model_data_its\BIT_split-dataset\\" + str(size[0]) + '\\'

if not os.path.exists(output_folder):
       os.makedirs(output_folder, 0o666)
######################################################################################################
file = "D:\yolov3\keras-yolo3\model_data_its\BIT_split-dataset/BIT_new_size.txt"
new_anot_text = output_folder + "BIT.txt"
outfilename1 = output_folder + "BIT_test_" + str(size) + ".txt"
outfilename2= output_folder + "BIT_train_"  + str(size) + ".txt"
outfilename11 = output_folder + "BIT_test__" + str(size) + ".txt"
outfilename22= output_folder + "BIT_train__"  + str(size) + ".txt"

with open(file,'r') as f:
    for lines in f:
        line = lines.split(' ')
        image = cv2.imread(line[0])
        (h, w) = image.shape[:2]
        image = cv2.resize(image, size)
        line0 = line[0].split('\\')
        #print(line0)
        out_z = output_folder + "image\\"
        out_r = out_z + line0[-1]
        #print(strrr)
        if not os.path.exists(out_z):
                os.makedirs(out_z, 0o666)
        cv2.imwrite(out_r,image)
        resize_factor_x = w / size[0]
        resize_factor_y = h / size[1]
        with open(new_anot_text, 'a') as out_f:
          line1 = line[0].split('\\')
          out_f.write(output_folder + "image\\"   + line1[-1] )
          
          for bbox in line[1:]:
              #print(bbox)
              if bbox != '\n':
                    out_f.write(' ')
                    # Here we are dealing with ground-truth annotations
                    x_min, y_min, x_max, y_max, class_id = list(map(int, bbox.split(',')))
                    out_box = '{},{},{},{},{}'.format(
                         int(x_min/resize_factor_x), int(y_min/resize_factor_y),int( x_max/resize_factor_x), int(y_max/resize_factor_y), class_id)
                    out_f.write(out_box)
          out_f.write("\n" )


with open(new_anot_text,'r') as f:
    lines = f.readlines()

random.shuffle(lines)
numlines = int(len(lines)*0.25)

with open(outfilename2, 'w') as f:
    f.writelines(lines[:numlines])
with open(outfilename1, 'w') as f:
    f.writelines(lines[numlines:])



for line in open(outfilename1):
    line = line.split(' ')
    out = output_folder+"test_image\\"
    if not os.path.exists(out):
           os.makedirs(out, 0o666)
    shutil.move(line[0],out)
    line3 = line[0].split('\\')
    with open(outfilename11, 'a') as f:
        f.writelines(out + line3[-1])
        for ant in line[1:]:
            f.writelines(' ' + ant)


for line in open(outfilename2):
    line = line.split(' ')
    out = output_folder+"train_image\\"
    if not os.path.exists(out):
           os.makedirs(out, 0o666)
    shutil.move(line[0],out)
    line3 = line[0].split('\\')
    with open(outfilename22, 'a') as f:
        f.writelines(out + line3[-1])
        for ant in line[1:]:
            f.writelines(' ' + ant)


os.rmdir(out_z)
os.remove(outfilename1)
os.remove(outfilename2)
os.remove(new_anot_text)









