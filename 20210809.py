import pandas as pd
import json
import numpy as np
import ast
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.offline as offline
from datetime import datetime
from pandas.core.indexes import interval
import re

def get_interval_per_row(index, df):
    row_data = df.loc[index,:]
    start_time = row_data['start_time']
    if start_time != start_time:
        return -1
    start_time = datetime.strptime(str(start_time),"%Y-%m-%dT%H:%M:%S+08:00")

    stop_time = row_data['stop_time']
    if stop_time != stop_time:
        return -1
    stop_time = datetime.strptime(str(stop_time),"%Y-%m-%dT%H:%M:%S+08:00")

    total_minu = (stop_time - start_time).seconds / 60.0
    return total_minu


df_main = pd.read_excel('E:/桌面/暑期实习/openct数据集/20210809科学问题解决素养作答数据.xlsx')

time_minu_list = []
drop_index_list = []
for row in range(len(df_main)):
    interval_minu = get_interval_per_row(row, df_main)
    if interval_minu == -1:
        drop_index_list.append(row)
    else:
        time_minu_list.append(interval_minu)

df_main = df_main.drop(drop_index_list)
if 'interval_minutes' not in df_main.columns:
    df_main.insert(len(df_main.columns), 'interval_minutes', time_minu_list)

x1 = []
for row in range(len(df_main)):
    interval = df_main.iloc[row, 17]
    if interval != -1:
        x1.append(interval)

x1_sum = len(x1)

x1_ary, _ = np.histogram(x1, bins=[0,10,20,30,40,50,60])
x1_list = list(x1_ary)
x1_list.append(x1_sum - x1_ary.sum())

print(x1_list)

import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot
labels = ['小于10min','10min到20min','20min到30min','30min到40min','40min到50min','50min到60min', '超过60min']
trace = [go.Pie(labels=labels, values=x1_list)]
layout = go.Layout(
    title = '答题时间分布图',
)
fig = go.Figure(data = trace, layout = layout)
fig.show()

