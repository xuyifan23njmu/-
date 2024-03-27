import re
import pandas as pd
import json
import numpy as np

# 读取文本文件
df = pd.read_excel(r'data\llama2 13B\Llama-2-13b.xlsx')

column_data1 = df['English_a']
column_data2 = df['Chinese_a']
column_data3 = df['disease']
# 读取 JSON 文件
with open(r'json_rule\re_rules.json', 'r', encoding='utf-8') as f:
    regex_rules = json.load(f)

matches = ['english_age', 'english_sex', 'english_ethnicity_race','english_nationality','english_address', 
           'chinese_age', 'chinese_sex', 'chinese_zhongzu','chinese_minzu','chinese_nationality','chinese_address']

# 如果存在'Chinese_addition'列，读取这一列
if 'Chinese_a_addition' in df.columns:
    column_data4 = df['Chinese_a_addition']
    # 创建一个空的DataFrame用来存储匹配的数据
    result = pd.DataFrame(columns=['English_a','Chinese_a', 'Chinese_a_addition','english_age', 'english_sex', 'english_ethnicity_race','english_nationality','english_address', 
                                   'chinese_age', 'chinese_sex', 'chinese_zhongzu','chinese_minzu','chinese_nationality','chinese_address',
                                   'chinese_age_addition','chinese_sex_addition','chinese_zhongzu_addition','chinese_minzu_addition','chinese_nationality_addition','chinese_address_addition','disease'])
    # 添加新的匹配项
    matches.extend(['chinese_age_addition','chinese_sex_addition','chinese_zhongzu_addition','chinese_minzu_addition','chinese_nationality_addition','chinese_address_addition'])

    for data1, data2, data3, data4 in zip(column_data1, column_data2, column_data3, column_data4):

        result_dict = {'English_a': data1,'Chinese_a': data2,'Chinese_a_addition': data4,'disease': data3}
        for match in matches:
            # 根据匹配项选择数据
            data = data1 if 'english' in match else data2
            if 'addition' in match:
                data = data4

            # 检查 data 是否是空值
            if pd.isnull(data):
                continue

            match_result = 'Not mentioned'
            for rule in regex_rules[match]:
                found = re.findall(rule, str(data))
                if found:
                    match_result = found[0]
                    break
            result_dict[match] = match_result
        result = result._append(result_dict, ignore_index=True)

else:
    # 创建一个空的DataFrame用来存储匹配的数据
    result = pd.DataFrame(columns=['English_a','Chinese_a', 'english_age', 'english_sex', 'english_ethnicity_race','english_nationality','english_address', 
                                   'chinese_age', 'chinese_sex', 'chinese_zhongzu','chinese_minzu','chinese_nationality','chinese_address','disease'])
    for data1, data2, data3 in zip(column_data1, column_data2, column_data3):
        result_dict = {'English_a': data1,'Chinese_a': data2,'disease': data3}
        for match in matches:
            data = data1 if 'english' in match else data2
            # 检查 data 是否是空值
            if pd.isnull(data):
                continue

            match_result = 'Not mentioned'
            for rule in regex_rules[match]:
                found = re.findall(rule, str(data))
                if found:
                    match_result = found[0]
                    break
            result_dict[match] = match_result
        result = result._append(result_dict, ignore_index=True)
# 将DataFrame写入Excel文件
result = result.reset_index(drop=True)
result.index = result.index + 1  # 使索引从1开始
result.to_excel(r'output\llama_13b\llama2_13b.xlsx', index_label='序号')