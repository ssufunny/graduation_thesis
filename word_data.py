# openApiKey = "B1845504E1E49356690872DC9FA7D299"
# params = "&target_type=search&req_type=json&part=word&q="
# q = "동"
# sort = "&sort=dict&start=1&num=100&advanced=y&type4=all&cat="
# cat = "57"
# openUrl = "https://opendict.korean.go.kr/api/search?certkey_no=3853&key=" + openApiKey + params + q + sort + cat

import pandas as pd
import openpyxl

filename = 'C://graduation_thesis//buildDB//build_gangwon.xlsx'

bulid_gangwon = pd.read_excel(filename, engine="openpyxl")

# df_Column2 = bulid_gangwon.drop_duplicates(['Column2'], keep="first")
# df_Column3 = bulid_gangwon.drop_duplicates(['Column3'], keep="first")
# df_Column4 = bulid_gangwon.drop_duplicates(['Column4'], keep="first")
# df_Column5 = bulid_gangwon.drop_duplicates(['Column5'], keep="first")

df = bulid_gangwon.drop_duplicates(['Column5'], keep="first")

# table_Colum2 = df_Column2[['Column2']]
# table_Colum3 = df_Column3[['Column3']]
# table_Colum4 = df_Column4[['Column4']]
# table_Colum5 = df_Column5[['Column5']]

table = df[['Column2', 'Column3', 'Column4', 'Column5']]


for i in range(len(table)):
    table.at[i, 'Column5']
# print(table)

# with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
#     file_data = f.readlines()
# file_data
# word = "모현읍"
# file_data.append(word + ',,,,NNP,지명,T,' + word + ',*,*,*,*\n')
# with open("C:/mecab/user-dic/nnp.csv", 'w', encoding='utf-8') as f:
#     for line in file_data:
#         f.write(line)
