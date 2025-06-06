import os
from openai import OpenAI
# import openai
import numpy as np
import pandas as pd



# 设置 OPENAI_API_KEY 环境变量
os.environ["OPENAI_API_KEY"] = "sk-6Uri7XQ9qZskgLVwHpivrHz2IHDedoBwMDNIaVG9KPaxFXJO"
# 设置 OPENAI_BASE_URL 环境变量
os.environ["OPENAI_BASE_URL"] = "https://xiaoai.plus/v1"#/chat/completions

# openai.api_key = os.environ.get("OPENAI_API_KEY")
# openai.api_base = os.environ.get("OPENAI_BASE_URL")
client = OpenAI(
    # 下面两个参数的默认值来自环境变量，可以不加
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)

with open('./allclasses.txt', 'r', encoding='utf-8') as file:
    trainclasses = file.readlines()

# 去除每行末尾的换行符，并存储到列表中
animals = [line.strip() for line in trainclasses]

with open('./predicates.txt', 'r', encoding='utf-8') as file:
    attributes = file.readlines()

# 提取每行第一个空格后的内容，并存储到列表中
attributes = [line.split('\t')[-1].strip() if line.strip() else '' for line in attributes]

attributes_str=', '.join(attributes)
# 打印结果
print(attributes)

# animals=['antelope','grizzly+bear']
# ,'grizzly+bear','killer+whale','beaver'

all_response_animal_has_att=[]
all_response_att=[]
a=0
for animal in animals:
    prompt="Now there is an animal whose name is "+animal+". You need to expand as much as possible some attributes that it may have, please tell me the 15 most important attributes in your opinion, with each attribute described in a single word, all in lowercase letters, and attributes are separated by ', '. Ensure that these attributes are as distinctive as possible to differentiate each animal from the others. "
    completion = client.chat.completions.create(
    # completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a knowledgeable zoologist and know a lot about animals."},
            {"role": "user", "content": prompt}
        ]
    )
    print(animal)
    # print(completion)  # 响应

    response=completion.choices[0].message.content.split(", ")
    print(response,"本动物拥有的属性数量",len(response))  # 回答
    all_response_animal_has_att.append(response)
    for r in response:
        if r not in all_response_att and r not in attributes:
            all_response_att.append(r)

    print("所有添加的属性数量: ",len(all_response_att))

array=np.zeros((len(animals),len(all_response_att)))
for i in range(len(all_response_animal_has_att)):
    for j in range(len(all_response_att)):
        if all_response_att[j] in all_response_animal_has_att[i]:
            array[i][j]=1

df = pd.DataFrame(np.transpose(array), index=all_response_att, columns=animals)

# 保存为CSV文件
df.to_csv('./output_all_no_original_prompt_15_distinctive.csv', encoding='utf-8')
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a knowledgeable zoologist and know a lot about animals."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion)  # 响应
# print(completion.choices[0].message)  # 回答

