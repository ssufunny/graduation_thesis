import pandas as pd
import glob


# 파일 불러오기
filename = 'C://graduation_thesis//buildDB//build_place.xlsx'

# 도로명 주소 엑셀 파일에서 중복 제거하여 다시 엑셀로 저장
for i in range(0, 21):
    test_result = pd.read_excel(filename, sheet_name=i, engine="openpyxl")
    df_test_result = test_result.drop_duplicates(['Column4', 'Column5'], keep="first")  # 4, 5열 중복 제거
    table = df_test_result[['Column2', 'Column3', 'Column4', 'Column5']]    # 2, 3, 4, 5열만 저장
    xlsx_dir = 'C://graduation_thesis//buildDB//place_' + str(i) + '.xlsx'  # 새로 저장할 엑셀 파일 생성
with pd.ExcelWriter(xlsx_dir) as writer:
    table.to_excel(writer, sheet_name='place')

# 파일 Union
all_data = pd.DataFrame()
for f in glob.glob('C://graduation_thesis//buildDB//place_*.xlsx'): # place_로 시작하는 엑셀 파일 합치기
    df = pd.read_excel(f)
    all_data = all_data.append(df, ignore_index=True)
# 파일 저장
all_data.to_excel("C://graduation_thesis//buildDB//all_place.xlsx", header=True, index=False)

