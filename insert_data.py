import pandas as pd
import re

# mecab 사전에 추가
def append(file, result, category, TF):
    with open("C:/mecab/user-dic/" + file + ".csv", 'r', encoding='utf-8') as f:
        file_data = f.readlines()
    file_data.append(result + ',,,,NNP,' + category + ',' + TF + ',' + result + ',*,*,*,*\n')
    with open("C:/mecab/user-dic/" + file + ".csv", 'w', encoding='utf-8') as f:
        for line in file_data:
            f.write(line)
    # test용 print
    # print(result + ',,,,NNP,' + category + ',' + TF + ',' + result + ',*,*,*,*\n')

# 받침 유무 확인
def TF(result):
    name = re.search("[가-힣]+", result)
    if name:
        last = name.group()[-1]
        if ((ord(last)) - 44032) % 28 > 0:  # 받침 있음
            return 'T'
        else:
            return 'F'
    else:
        return '*'


# 엑셀 파일에서 미디어 이름 불러오기
def Media(media_list):
    file = 'nnp'
    category = '제목'
    filename = 'C://graduation_thesis//' + media_list + '.xlsx'
    media_data = pd.read_excel(filename, engine="openpyxl", keep_default_na=False)
    for i in range(len(media_data)):
        media_name = str(media_data.iloc[i, 0]).replace(" ", "")  # 공백 제거
        append(file, media_name, category, TF(media_name))

# 엑셀 파일에서 지명 불러오기
def Place(i):
    filename = 'C://graduation_thesis//buildDB//all_place.xlsx'
    place_sheet = pd.read_excel(filename, engine="openpyxl", keep_default_na=False)
    file = 'place'
    category = '지명'
    column = 'Column' + str(i)
    df_place = place_sheet.drop_duplicates([column], keep="first")
    for place_name in df_place[column].unique():
        if ' ' in place_name:
            result_left, result_right = place_name.split()
            append(file, result_left, category, TF(result_left))
            append(file, result_right, category, TF(result_right))
        else:
            result = place_name
            name = re.search("[가-힣]+", result)
            if name:
                append(file, result, category, TF(result))

# 엑셀 파일에서 상호명 불러오기
def Build():
    filename = 'C://graduation_thesis//build_list.xlsx'
    build_list = pd.read_excel(filename, engine="openpyxl", keep_default_na=False)
    file = 'place'
    category = '상호명'
    for i in range(len(build_list)):
        build_name = str(build_list.iloc[i, 1]).replace(" ", "")  # 공백 제거
        append(file, build_name, category, TF(build_name))

def main():
    Media('movie_list')
    Media('drama_list')
    Media('variety_list')
    Build()
    for i in range(2, 6):
        Place(i)

main()
