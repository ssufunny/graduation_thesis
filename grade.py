with open("C:/mecab/mecab-ko-dic/user-place.csv", 'r', encoding='utf-8') as f:
    file_data = f.readlines()
    for i in file_data:
        word, left_ID, right_ID, weight, tag, category, TF, read, word_type, first_tag, last_tag, exp = i.split(',')
        # 우선순위가 0이 아닌 단어와 우선순위 값 출력
        if weight != '0':
            print(word, weight)

with open("C:/mecab/mecab-ko-dic/user-place.csv", 'r', encoding='utf-8') as f:
    file_data = f.readlines()
print(file_data)

# 우선 순위 값을 다 0으로 바꾸고 다시 추가하는 코드
# 근데 너무 용량이 커서 안되는 듯 ㅜ
# with open("C:/mecab/mecab-ko-dic/user-place.csv", 'r', encoding='utf-8') as f:
#     file_data = f.readlines()
# for i in file_data:
#     word, left_ID, right_ID, weight, tag, category, TF, read, word_type, first_tag, last_tag, exp = i.split(',')
#     result = word + ',' + left_ID + ',' + right_ID + ',' + str(0) + ',' + tag + ',' + category + ',' + TF + ',' + read + ',' + word_type + ',' + first_tag + ',' + last_tag + ',' + exp
#     file_data.append(result)
#     # print(result)
# with open("C:/graduation_thesis/test.csv", 'w', encoding='utf-8') as f:
#     for line in file_data:
#         f.write(line)
#
# def append():



# # test용 print
#     print(word + ',,,,NNP,' + category + ',' + TF + ',' + result + ',*,*,*,*\n')