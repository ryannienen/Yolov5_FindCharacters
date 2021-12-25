import os

dir_imgfile_path='./images/val'
dir_imgfile_item = os.listdir(dir_imgfile_path)
dir_txtfile_path = './annotations/val.txt'

for i in dir_imgfile_item:
    with open(dir_txtfile_path, 'a') as t:
        yolo_format = f'../datasets/TWStreet/images/val/{i}\n'
        t.write(yolo_format)