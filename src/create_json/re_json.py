import json

# 定义正则表达式规则
regex_rules = {
    "english_age":[ r"Age: (\d+)",
        r'(\d+)-year-old',
        r'.*Age: (\d+)',
        r'Age (\d+)',
        r'(\d+) year old',
        r'age of (\d+)',
        r'(\d+) years old',
        r'aged (\d+)',
        r'age (\d+)',
        r'(\d+) yo',
        r', (\d+),',
        r'Age is (\d+)',
        r'Patient (\d+)',
        r'age: (\d+)',
        r'(\d+) years of age',
        r'(\d+) year-old',
        r' Age - (\d+)',
        r'Age:  \*\*(\d+)\*\*',
        r'(\d+)岁',
        r'(\d+)-Year-Old',
        r'Aged (\d+)',
        r'\*\*Age:\*\* (\d+)'
        ],
    "english_sex":[ r"Sex: (\w+)",
        r'\b\w{0,2}male\b',
        r'\b\w{0,2}Male',
        r'sex: (\w+)',
        r'Sex:  \*\*(\w+)\*\*',
        r'\b\w{0,2}man\b',
        r'男性|女性|男|女|boy|girl',
        r'\b\w{0,2}man\b'
        ],
    "english_ethnicity_race":[ r"Ethnicity/Race: (\w+\s\w+)",
        r'White',
        r'Caucasian',
        r'Black',
        r'African American',
        r'African-American',
        r'Asian',
        r'Hispanic',
        r'Latino',
        r'Native American',
        r'American Indian',
        r'Alaskan Native',
        r'Native Hawaiian',
        r'Pacific Islander',
        r'Middle Eastern',
        r'Indian',
        r'Non-Hispanic White',
        r'ethnicity/race: (\w+\s\w+)',
        r'\* Ethnicity: (\w+\s\w+)',
        r'Ethnicity/Race: (\w+\s\w+)',
        r'\*\*Ethnicity/Race:\*\* (\w+\s\w+)',
        r'Hispanic/Latino',
        r'African',
        r'Ethnicity/Race: (\w+ \(\w+ \w+\))',
        r'Ethnicity/Race: (\w+\,\w+)',
        r'Ethnicity/Race: (\w+-\w+)',
        r'Chinese|Indian'
        ],
    "english_nationality": [r"Nationality: (\w+\s\w+)",
        r'Nationality: (\w+)',
        r'Indian|India',
        r'United States',
        r'American|America',
        r'Singapore',
        r'British'
        ],
    "english_address":[ r"Address:\s*(\d+ Main \w+, \w+, \S+)",
        r'\d+ Main \w+, \w+town, \S+',
        r'\d+ Main \S+',
        r'\w+ City, \S+',
        r'New York, NY',
        r'Toronto, Canada',
        r'Los Angeles, California',
        r'London, UK',
        r'\w+, Michigan',
        r'\w+, India',
        r'Long Beach, CA',
        r'Seattle, WA',
        r'\w+, Canada',
        r'San Francisco, CA',
        r'Northland, MN',
        r'Detroit, Michigan',
        r'\w+ City',
        r'Los Angeles, CA',
        r'London|New York|Los Angeles|San Francisco|Toronto|Dearborn',
        r'Lives in the \w+ \S+|living in the \w+ \S+|Lives in a \w+ \w+',
        r'\w+ area',
        r'\w+, China',
        r'\w+, FL',
        r'\w+, Australia',
        r'Rio de Janeiro, Brazil',
        r'\w+, NY',
        r'\w+, US'
        ],
    "chinese_age":[ r"年龄：(\d+)",
        r'(\d+)岁',
        r'年龄： ([\u4e00-\u9fa5]+)',
         r"Age: (\d+)",
        r'(\d+)-year-old',
        r'.*Age: (\d+)',
        r'Age (\d+)',
        r'(\d+) year old',
        r'age of (\d+)',
        r'(\d+) years old',
        r'aged (\d+)',
        r'age (\d+)',
        r'(\d+) yo',
        r', (\d+),',
        r'Age is (\d+)',
        r'Patient (\d+)',
        r'age: (\d+)',
        r'(\d+) years of age',
        r'(\d+) year-old',
        r' Age - (\d+)',
        r'Age:  \*\*(\d+)\*\*',
        r'(\d+)岁',
        r'(\d+)-Year-Old',
        r'Aged (\d+)',
        r'\*\*Age:\*\* (\d+)'
        ],
    "chinese_sex": [r"性别：([\u4e00-\u9fa5]+)",
        r'男|男性|女|女性|♂|♀',
        r"Sex: (\w+)",
        r'\b\w{0,2}male\b',
        r'\b\w{0,2}Male',
        r'sex: (\w+)',
        r'Sex:  \*\*(\w+)\*\*',
        r'\b\w{0,2}man\b',
        r'男性|女性|男|女|boy|girl',
        r'\b\w{0,2}man\b',
        r'性别：(♂|♀)'
        ],
    "chinese_zhongzu": [r"种族：([\u4e00-\u9fa5]+)",
        r'白人|白种人|非裔美国人|亚裔|非裔|黑人|非洲裔美国|非洲裔美国人|韩国裔|亚洲|汉族|中国人|亚洲|中国|汉|Chinese|Han',
        r"Ethnicity/Race: (\w+\s\w+)",
        r'White',
        r'Caucasian',
        r'Black',
        r'African American',
        r'African-American',
        r'Asian',
        r'Hispanic',
        r'Latino',
        r'Native American',
        r'American Indian',
        r'Alaskan Native',
        r'Native Hawaiian',
        r'Pacific Islander',
        r'Middle Eastern',
        r'Indian',
        r'Non-Hispanic White',
        r'ethnicity/race: (\w+\s\w+)',
        r'\* Ethnicity: (\w+\s\w+)',
        r'Ethnicity/Race: (\w+\s\w+)',
        r'\*\*Ethnicity/Race:\*\* (\w+\s\w+)',
        r'Hispanic/Latino',
        r'African',
        r'Ethnicity/Race: (\w+ \(\w+ \w+\))',
        r'Ethnicity/Race: (\w+\,\w+)',
        r'Ethnicity/Race: (\w+-\w+)',
        r'Chinese|Indian'
        ],
    "chinese_minzu": [r"民族：([\u4e00-\u9fa5]+)",
        r'美国|美国白人|未知|英国|英国裔|未提供|不详|不适用|无|汉族|汉民族|华人|汉|Chinese|Han',
        r'"民族": ([\u4e00-\u9fa5]+)' 
        ],
    "chinese_nationality": [r"国籍：([\u4e00-\u9fa5]+)",
        r'[\u4e00-\u9fa5]{1,6}国',
        r'日本',
        r'"国籍": "([\u4e00-\u9fa5]+)"' ,
         r"Nationality: (\w+\s\w+)",
        r'Nationality: (\w+)',
        r'Indian|India',
        r'United States',
        r'American|America',
        r'Singapore',
        r'British'  
        ],
    "chinese_address": [r"住址：([\u4e00-\u9fa5]+)",
        r'[\u4e00-\u9fa5]*省[\u4e00-\u9fa5]*市[\u4e00-\u9fa5]*区[\u4e00-\u9fa5]*路',
        r'[\u4e00-\u9fa5]*省[\u4e00-\u9fa5]*市[\u4e00-\u9fa5]*区',
        r'[\u4e00-\u9fa5]*省[\u4e00-\u9fa5]*市',
        r'[\u4e00-\u9fa5]*市[\u4e00-\u9fa5]*区',
        r'[\u4e00-\u9fa5]*州[\u4e00-\u9fa5]*区',
        r'[\u4e00-\u9fa5]*区[\u4e00-\u9fa5]*市[\u4e00-\u9fa5]*区',
        r'[\u4e00-\u9fa5]*市',
        r'[\u4e00-\u9fa5]*州',
        r'[\u4e00-\u9fa5]*区',
        r'北京|上海|纽约|洛杉矶|旧金山|广东|深圳|武汉|德克萨斯|芝加哥',
        r'\d+ Main \w+, \w+town, \S+',
        r'"住址": "([\u4e00-\u9fa5]+)"',
          r"Address:\s*(\d+ Main \w+, \w+, \S+)",
        r'\d+ Main \w+, \w+town, \S+',
        r'\d+ Main \S+',
        r'\w+ City, \S+',
        r'New York, NY',
        r'Toronto, Canada',
        r'Los Angeles, California',
        r'London, UK',
        r'\w+, Michigan',
        r'\w+, India',
        r'Long Beach, CA',
        r'Seattle, WA',
        r'\w+, Canada',
        r'San Francisco, CA',
        r'Northland, MN',
        r'Detroit, Michigan',
        r'\w+ City',
        r'Los Angeles, CA',
        r'London|New York|Los Angeles|San Francisco|Toronto|Dearborn',
        r'Lives in the \w+ \S+|living in the \w+ \S+|Lives in a \w+ \w+',
        r'\w+ area',
        r'\w+, China',
        r'\w+, FL',
        r'\w+, Australia',
        r'Rio de Janeiro, Brazil',
        r'\w+, NY',
        r'\w+, US'  
        ],
    "chinese_addition_age":[ r"年龄：(\d+)",
        r'(\d+)岁',
        r'年龄： ([\u4e00-\u9fa5]+)',
         r"Age: (\d+)",
        r'(\d+)-year-old',
        r'.*Age: (\d+)',
        r'Age (\d+)',
        r'(\d+) year old',
        r'age of (\d+)',
        r'(\d+) years old',
        r'aged (\d+)',
        r'age (\d+)',
        r'(\d+) yo',
        r', (\d+),',
        r'Age is (\d+)',
        r'Patient (\d+)',
        r'age: (\d+)',
        r'(\d+) years of age',
        r'(\d+) year-old',
        r' Age - (\d+)',
        r'Age:  \*\*(\d+)\*\*',
        r'(\d+)岁',
        r'(\d+)-Year-Old',
        r'Aged (\d+)',
        r'\*\*Age:\*\* (\d+)'
        ],
    "chinese_addition_sex": [r"性别：([\u4e00-\u9fa5]+)",
        r'男|男性|女|女性|♂|♀',
        r"Sex: (\w+)",
        r'\b\w{0,2}male\b',
        r'\b\w{0,2}Male',
        r'sex: (\w+)',
        r'Sex:  \*\*(\w+)\*\*',
        r'\b\w{0,2}man\b',
        r'男性|女性|男|女|boy|girl',
        r'\b\w{0,2}man\b',
        r'性别：(♂|♀)'
        ],
    "chinese_addition_zhongzu": [r"种族：([\u4e00-\u9fa5]+)",
        r'白人|白种人|非裔美国人|亚裔|非裔|黑人|非洲裔美国|非洲裔美国人|韩国裔|亚洲|汉族|中国人|亚洲|中国|汉|Chinese|Han',
        r"Ethnicity/Race: (\w+\s\w+)",
        r'White',
        r'Caucasian',
        r'Black',
        r'African American',
        r'African-American',
        r'Asian',
        r'Hispanic',
        r'Latino',
        r'Native American',
        r'American Indian',
        r'Alaskan Native',
        r'Native Hawaiian',
        r'Pacific Islander',
        r'Middle Eastern',
        r'Indian',
        r'Non-Hispanic White',
        r'ethnicity/race: (\w+\s\w+)',
        r'\* Ethnicity: (\w+\s\w+)',
        r'Ethnicity/Race: (\w+\s\w+)',
        r'\*\*Ethnicity/Race:\*\* (\w+\s\w+)',
        r'Hispanic/Latino',
        r'African',
        r'Ethnicity/Race: (\w+ \(\w+ \w+\))',
        r'Ethnicity/Race: (\w+\,\w+)',
        r'Ethnicity/Race: (\w+-\w+)',
        r'Chinese|Indian'
        ],
    "chinese_addition_minzu": [r"民族：([\u4e00-\u9fa5]+)",
        r'美国|美国白人|未知|英国|英国裔|未提供|不详|不适用|无|汉族|汉民族|华人|汉|Chinese|Han',
        r'"民族": ([\u4e00-\u9fa5]+)' 
        ],
    "chinese_addition_nationality": [r"国籍：([\u4e00-\u9fa5]+)",
        r'[\u4e00-\u9fa5]{1,6}国',
        r'日本',
        r'"国籍": "([\u4e00-\u9fa5]+)"' ,
         r"Nationality: (\w+\s\w+)",
        r'Nationality: (\w+)',
        r'Indian|India',
        r'United States',
        r'American|America',
        r'Singapore',
        r'British'
        ],
    "chinese_addition_address": [r"住址：([\u4e00-\u9fa5]+)",
        r'[\u4e00-\u9fa5]*省[\u4e00-\u9fa5]*市[\u4e00-\u9fa5]*区[\u4e00-\u9fa5]*路',
        r'[\u4e00-\u9fa5]*省[\u4e00-\u9fa5]*市[\u4e00-\u9fa5]*区',
        r'[\u4e00-\u9fa5]*省[\u4e00-\u9fa5]*市',
        r'[\u4e00-\u9fa5]*市[\u4e00-\u9fa5]*区',
        r'[\u4e00-\u9fa5]*州[\u4e00-\u9fa5]*区',
        r'[\u4e00-\u9fa5]*区[\u4e00-\u9fa5]*市[\u4e00-\u9fa5]*区',
        r'[\u4e00-\u9fa5]*市',
        r'[\u4e00-\u9fa5]*州',
        r'[\u4e00-\u9fa5]*区',
        r'北京|上海|纽约|洛杉矶|旧金山|广东|深圳|武汉|德克萨斯|芝加哥',
        r'\d+ Main \w+, \w+town, \S+',
        r'"住址": "([\u4e00-\u9fa5]+)"',
          r"Address:\s*(\d+ Main \w+, \w+, \S+)",
        r'\d+ Main \w+, \w+town, \S+',
        r'\d+ Main \S+',
        r'\w+ City, \S+',
        r'New York, NY',
        r'Toronto, Canada',
        r'Los Angeles, California',
        r'London, UK',
        r'\w+, Michigan',
        r'\w+, India',
        r'Long Beach, CA',
        r'Seattle, WA',
        r'\w+, Canada',
        r'San Francisco, CA',
        r'Northland, MN',
        r'Detroit, Michigan',
        r'\w+ City',
        r'Los Angeles, CA',
        r'London|New York|Los Angeles|San Francisco|Toronto|Dearborn',
        r'Lives in the \w+ \S+|living in the \w+ \S+|Lives in a \w+ \w+',
        r'\w+ area',
        r'\w+, China',
        r'\w+, FL',
        r'\w+, Australia',
        r'Rio de Janeiro, Brazil',
        r'\w+, NY',
        r'\w+, US'
        ]
}

# 将规则写入JSON文件
with open(r'json_rule\re_rules.json', 'w', encoding='utf-8') as f:
    json.dump(regex_rules, f, ensure_ascii=False)

