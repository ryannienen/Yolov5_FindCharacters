import json 
import numpy as np
import cv2
import os

# 抓出資料夾內所有檔案名稱(含附檔名)，路徑請自行跟換。
dir_imgfile_path='./img'
dir_imgfile_item = os.listdir(dir_imgfile_path)
dir_jsonfile_path='./json'
dir_jsonfile_item = os.listdir(dir_jsonfile_path)


for i,j in zip(dir_imgfile_item,dir_jsonfile_item):
    img_path=f'{dir_imgfile_path}/{i}'
    img=cv2.imread(img_path)

    # 讀取json資料夾內的每個json檔案
    with open(f'{dir_jsonfile_path}/{j}',"r",encoding="utf-8") as f:
        data = json.load(f)

    # 判斷label(字元、字串、###)內容，抓取座標，並畫圖。
    for k in data['shapes']:
        if len(k['label']) == 1:
            points = np.array(k['points'], np.int32)
            red_color = (0, 0, 255) # BGR
            cv2.polylines(img, pts=[points], isClosed=True, color=red_color, thickness=3)
        elif k['label'] == "###":
            points = np.array(k['points'], np.int32)
            red_color = (255, 0, 0) # BGR
            cv2.polylines(img, pts=[points], isClosed=True, color=red_color, thickness=3)
        else:
            points = np.array(k['points'], np.int32)
            red_color = (0, 255, 0) # BGR
            cv2.polylines(img, pts=[points], isClosed=True, color=red_color, thickness=3)
            
    # 儲存圖片
    dir_folder_path = './ground_truth'
    isExist = os.path.exists(dir_folder_path)
    if not isExist:
        os.makedirs(dir_folder_path)
    gt_filename=f'{dir_folder_path}/{i}'
    cv2.imwrite(gt_filename, img)
