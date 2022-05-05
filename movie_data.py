import pandas as pd
import openpyxl

filename = 'C://Users//jisu//Documents//한국외대//2022 - 1//정보통신종합설계//Data//movie_list.xlsx'
with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
    file_data = f.readlines()
file_data

movie_list = pd.read_excel(filename, engine="openpyxl")

for i in range(len(movie_list)):
    movie_name = movie_list.iloc[i, 1]
    # 받침 유무 판단
    if (ord(movie_name[-1]) - 44032) == 0:  # 받침 없음
        TF = 'F'
    else:
        TF = 'T'
    print(movie_name, TF)
    # mecab 사용자 사전에 추가
    # file_data.append(movie_name + ',,,,NNP,미디어명,' + TF + ',' + movie_name + ',*,*,*,*\n')
    # with open("C:/mecab/user-dic/nnp.csv", 'w', encoding='utf-8') as f:
    #     for line in file_data:
    #         f.write(line)