import os
from pathlib import Path

# 抓出資料夾內所有檔案名稱(不含附檔名)，路徑請自行跟換。
train_img_path = './images/train'
val_img_path = './images/val'
train_label_path = './labels/train'
val_label_path = './labels/val'

train_list_A = [Path(x).stem for x in os.listdir(train_img_path)]
train_list_B = [Path(x).stem for x in os.listdir(train_label_path)]
val_list_A = [Path(x).stem for x in os.listdir(val_img_path)]
val_list_B = [Path(x).stem for x in os.listdir(val_label_path)]

# 查看有哪些圖片檔案沒有字串內容
train_diff = set(train_list_A) - set(train_list_B)
val_diff = set(val_list_A) - set(val_list_B)

redundant_train_img = [f'{x}.jpg' for x in train_diff]
redundant_val_img = [f'{x}.jpg' for x in val_diff]

print(redundant_train_img)
print(redundant_val_img)

# # 移除那些沒有字串內容的圖片檔案
# for i in redundant_train_img:
#     path = f'{train_img_path}/{i}'
#     os.remove(path)
# for i in redundant_val_img:
#     path = f'{val_img_path}/{i}'
#     os.remove(path)