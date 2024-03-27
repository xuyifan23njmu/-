import pandas as pd
import json
import os

# 文件夹路径
folder_path = r'output\get_mapping_minzu' 

# 获取文件夹中的所有文件名
filenames = os.listdir(folder_path)

# 初始化两个字典来分别存储两种不同的映射关系
data_y1 = {}
data_y2 = {}

# 对每个文件进行操作
for filename in filenames:
    # 检查文件是否是 Excel 文件
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        # 读取 Excel 文件
        df = pd.read_excel(os.path.join(folder_path, filename))
        
        # 遍历DataFrame中的每一行
        for index, row in df.iterrows():
            dict_name = row['索引']  # 第一列为字典名
            key = row['唯一值']  # 第二列为键
            value = row['分类']  # 第三列为值
            
            # 检查字典名是否已经在对应的字典中
            if 'y1' in filename:
                if dict_name not in data_y1:
                    data_y1[dict_name] = {}  # 如果没有，则创建一个新的字典
                # 将键值对添加到对应的字典中
                data_y1[dict_name][key] = value
            elif 'y2' in filename:
                if dict_name not in data_y2:
                    data_y2[dict_name] = {}  # 如果没有，则创建一个新的字典
                # 将键值对添加到对应的字典中
                data_y2[dict_name][key] = value

# 将两个字典分别写入两个JSON文件
with open(r'json_rule\map_rules_minzuy1.json', 'w', encoding='utf-8') as json_file:  # 相对路径
    json.dump(data_y1, json_file, ensure_ascii=False, indent=4)

with open(r'json_rule\map_rules_minzuy2.json', 'w', encoding='utf-8') as json_file:  # 相对路径
    json.dump(data_y2, json_file, ensure_ascii=False, indent=4)
