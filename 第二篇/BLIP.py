import pandas as pd
from PIL import Image
import os
from transformers import BlipProcessor, BlipForConditionalGeneration
import openai
import random
import gensim.downloader as api
import numpy as np

# # 设置 OPENAI_API_KEY 环境变量
# os.environ["OPENAI_API_KEY"] = "sk-fli3OaPNdKUhcJEa15B8DbA2C3054a36B5F873D16308D1B5"
# # 设置 OPENAI_BASE_URL 环境变量
# os.environ["OPENAI_BASE_URL"] = "https://xiaoai.plus/v1"
# # 初始化 OpenAI 客户端
# openai.api_key = os.environ.get("OPENAI_API_KEY")
# openai.api_base = os.environ.get("OPENAI_BASE_URL")

# 加载BLIP模型和处理器
blip_processor = BlipProcessor.from_pretrained("./model/openai/blip-image-captioning-large")
blip_model = BlipForConditionalGeneration.from_pretrained("./model/openai/blip-image-captioning-large")

# image = Image.open("F:/cvpr20_DAZLE/data/CUB/CUB_200_2011/images/010.Red_winged_Blackbird/Red_Winged_Blackbird_0024_4180.jpg")
image = Image.open("F:/cvpr20_DAZLE/data/CUB/CUB_200_2011/images/012.Yellow_headed_Blackbird/Yellow_Headed_Blackbird_0065_8481.jpg")
# 处理图像
inputs = blip_processor(images=image, return_tensors="pt")

# 生成图像描述
outputs = blip_model.generate(**inputs)
description = blip_processor.decode(outputs[0], skip_special_tokens=True)
print(description)

def get_random_files_from_subfolders(main_folder, num_files=10):
    folder_files_dict = {}

    # 遍历主文件夹下的所有子文件夹
    for root, dirs, files in os.walk(main_folder):
        if files:
            # 随机选择指定数量的文件
            random_files = random.sample(files, min(num_files, len(files)))
            # 获取子文件夹的名字
            subfolder_name = os.path.basename(root)
            # 保存子文件夹名字和对应的文件路径
            folder_files_dict[subfolder_name] = [os.path.join(root, file).replace("\\","/") for file in random_files]

    return folder_files_dict

# 提取文本中的词向量
def get_sentence_vector(sentence, glove_model):
    words = sentence.split()
    word_vectors = [glove_model[word] for word in words if word in glove_model]
    if word_vectors:
        sentence_vector = np.mean(word_vectors, axis=0)
    else:
        sentence_vector = np.zeros(300)  # 假设GloVe词向量的维度是300
    return sentence_vector

# 主文件夹路径
main_folder = "F:/cvpr20_DAZLE/data/AWA2/Animals_with_Attributes2/JPEGImages"
# 获取随机选择的文件
random_files_dict = get_random_files_from_subfolders(main_folder, num_files=10)
# print(random_files_dict)

print('Loading pretrain w2v model')
model_name = 'word2vec-google-news-300'  # best model
glove_model = api.load(model_name)
dim_w2v = 300
print('Done loading model')
data = pd.DataFrame()
for subfolder, files in random_files_dict.items():
    # print(subfolder)
    #存储每个类的词向量
    class_vector = pd.DataFrame()
    for image_path in files:
        # 在这里添加你对每个文件的处理逻辑
        # print(image_path)
        image = Image.open(image_path)
        # 处理图像
        inputs = blip_processor(images=image, return_tensors="pt")

        # 生成图像描述
        outputs = blip_model.generate(**inputs)
        description = blip_processor.decode(outputs[0], skip_special_tokens=True)
        print(description)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a knowledgeable zoologist and know a lot about animals."},
                {"role": "user",
                 "content": f"Based on the following description, provide more detailed attributes and information about the scene: {description}"}
            ]
        )

        # 输出GPT-3.5生成的文本描述
        gpt_description = completion.choices[0].message['content']
        print("GPT-3.5生成的详细描述:", gpt_description)
        '''提取文本描述的词向量'''
        word2vector = get_sentence_vector(gpt_description,glove_model)
        # print(len(word2vector))
        df = pd.DataFrame([word2vector])
        class_vector = pd.concat([class_vector,df],ignore_index=True)
    # 计算每列的均值，得到1x300的向量
    mean_vector = np.mean(class_vector, axis=0)
    new_df = pd.DataFrame([mean_vector])
    new_df['animals'] = subfolder
    data = pd.concat([data,new_df],ignore_index=True) # n*301
    # print("每个类所对应的词向量为：",data.shape)
    # print(10)
print("每个类所对应的词向量为：",data.shape)
data.to_csv('./AWA2_BLIP_w2v.csv', encoding='utf-8')




'''
# 加载图像
image_path = "F:/cvpr20_DAZLE/data/AWA2/Animals_with_Attributes2/JPEGImages/antelope/antelope_10255.jpg"
image = Image.open(image_path)

# 处理图像
inputs = blip_processor(images=image, return_tensors="pt")

# 生成图像描述
outputs = blip_model.generate(**inputs)
description = blip_processor.decode(outputs[0], skip_special_tokens=True)

print(description)

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a knowledgeable zoologist and know a lot about animals."},
        {"role": "user", "content": f"Based on the following description, provide more detailed attributes and information about the scene: {description}"}
    ]
)

# 输出GPT-3.5生成的文本描述
gpt_description = completion.choices[0].message['content']
print("GPT-3.5生成的详细描述:", gpt_description)

'''
