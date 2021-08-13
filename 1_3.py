import pandas as pd
import numpy as np
from datetime import datetime
import ast
import json


df_main = pd.read_excel('E:/桌面/暑期实习/问题解决素养完整数据2.xlsx')
PD = pd.DataFrame(columns=('1_问题1橙色曲线', '1_问题1绿色曲线','1_问题1蓝色曲线','1_问题2', '1_问题3橙色曲线', '1_问题3绿色曲线', '1_问题3蓝色曲线', '1_问题4', '1_问题5', '1_问题6', '2_问题1', '2_问题1', '2_问题1毛巾位置', '2_问题1水位高度', '2_问题2', '2_问题2', '2_问题3', '2_问题3', '2_问题4', '2_问题4', '2_问题5', '3_前言2鱼的数量', '3_前言2水面位置', '3_前言2水草数量', '3_问题1.1', '3_问题1.1', '3_问题1.1水面位置', '3_问题1.1水温', '3_问题1.2', '3_问题2.1', '3_问题2.2', '3_问题2.2', '3_问题2.3', '3_问题2.3鱼的数量', '3_问题2.3水面位置', '3_问题2.3水草数量', '3_问题2.4', '3_问题2.4', '3_问题2.5', '3_问题2.5'))
dict_answer = {'1':'A','2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '-1':'未作答'}
dict_B = {'0':'A','1':'B','2':'C', '3':'D', '4':'E', '5':'F', '-1':'未作答'}
dict_mao = {'0':'无毛巾', '1':'未进入水中','2':'进入水中','-1':'未作答'}
dict_shui = {'0':'水位0', '1':'水位1','2':'水位2','3':'水位3', '4':'水位4', '-1':'未作答'}
for row in range(len(df_main)):
    print(row)
    num = 0
    A = []
    B = []
    C = []
    D = []
    P = []
    dic_list_test = df_main.loc[row,'task_answers']
    frame_list = ast.literal_eval(dic_list_test)
    print(len(frame_list))
    for data in frame_list:
        jr = json.loads(data)
        A.append(jr['frame']['answer'])
    if len(A) != 3:
        
    B = np.array(A[0])
    C = np.array(A[1])
    D = np.array(A[2])
    for i in range(10):
        if i <7:
            std = str(B[i])
            for num in dict_answer:
                if std[1:len(std) - 1] == num:
                    P.append(dict_answer[num])
        elif i == 7:
            std = str(B[i])
            san = ''
            for stl in std:
                for num in dict_answer:
                    if stl == num:
                        san += dict_answer[num]
            if san == '':
                P.append('未作答')
            else:
                P.append(san)
        elif i >7:
            if B[i] == 'null':
                P.append('未作答')
            else:
                P.append(B[i])
    for i in range(11):
        if i == 5 or i == 7 or i == 10:
            if C[i] == 'text':
                P.append('未作答')
            else:
                P.append(C[i])
        elif i == 0 or i == 2 or i == 8:
            std = str(C[i])
            for num in dict_mao:
                if std == num:
                    P.append(dict_mao[num])
        elif i == 1 or i == 3 or i == 9:
            std = str(C[i])
            for num in dict_shui:
                if std == num:
                    P.append(dict_shui[num])
        elif i == 4 or i == 6:
            std = str(C[i])
            for num in dict_answer:
                if std == num:
                    P.append(dict_answer[num])
    for i in range(19):
        if i < 2:
            std = str(D[i])
            for stl in std:
                for num in dict_answer:
                    if stl == num:
                        P.append(num)
        elif i == 3 or i == 4:
            std = str(D[i])
            for stl in std:
                for num in dict_answer:
                    if stl == num:
                        P.append(dict_answer[num])
        elif i > 4 and i < 6:
            std = str(D[i])
            for stl in std:
                for num in dict_answer:
                    if stl == num:
                        P.append(num)
        elif i == 6:
            std = str(D[i])
            std = std[1:len(std) - 1]
            stdd = std.replace("'", '')
            P.append(stdd)
        elif i == 7 or i == 8:
            std = str(D[i])
            stdd = std.replace("\\n", '')
            if stdd == 'text':
                P.append('未作答')
            else:
                P.append(stdd[2:len(stdd) - 2])
        elif i == 9:
            std = str(D[i])
            for stl in std:
                for num in dict_answer:
                    if stl == num:
                        P.append(dict_answer[num])
        elif i == 10 or i == 11:
            std = str(D[i])
            stdd = std.replace("\\n", '')
            if stdd == 'text':
                P.append('未作答')
            else:
                P.append(stdd[2:len(stdd) - 2])
        elif i > 11 and i < 14:
            std = str(D[i])
            for stl in std:
                for num in dict_answer:
                    if stl == num:
                        P.append(num)
        elif i == 2 or i == 14:
            std = str(D[i])
            for stl in std:
                for num in dict_answer:
                    if stl == num:
                        P.append(int(num) -1)
        elif i == 15:
            std = str(D[i])
            for stl in std:
                for num in dict_answer:
                    if stl == num:
                        P.append(dict_answer[num])
        elif i == 16:
            std = str(D[i])
            stdd = std.replace("\\n", '')
            if stdd == 'text':
                P.append('未作答')
            else:
                P.append(stdd[2:len(stdd) - 2])
        elif i == 17:
            std = str(D[i])
            stdd = std.replace("'", '')
            std = stdd[1:len(stdd)-1]
            for num in dict_answer:
                if std == num:
                    P.append(dict_answer[num])
        elif i == 18:
            std = str(D[i])
            stdd = std.replace("\\n", '')
            if stdd == 'text':
                P.append('未作答')
            else:
                P.append(stdd[2:len(stdd) - 2])
    PD.loc[row] = P
PD.to_excel('E:/桌面/暑期实习/问题解决数据处理结果(1).xlsx', index=False)