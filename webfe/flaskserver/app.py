from flask import Flask, render_template, request, redirect, url_for
import os
# Selenium 웹드라이버 사용으로 동적페이지 크롤링
from bs4 import BeautifulSoup
from urllib.request import HTTPError
from urllib.request import URLError
from selenium import webdriver
from multiprocessing import Pool, Manager, freeze_support
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import time
import copyreg
import re
import numpy as np
import MeCab
from collections import Counter
import pandas as pd
import os


def get_driver():
    # 창을 키지않고도 백그라운드에서 코드 자동으로 돌린 후 원하는 결과 출력되도록
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_argument('headless')
    driver = webdriver.Chrome("C://graduation_thesis//chromedriver.exe")
    #driver = webdriver.Chrome("C://Users//ryuhyisu//Downloads//chromedriver_win32 (2)//chromedriver.exe")
    return driver

def not_crawl_link(link):
    not_crawl = ['youtube', 'twitter', 'pdf', 'pinter']
    return "youtube" in link or "twitter" in link or "pdf" in link or "pinter" in link or "pixta" in link or "facebook" in link

def generate_urls(filename):
    driver = get_driver()

    # 빅데이터 수집을 위한 url 리스트
    url_list = []

    # 구글 이미지 검색 이용
    google = "https://www.google.co.kr/imghp?hl=ko"
    driver.get(google)

    #driver.find_element(By.XPATH, value="//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div/div[2]/div[2]/button").click()


    # 구글이미지 검색창
    driver.find_element(By.XPATH, value="//*[@id='sbtc']/div/div[3]/div[2]").click()

    # 이미지 업로드 화면 클릭
    driver.execute_script("document.getElementById('dRSWfb').style.display = 'none';")
    driver.execute_script("document.getElementById('FQt3Wc').style.display = 'block';")

    # 이미지 업로드 & 파일 선택 버튼 클릭
    # driver.find_element(By.CSS_SELECTOR, value="input[type='file']").send_keys(
    #     "C://Users//정보통신공학과//Desktop//호텔.jpeg")
    driver.find_element(By.CSS_SELECTOR, value="input[type='file']").send_keys(
       "C:/graduation_thesis/graduation_thesis/webfe/flaskserver/"+filename)
    driver.implicitly_wait(5)

    # 이미지+촬영지 검색
    elem = driver.find_element(By.XPATH, value='//*[@id="sbtc"]/div[2]/div[2]/input')

    # 검색창 초기화
    elem.clear()

    # 검색어 입력
    elem.send_keys("촬영지")
    elem.send_keys(Keys.ENTER)

    # class:yuRUbf->a태그->href에 구하려는 url존재
    for page in range(2, 5):
        # 첫페이지라면
        if (page == 2):
            # class:yuRUbf->a태그->href에 구하려는 url존재
            find_url1 = driver.find_elements(By.CLASS_NAME, 'ULSxyf')
            find_url2 = find_url1[2].find_elements(By.CLASS_NAME, 'yuRUbf')
            for i in range(len(find_url2)):
                url = find_url2[i].find_element(By.TAG_NAME, 'a').get_attribute('href')
                if not (not_crawl_link(url)):
                    url_list.append(url)
            print("-----------페이지 1 수집 끝-----------")
        else:
            find_url3 = driver.find_elements(By.CLASS_NAME, 'ULSxyf')
            find_url4 = find_url3[0].find_elements(By.CLASS_NAME, 'yuRUbf')
            for i in range(len(find_url4)):
                url = find_url4[i].find_element(By.TAG_NAME, 'a').get_attribute('href')
                if not (not_crawl_link(url)):
                    url_list.append(url)
            print("-----------페이지 2 수집 끝-----------")
        print((page - 1), "페이지")

        # 다음페이지 이동
        try:
            driver.find_element(By.XPATH, '// *[ @ id = "botstuff"] / div / div[3] / table / tbody / tr / td[%d] / a' % (page + 1)).click()
            #driver.find_element(By.XPATH, '//*[@id="xjs"]/table/tbody/tr/td[%d]' % (page + 1)).click()
            driver.implicitly_wait(5)
        except:
            break
    driver.implicitly_wait(5)
    driver.quit()

    return url_list

