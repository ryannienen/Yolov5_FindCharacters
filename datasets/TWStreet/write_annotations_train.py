import os

dir_imgfile_path='./images/train'
dir_imgfile_item = os.listdir(dir_imgfile_path)
dir_txtfile_path = './annotations/train.txt'

for i in dir_imgfile_item:
    with open(dir_txtfile_path, 'a') as t:
        yolo_format = f'../datasets/TWStreet/images/train/{i}\n'
        t.write(yolo_format)