import pandas as pd
import numpy as np
from datetime import datetime
import ast
import json


df_main = pd.read_excel('./data.xlsx')
PD = pd.DataFrame(columns=('1_问题1', '1_问题1','1_问题1','1_问题2', '1_问题3', '1_问题3', '1_问题3', '1_问题4', '1_问题5', '1_问题6', '2_问题1', '2_问题1', '2_问题2', '2_问题2', '2_问题3', '2_问题3', '2_问题4', '2_问题4', '2_问题5', '2_问题5', '2_问题5', '3_前言2鱼的数量', '3_前言2水面位置', '3_前言2水草数量', '3_问题1.1', '3_问题1.1', '3_问题1.1水面位置', '3_问题1.1水温', '3_问题1.2', '3_问题2.1', '3_问题2.2', '3_问题2.2', '3_问题2.3', '3_问题2.3鱼的数量', '3_问题2.3水面位置', '3_问题2.3水草数量', '3_问题2.4', '3_问题2.4', '3_问题2.5', '3_问题2.5'))
for row in range(200):
    A = []
    B = []
    C = []
    D = []
    P = []
    dic_list_test = df_main.loc[row,'task_answers']
    frame_list = ast.literal_eval(dic_list_test)
    for data in frame_list:
        jr = json.loads(data)
        A.append(jr['frame']['answer'])
    if len(A) != 3:
        continue
    n1 = 0
    n2 = 0
    n3 = 0
    B = np.array(A[0])
    C = np.array(A[1])
    D = np.array(A[2])
    for i in range(19):
        if i < 3:
            std = str(D[i])
            P.append(std)
        elif i == 3 or i == 4:
            std = str(D[i])
            P.append(std)
        elif i > 4 and i < 6:
            std = str(D[i])
            P.append(std)
        elif i == 6:
            std = str(D[i])
            std = std[1:len(std)-1]
            stdd = std.replace("'", '')
            P.append(stdd)
        elif i == 7 or i == 8:
            std = str(D[i])
            P.append(stdd[2:len(stdd) - 2])
        elif i == 9:
            std = str(D[i])
            P.append(std)
        elif i == 10 or i == 11:
            std = str(D[i])
            P.append(stdd[2:len(stdd) - 2])
        elif i > 11 and i < 15:
            std = str(D[i])
            P.append(std)
        elif i == 15:
            std = str(D[i])
            P.append(std)
        elif i == 16:
            std = str(D[i])
            P.append(stdd[2:len(stdd) - 2])
        elif i == 17:
            std = str(D[i])
            P.append(std)
        elif i == 18:
            std = str(D[i])
            P.append(stdd[2:len(stdd) - 2])
    PD.loc[row] = P
PD.to_excel('./answer.xlsx')
