
# !/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import json
from ipdb import set_trace

json_dir = "E:\\My Projects\\UNet++\\inputs\\dataprocess_rock_dataset-unet"
Allfiles = os.listdir(json_dir)

json_files = []

for file in Allfiles:
    if file.endswith('json'):
        json_files.append(file)

print(json_files)

json_dict = {}
# 需要修改的新名称
new_name = 'rock'

for json_file in json_files:
    
    
    jsonfile = json_dir +'/'+ json_file
    # 读单个json文件
    
    with open(jsonfile,'r',encoding = 'utf-8') as jf:

        info = json.load(jf)
        # print(type(info))
        # 找到位置进行修改
        for i,label in enumerate(info['shapes']):
            info['shapes'][i]['label'] = new_name
        # 使用新字典替换修改后的字典
        json_dict = info
        print(json_dict) 
    # set_trace()
    # 将替换后的内容写入原文件 
    with open(jsonfile,'w') as new_jf:
        json.dump(json_dict,new_jf)       

print('change name over!')

