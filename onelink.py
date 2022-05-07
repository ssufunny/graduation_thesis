# Selenium 웹드라이버 사용으로 동적페이지 크롤링
from attr import attr
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

start = time.time()
# 창을 키지않고도 백그라운드에서 코드 자동으로 돌린 후 원하는 결과 출력되도록
webdriver_options = webdriver.ChromeOptions()
webdriver_options .add_argument('headless')
driver = webdriver.Chrome(r"C:\Users\ryuhyisu\Downloads\chromedriver_win32 (1)\chromedriver")
driver.implicitly_wait(5)
# 빅데이터 수집을 위한 url 리스트
url_list = []

# 구글 이미지 검색 이용
google = "https://www.google.co.kr/imghp?hl=ko"
driver.get(google)

#구글이미지 검색창
driver.find_element(By.XPATH, value="//*[@id='sbtc']/div/div[3]/div[2]").click()

#이미지 업로드 화면 클릭
driver.execute_script("document.getElementById('dRSWfb').style.display = 'none';")
driver.execute_script("document.getElementById('FQt3Wc').style.display = 'block';")

#이미지 업로드 & 파일 선택 버튼 클릭
driver.find_element(By.CSS_SELECTOR, value="input[type='file']").send_keys(r"C:/Users/ryuhyisu/Desktop/도깨비.PNG")
# time.sleep(0.3)
driver.implicitly_wait(5)

#이미지+촬영지 검색
elem = driver.find_element(By.XPATH, value='//*[@id="sbtc"]/div[2]/div[2]/input')

#검색창 초기화
elem.clear()

#검색어 입력
elem.send_keys("촬영지")
elem.send_keys(Keys.ENTER)

# html = driver.page_source #URL에 해당하는 페이지의 HTML를 가져옴 
# soup = BeautifulSoup(html, 'html.parser') #앞서 Selenium에서 받아온 HTML을 BS에다 넣어준다.
# test_ids = soup.find_all(['p','span','br','figcaption'])  #id 속성이 "test_id"인 모든 요소를 리스트형태로 반환
html = driver.page_source
bsoup = BeautifulSoup(html, 'lxml')
find_url1 = bsoup.select('.ULSxyf')
find_url2 = find_url1[2].select('.yuRUbf')
for i in range(len(find_url2)):
     url = find_url2[i].find('a')['href']
     print(url)
#     print(url)

        # for url in find_url2:
        #     if not(not_crawl_link(url)):
        #         url_list.append(url) 
        #         print(url)
        # print("-----------페이지 1 수집 끝-----------") 
