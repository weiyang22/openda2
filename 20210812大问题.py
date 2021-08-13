#coding=utf-8
import numpy as np
import pandas as pd
from datetime import datetime

df_main1 = pd.read_excel('E:\桌面\作答率完成率分析数据\所有个体信息.xlsx')
df_main2 = pd.read_excel('E:\桌面\已完成\高中生问卷四结果数据.xlsx')
start = []
stop = []
num = 0
for index in range(len(df_main1)):
    row_data1 = df_main1.loc[index,:]
    row_data2 = df_main2.loc[num,:]
    if row_data1['id'] != row_data2['ticket_id']:
        start.append('0')
        stop.append('0')
    else:
        start_time = row_data2['start_time']
        if start_time != start_time:
            start.append('0')
        else:
            start.append('1')

        stop_time = row_data2['stop_time']
        if stop_time != stop_time:
            stop.append('0')
        else:
            stop.append('1')
        num += 1

df_main1['start'] = start
df_main1['finish'] = stop
#df_main1.to_excel('E:\\桌面\\高中生问卷五概率结果.xlsx', index = False)

sum =  {'南山中学':0, '四川省绵阳中学':0, '四川省绵阳第一中学':0, '四川省绵阳实验高级中学':0, '绵阳普明中学':0, '四川省绵阳外国语学校':0, '四川省绵阳南山中学双语学校':0, '绵阳南山中学实验学校':0, '绵阳中学实验学校':0, '四川省绵阳市丰谷中学':0, '绵阳东辰国际学校':0, '绵阳市第三中学':0, '开元中学':0, '绵阳高新区实验中学':0, '四川省科学城第一中学':0, '三台中学校':0, '三台县芦溪中学':0, '三台一中':0, '三台中学实验学校':0, '四川省盐亭中学':0, '四川省绵阳市安州中学':0, '绵阳市秀水中学':0, '四川省梓潼中学校':0, '四川省北川中学':0, '四川省平武中学':0, '江油中学':0, '四川省江油市第一中学':0, '江油市太白中学':0, '江油外国语学校':0}
sanum =  {'南山中学':0, '四川省绵阳中学':0, '四川省绵阳第一中学':0, '四川省绵阳实验高级中学':0, '绵阳普明中学':0, '四川省绵阳外国语学校':0, '四川省绵阳南山中学双语学校':0, '绵阳南山中学实验学校':0, '绵阳中学实验学校':0, '四川省绵阳市丰谷中学':0, '绵阳东辰国际学校':0, '绵阳市第三中学':0, '开元中学':0, '绵阳高新区实验中学':0, '四川省科学城第一中学':0, '三台中学校':0, '三台县芦溪中学':0, '三台一中':0, '三台中学实验学校':0, '四川省盐亭中学':0, '四川省绵阳市安州中学':0, '绵阳市秀水中学':0, '四川省梓潼中学校':0, '四川省北川中学':0, '四川省平武中学':0, '江油中学':0, '四川省江油市第一中学':0, '江油市太白中学':0, '江油外国语学校':0}
stnum =  {'南山中学':0, '四川省绵阳中学':0, '四川省绵阳第一中学':0, '四川省绵阳实验高级中学':0, '绵阳普明中学':0, '四川省绵阳外国语学校':0, '四川省绵阳南山中学双语学校':0, '绵阳南山中学实验学校':0, '绵阳中学实验学校':0, '四川省绵阳市丰谷中学':0, '绵阳东辰国际学校':0, '绵阳市第三中学':0, '开元中学':0, '绵阳高新区实验中学':0, '四川省科学城第一中学':0, '三台中学校':0, '三台县芦溪中学':0, '三台一中':0, '三台中学实验学校':0, '四川省盐亭中学':0, '四川省绵阳市安州中学':0, '绵阳市秀水中学':0, '四川省梓潼中学校':0, '四川省北川中学':0, '四川省平武中学':0, '江油中学':0, '四川省江油市第一中学':0, '江油市太白中学':0, '江油外国语学校':0}

fin = []
sta = []
for index in range(len(df_main1)):
    df_row = df_main1.loc[index, :]

    for i in sum:
        if i == df_row['school']:
            sum[i] += 1
    for i in sanum:
        if i == df_row['school'] and df_row['start'] == '1':
            sanum[i] += 1
    for i in stnum:
        if i == df_row['school'] and df_row['finish'] == '1':
            stnum[i] += 1
print(sum)
print(sanum)
print(stnum)

print('get answer')