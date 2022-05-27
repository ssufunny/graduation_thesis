# Selenium 웹드라이버 사용으로 동적페이지 크롤링
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from selenium import webdriver
from multiprocessing import Pool, Manager, freeze_support
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import time

def get_driver():
    # 창을 키지않고도 백그라운드에서 코드 자동으로 돌린 후 원하는 결과 출력되도록
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_argument('headless')
    #driver = webdriver.Chrome("C://graduation_thesis//chromedriver.exe")
    driver = webdriver.Chrome("C://Users//ryuhyisu//Downloads//chromedriver_win32 (2)//chromedriver.exe")
    return driver

def not_crawl_link(link):
    not_crawl = ['youtube', 'twitter', 'pdf', 'pinter']
    return "youtube" in link or "twitter" in link or "pdf" in link or "pinter" in link or "pixta" in link or "facebook" in link

def generate_urls():
    driver = get_driver()

    # 빅데이터 수집을 위한 url 리스트
    url_list = []

    # 구글 이미지 검색 이용
    google = "https://www.google.co.kr/imghp?hl=ko"
    driver.get(google)

    # 구글이미지 검색창
    driver.find_element(By.XPATH, value="//*[@id='sbtc']/div/div[3]/div[2]").click()

    # 이미지 업로드 화면 클릭
    driver.execute_script("document.getElementById('dRSWfb').style.display = 'none';")
    driver.execute_script("document.getElementById('FQt3Wc').style.display = 'block';")

    # 이미지 업로드 & 파일 선택 버튼 클릭
    # driver.find_element(By.CSS_SELECTOR, value="input[type='file']").send_keys(
    #     "C://Users//정보통신공학과//Desktop//호텔.jpeg")
    driver.find_element(By.CSS_SELECTOR, value="input[type='file']").send_keys(
        "C://Users//ryuhyisu//Desktop//도깨비.png")
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

    return url_list

def get_content(url):
    with open('myfile.txt', 'a', encoding="utf-8") as f, open('address.txt','a',encoding="utf-8") as f1:

        data_list = []
        map_address = []
        res = requests.get(url)
        time.sleep(0.5)

        try:
            # print("본문 %d 수집 시작" % idx)
            html = res.text
            bsoup = BeautifulSoup(html, 'lxml')
            tag = bsoup.find_all(['p', 'b','span', 'br', 'figcaption', 'blockquote', 'strong'])

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
            f.write(content.text + " ")
        for title, address in zip(map_title1, map_address1):
            #map_address.append(title.text + "," + address.text + "\n")
            f1.write(address.text + "," + title.text + "\n")

        for title, address in zip(map_title2, map_address2):
            #map_address.append(title.text + "," + address.text + "\n")
            f1.write(address.text + "," + title.text + "\n")
        print("본문 수집 끝")

if __name__ == '__main__':
    print("크롤링링링")
    with open("myfile.txt", "w", encoding="utf-8") as f:
        pass
    start_time = time.time()

    pool = Pool(processes=4)  # 4개의 프로세스를 사용합니다.
    pool.map(get_content, generate_urls())  # get_contetn 함수를 넣어줍시다.
    pool.close()
    pool.join()

    print("--- %s seconds ---" % (time.time() - start_time))