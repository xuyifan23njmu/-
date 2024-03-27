import pandas as pd
import json
import os

# 文件夹路径
folder_path = 'output\get_mapping' 

# 获取文件夹中的所有文件名
filenames = os.listdir(folder_path)

# 初始化一个字典来存储转换后的数据
data = {}

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
            
            # 检查字典名是否已经在data字典中
            if dict_name not in data:
                data[dict_name] = {}  # 如果没有，则创建一个新的字典
            
            # 将键值对添加到对应的字典中
            data[dict_name][key] = value
# 检查 'chinese_sex' 是否在 data 字典中
if 'chinese_sex' in data:
    # 遍历 'chinese_sex' 字典
    for key in data['chinese_sex']:
        # 如果值为 'Female'，则替换为 '女性'
        if data['chinese_sex'][key] == 'Female':
            data['chinese_sex'][key] = '女性'
        # 如果值为 'Male'，则替换为 '男性'
        elif data['chinese_sex'][key] == 'Male':
            data['chinese_sex'][key] = '男性'
# 将data字典写入JSON文件
with open('json_rule\map_rules.json', 'w', encoding='utf-8') as json_file: 
    json.dump(data, json_file, ensure_ascii=False, indent=4)

