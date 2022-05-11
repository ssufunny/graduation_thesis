import pandas as pd
import re

filename = 'C://graduation_thesis//buildDB//all_place.xlsx'
place_sheet = pd.read_excel(filename, engine="openpyxl", keep_default_na=False)
with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
    file_data = f.readlines()
file_data

# mecab 사전에 추가
def append(result, TF):
    file_data.append(result + ',,,,NNP,지명,' + TF + ',' + result + ',*,*,*,*\n')
    with open("C:/mecab/user-dic/nnp.csv", 'w', encoding='utf-8') as f:
        for line in file_data:
            f.write(line)
# 받침 유무 확인
def TF(result):
    name = re.search("[가-힣]+", result)
    if name:
        last = result[-1]
        if ((ord(last)) - 44032) % 28 > 0:  # 받침 있음
            return 'T'
        else:
            return 'F'
# 엑셀 파일에서 지명 불러오기
def Place(i):
    column = 'Column' + str(i)
    df_place = place_sheet.drop_duplicates([column], keep="first")
    for place_name in df_place[column].unique():
        if ' ' in place_name:
            result_left, result_right = place_name.split()
            append(result_left, TF(result_left))
            append(result_right, TF(result_right))
        else:
            result = place_name
            name = re.search("[가-힣]+", result)
            if name:
                append(result, TF(result))

def main():
    for i in range(2, 6):
        Place(i)

main()