def get_content(url):
    with open('myfile.txt', 'a', encoding="utf-8") as bigtextdata, open('address.txt','a',encoding="utf-8") as detaildata:

        data_list = []
        map_address = []
        time.sleep(0.3)
        res = requests.get(url)
        time.sleep(0.3)

        try:
            # print("본문 %d 수집 시작" % idx)
            html = res.text
            bsoup = BeautifulSoup(html, 'lxml')
            tag = bsoup.find_all(['div', 'p', 'b','span', 'br', 'figcaption', 'blockquote', 'strong'])

            map_title1 = bsoup.find_all("strong", "se-map-title")
            map_address1 = bsoup.find_all("p", "se-map-address")
            map_title2 = bsoup.find_all("strong", "tit_store")
            map_address2 = bsoup.find_all("span", "access")

        except HTTPError as e:
            print("httperror")
        except:
            print("error")

        for content in tag:
            data_list.append(content.text+" ")
            bigtextdata.write(content.text + " ")
        for title, address in zip(map_title1, map_address1):
            #map_address.append(title.text + "," + address.text + "\n")
            detaildata.write(address.text + "," + title.text + "\n")

        for title, address in zip(map_title2, map_address2):
            #map_address.append(title.text + "," + address.text + "\n")
            detaildata.write(address.text + "," + title.text + "\n")
        print("본문 수집 끝")

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("upload.html")
@app.route('/result', methods=['GET', 'POST'])
def form():
    result = ""
    if  request.method == 'POST':
        # 업로드된 파일 저장
        image = request.files['file']
        image.save(image.filename)
        # 웹크롤링 실행
        with open("myfile.txt", "w", encoding="utf-8") as f, open("address.txt", "w", encoding='utf-8') as ff:
            pass
        start_time = time.time()

        pool = Pool(processes=4)  # 4개의 프로세스를 사용합니다.
        pool.map(get_content, generate_urls(image.filename))  # get_contetn 함수를 넣어줍시다.
        pool.close()
        pool.join()
        flag = 1
        #testdata = str(time.time())

        print("--- %s seconds ---" % (time.time() - start_time))

        time.sleep(1)

        # 자연어처리
        #f = open("C://graduation_thesis//graduation_thesis//myfile.txt", 'r', encoding='utf-8')
        f = open("C://graduation_thesis//graduation_thesis//webfe//flaskserver//myfile.txt", 'r', encoding='UTF8')
        text_file = f.read()
        # Mecab 이용
        m = MeCab.Tagger()
        # parse 함수 사용(형태소 분석 & 품사 매칭)
        texts = m.parse(text_file)
        # 띄어쓰기, 줄바꿈마다 split
        words = re.split('[\t\n]', texts)

        tagging = []
        word = []

        # 단어와 품사 태깅 부분으로 배열 따로 지정
        for i in range(0, len(words) - 1):  # 배열 길이만큼 반복
            if i % 2 == 1:  # 품사 태깅
                tagging.append(words[i])
            else:  # 단어
                if words[i] != "EOS":  # "EOS" 제외한 단어만
                    word.append(words[i])

        num = -1
        place = []
        tags = []

        # 저장 하지 않을 장소
        not_save = ['지역', '국내', '대한민국', '한국', '중심', '장소', '도시', '현장', '해외', '내륙', '외국', '명소', '관광지', '아시아', '우주', '호텔',
                    '마을', '이곳', '예술', '델루나', '호실', '식당', '맛집', '슈퍼', '저승', '도서관', '사이', '해피초원목장']

        for i in tagging:
            tag, category, TF, read, word_type, first_tag, last_tag, exp = i.split(',')
            num += 1
            name = re.search("[가-힣]+", word[num])  # 한글
            if name:
                if (category == '지명') or (category == '장소'):
                    if (word[num] not in not_save):
                        place.append(word[num])
                        tags.append(tag)
                        count = Counter(place)
        place_count = []
        places = []

        for i, j in count.most_common(20):
            if len(i) >= 2:
                places.append(i)
                place_count.append(j)

        # 태그 넣기
        place_tags = []
        for i in range(len(places)):
            place_tag = tags[place.index(places[i])]
            place_tags.append(place_tag)
        count_NNG = place_tags.count('NNG')
        count_NNP = place_tags.count('NNP')
        # print(place_tags)
        # test용 print
        for i in range(len(places)):
            print(places[i], place_tags[i], place_count[i])
        #print(count_NNG, count_NNP)

        # 빈도수가 가장 많은 단어
        most_place = places[0]
        most_place_index = place.index(most_place)
        most_place_tag = tags[most_place_index]

        # 상호명 엑셀 파일 열기
        filenamenlp = 'C://graduation_thesis//build_list.xlsx'
        #filenamenlp = "C://Users//ryuhyisu//Downloads//build_list.xlsx"
        build_list = pd.read_excel(filenamenlp, engine="openpyxl", keep_default_na=False)

        addresses = []
        with open('address.txt', 'r', encoding='utf-8') as f:
            file_data = f.readlines()
            # print(file_data)
            for i in file_data:
                # address, build = i.split(',')
                addresses.append(i)

        # 빈도표로 장소 정보 알아내기
        # 빈도표에서 품사가 NNG인 단어를 포함하는 장소 찾기

        if place_count[place_tags.index('NNP')] < 1500:
            print(place_count[place_tags.index('NNP')])
            NNG_place = places[place_tags.index('NNG')]
            print(NNG_place)
            if NNG_place == '해변' or NNG_place == '해수욕장' or NNG_place =='바다':
                df_NNG_place = build_list.loc[build_list['Column2'].str.contains('해변|해수욕장|바다')]
            elif NNG_place == '터널':
                df_NNG_place = build_list.loc[build_list['Column2'].str.contains('터널|굴')]
            else:
                one = build_list['Column2'] == NNG_place
                print(one)
                if len(one) != 1:
                    df_NNG_place = build_list.loc[build_list['Column2'].str.contains(NNG_place)]
                    # print(df_NNG_place)
                else:
                    df_NNG_place = build_list[one]
        else:
            NNP_place = places[place_tags.index('NNP')]
            one = build_list['Column2'] == NNP_place
            if len(one) != 1:
                df_NNG_place = build_list.loc[build_list['Column2'].str.contains(NNP_place)]
            else:
                df_NNG_place = build_list[one]
        print(df_NNG_place)
        # NNG인 단어를 포함하는 장소의 목록이 1개가 될 때까지 NNP인 단어 함께 검색

        index1 = 0
        index2 = 0
        index3 = 0
        flag = 0
        while (len(df_NNG_place) != 1):
            if -1 < index1 < 10:
                NNP_place = places[place_tags.index('NNP', index1)]
                #print(index1, NNP_place)
                df_NNP_place = df_NNG_place.loc[df_NNG_place['Column1'].str.contains(NNP_place)]
                print(df_NNP_place)
                if df_NNP_place.empty:
                    df_NNP_place = df_NNG_place.loc[df_NNG_place['Column2'].str.contains(NNP_place)]
                    if df_NNP_place.empty:
                        df_NNP_place = df_NNG_place
                elif 5 < len(df_NNP_place) <= 10:
                    # print(10)
                    df_NNP_place = df_NNG_place.loc[df_NNG_place['Column2'].str.contains(NNP_place)]
                df_NNG_place = df_NNP_place
                index1 += 1
                # if len(df_NNP_place) <= 5:
                #     # print(5)
                #     df_NNP_place_last = df_NNP_place.iloc[0]
                #     # print(len(df_NNP_place_last))
                #     break
                # df_NNP_place_last = df_NNP_place_last

            elif index1 == 10 and -1 < index2 < 10:
                NNP_place = places[place_tags.index('NNP', index2)]
                #print(index2, NNP_place)
                for j in addresses:
                    # print(j)
                    if NNP_place in j:
                        address, build = j.split(',')
                        data = {'Column1': [address[0]], 'Column2': [build[0][:-1]]}
                        df_NNG_place = pd.DataFrame(data)
                    else:
                        df_NNG_place = df_NNP_place
                index2 += 1

            # elif index2 == 10 and index3 == 0:
            #     df_NNG_place = df_NNP_place_last
        print(df_NNG_place)
        flag = 2
        result = df_NNG_place['Column1'].values[0] + " " + df_NNG_place['Column2'].values[0]
        print(result)



    return render_template("map.html",a=result)
    #return render_template("map.html", a=str(flag))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)