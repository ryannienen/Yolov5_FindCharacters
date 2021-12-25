import json 
import numpy as np
import cv2

img=cv2.imread('./img/img_2.jpg')

with open('./json/img_2.json',"r",encoding="utf-8") as f:
    data = json.load(f)

for k in data['shapes']:
    if len(k['label']) == 1:
        points = np.array(k['points'], np.int32)
        line_color = (0, 0, 255) # BGR
        cv2.polylines(img, pts=[points], isClosed=True, color=line_color, thickness=3)
    elif k['label'] == "###":
        points = np.array(k['points'], np.int32)
        line_color = (255, 0, 0) # BGR
        cv2.polylines(img, pts=[points], isClosed=True, color=line_color, thickness=3)

    # 為了符合yolov5訓練模型的格式，測試抓取的座標是否正確    
    else:
        points = np.array(k['points'], np.int32)
        line_color = (0, 255, 0) # BGR
        cv2.polylines(img, pts=[points], isClosed=True, color=line_color, thickness=3)
        max_point = np.max(points, axis=0)
        min_point = np.min(points, axis=0)
        cv2.rectangle(img, (min_point[0], min_point[1]), (max_point[0], max_point[1]), (0, 0, 0), 3)

cv2.imshow('Result', img)
cv2.waitKey(0)
        
