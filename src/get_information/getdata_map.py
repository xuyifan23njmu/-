import pandas as pd
import numpy as np
import json

# 定义一个函数，用于映射列
def map_columns(df, mapping_dict, suffix):
    # 如果 'Chinese_a_addition' 列存在于数据框中，那么在需要映射的列中增加几列
    if 'Chinese_a_addition' in df.columns:
        columns_to_map.extend(['chinese_age_addition', 'chinese_sex_addition', 'chinese_zhongzu_addition']) 
    # 使用循环为每一列添加新列
    for col in columns_to_map:
        new_col = col + suffix
        # 直接复制原列的数据
        if col in ['english_age', 'chinese_age', 'chinese_age_addition']:
            df[new_col] = df[col]
        else:
            # 检查列的数据类型
            if np.issubdtype(df[col].dtype, np.number):
                # 如果列的数据类型是数字，那么复制原列
                df[new_col] = df[col]
            else:
                # 如果列的数据类型不是数字，那么进行映射
                df[new_col] = df[col].map(mapping_dict[col])
        # 将原列和新列中的 None 或 NaN 替换为 'unknown'
        df[col] = df[col].fillna('unknown')
        df[new_col] = df[new_col].fillna('unknown')
        # 获取新列的位置
        col_index = df.columns.tolist().index(col)
        # 重新排序列名的列表
        cols = df.columns.tolist()
        cols = cols[:col_index+1] + [new_col] + cols[col_index+1:-1]
        df = df[cols]
    return df

def map_minzu(df, mapping_dict,  suffix):
    # 如果 'Chinese_a_addition' 列存在于数据框中，那么在需要映射的列中增加几列
    if 'Chinese_a_addition' in df.columns:
        columns_to_map_minzu.extend(['chinese_minzu_addition']) 
    for col in columns_to_map_minzu:
        new_col = col + suffix
        df[new_col] = df[col].map(mapping_dict[col])
        # 将原列和新列中的 None 或 NaN 替换为 'unknown'
        df[col] = df[col].fillna('unknown')
        df[new_col] = df[new_col].fillna('unknown')
        # 获取新列的位置
        col_index = df.columns.tolist().index(col)
        # 重新排序列名的列表
        cols = df.columns.tolist()
        cols = cols[:col_index+1] + [new_col] + cols[col_index+1:-1]
        df = df[cols]
    return df


# 读取 Excel 文件
df = pd.read_excel('output\llama_13b\llama2_13b.xlsx')  # 需要添加列的 Excel 文件
disease_column = df['disease']
# 需要映射的列
columns_to_map = ['english_age', 'english_sex', 'english_ethnicity_race', 'chinese_age', 'chinese_sex', 'chinese_zhongzu']
columns_to_map_minzu=['chinese_minzu']

# 读取json文件
with open(r'json_rule\map_rules.json', 'r',encoding='utf-8') as f:
    mapping_dict = json.load(f)

# 映射列
df = map_columns(df, mapping_dict, '_y')


# 读取第三个json文件
with open(r'json_rule\map_rules_minzuy2.json', 'r',encoding='utf-8') as f:
    mapping_dict_y2 = json.load(f)

# 映射列
df = map_minzu(df, mapping_dict_y2, '_y2')

# 读取第二个json文件
with open(r'json_rule\map_rules_minzuy1.json', 'r',encoding='utf-8') as f:
    mapping_dict_y1 = json.load(f)

# 映射列
df = map_minzu(df, mapping_dict_y1, '_y1')

df['disease'] = disease_column
# 将结果写入到一个新的 Excel 文件
df.to_excel('output\llama_13b\llama2_13b_adding_v2.0.xlsx', index=False)