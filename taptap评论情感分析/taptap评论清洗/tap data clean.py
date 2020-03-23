# coding=gbk
import pandas as pd
import time
import re
import numpy as np


# 爬虫获取的数据的所在路径
csv_path = r'C:\Users\12517\PycharmProjects\NLP\projects\taptap评论情感分析\data\tap_reviews-extend.csv'
# 清洗后的数据的保存路径
clean_path = r'C:\Users\12517\PycharmProjects\NLP\projects\taptap评论情感分析\data\tap_reviews-extend cleaned.csv'

# 读取数据
data = pd.read_csv(csv_path, header=0, index_col='id')

# # 查看前20条数据和列名
# print(data[:20])
# print(data.columns)

# 将评论时间由时间戳转日期
data['updated_time'] = data['updated_time'].apply(lambda x: time.strftime('%Y-%m-%d', time.localtime(x)))
# 评论净支持数
data['net_support'] = data['ups'] - data['downs']
# 评论热度
data['heat'] = data['ups'] + data['downs']
data['heat'] = (data['heat'] - data['heat'].min()) / (data['heat'].max() - data['heat'].min())
# 评分
data['score'] = data['stars']*2

# 将游玩时间为0的标注为缺失值
data['spent'] = data['spent'].replace(0, np.nan)

# 清除无意义字符
data['contents'] = data['contents'].apply(lambda x: re.sub('&[\w]+;', '', str(x)))
data['contents'] = data['contents'].apply(lambda x: re.sub('\(\s*\)', '', str(x)))
# 删除用不上的列
data.drop(['ups', 'downs'], axis=1, inplace=True)
# 保存数据，转换成utf-8编码
data.to_csv(clean_path, encoding='utf_8_sig')