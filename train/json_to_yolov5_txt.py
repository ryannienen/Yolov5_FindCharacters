import json 
import numpy as np
import os
from pathlib import Path

# 抓出資料夾內所有檔案名稱(含附檔名)，路徑請自行跟換。
dir_jsonfile_path='./json'
dir_jsonfile_item = os.listdir(dir_jsonfile_path)

for i in dir_jsonfile_item:
    
    with open(f'{dir_jsonfile_path}/{i}',"r",encoding="utf-8") as f:
        data = json.load(f)
    for j in data['shapes']:
        if j['label'] == "###":
            pass
        elif len(j['label']) > 1:

            # 抓出json檔中，image的尺寸大小，因為後續要作數值計算，使用numpy
            img_width = np.array(data['imageWidth'], np.int32)
            img_height = np.array(data['imageHeight'], np.int32)

            # 抓出json檔中，Ground True(GT)四個點座標XY軸最大&最小值
            points = np.array(j['points'], np.int32)
            max_point = np.max(points, axis=0)
            min_point = np.min(points, axis=0)

            # GT中心點XY座標
            center_point = (max_point+min_point)/2

            # 轉成YOLOv5矩形框的寬跟高
            width_height = max_point-min_point

            # 以下設定參考YOUTUBE搜尋"繁體中文進階賽 yolo介紹"中，"Json to Yolo GT"片段
            Class = 0
            x_center = center_point[0]/img_width
            y_center = center_point[1]/img_height
            width = width_height[0]/img_width
            height = width_height[1]/img_height

            # 取出資料夾內檔名(不含副檔名)
            file_name = Path(i).stem

            # 設定存取路徑(.txt)
            dir_folder_path = './yolov5_training_txt'
            isExist = os.path.exists(dir_folder_path)
            if not isExist:
                os.makedirs(dir_folder_path)
            dir_txtfile_path = f'{dir_folder_path}/{file_name}.txt'

            # 最後寫入txt檔，特別注意，這邊是用'a'，如果有要重跑，要先刪除txt檔，否則原有內容會存在，新的資料會接在舊的後面，然後儲存。
            with open(dir_txtfile_path, 'a') as t:
                yolo_format = f'{Class} {x_center} {y_center} {width} {height}\n'
                t.write(yolo_format)
