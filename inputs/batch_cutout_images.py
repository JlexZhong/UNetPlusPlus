# coding: utf-8
from PIL import Image
import os
import os.path
import numpy as np
import cv2
#指明被遍历的文件夹
rootdir = r'E:\My Projects\UNet++\inputs\tmp'
save_path = r'E:\My Projects\UNet++\inputs\dataprocess_rock_dataset-unet'
for parent, dirnames, filenames in os.walk(rootdir):#遍历每一张图片
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)
   
        img = cv2.imread(currentPath)
        #img.show()
        cropped_img = img[60:460,60:460]
        # 60, 80, 425, 445 左上右下
        # 60 ,460, 60,460  左右上下
        # 中值滤波
        # medianfilter_img = cv2.medianBlur(cropped_img,3)
        # 保存
        cv2.imwrite(os.path.join(save_path,filename),cropped_img)
        print(filename)
