# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer  # 修改此行
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
import logging
import random
import jieba
import json

# 设置日志和警告
logging.getLogger('jieba').setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题


def load_stopwords(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            stopwords = f.read().splitlines()
        return stopwords

    except Exception as e:
        print(f"加载停用词文件时出错: {e}")
        return []


def load_news(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            news_list = json.load(f)

        data_list = []
        for news in news_list:
            data_list.append(news['content'])

        return data_list

    except Exception as e:
        print(f"加载新闻文件时出错: {e}")
        return []


# 加载数据
data_list = load_news('news.json')
data = random.sample(data_list, 20)


# 分词函数
def jieba_tokenize(text):
    text = text.strip()  # 去掉首尾空白
    return [word for word in jieba.cut(text) if word not in stopwords]


# 加载停用词
stopwords = load_stopwords('stopwords.txt')

# 构建TF-IDF模型（修改此行）
vectorizer = TfidfVectorizer(tokenizer=jieba_tokenize)
X = vectorizer.fit_transform(data)

# 计算余弦相似度
similarity_matrix = cosine_similarity(X)


# 打印和可视化余弦相似度矩阵
def print_similarity_matrix(similarity_df, max_rows=20):
    print("\n余弦相似度矩阵：")
    print(similarity_df.head(max_rows))  # 只打印前max_rows行

    # 可视化相似度矩阵
    plt.figure(figsize=(10, 8))
    sns.heatmap(similarity_df, cmap='coolwarm', annot=True, fmt=".2f",
                xticklabels=[f'文档 {i + 1}' for i in range(similarity_df.shape[1])],
                yticklabels=[f'文档 {i + 1}' for i in range(similarity_df.shape[0])])

    # plt.title("余弦相似度热图")
    # plt.xlabel("文档")
    # plt.ylabel("文档")
    plt.show()


# 创建相似度数据框以便传递给可视化函数
similarity_df = pd.DataFrame(similarity_matrix, columns=[f'文档 {i + 1}' for i in range(len(data))],
                             index=[f'文档 {i + 1}' for i in range(len(data))])

print_similarity_matrix(similarity_df)
