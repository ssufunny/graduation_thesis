# Selenium 웹드라이버 사용으로 동적페이지 크롤링
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from selenium import webdriver
from multiprocessing import Pool
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
driver = webdriver.Chrome("C://graduation_thesis//chromedriver.exe", options=webdriver_options)
#driver = webdriver.Chrome("C://graduation_thesis//chromedriver.exe")

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
driver.find_element(By.CSS_SELECTOR, value="input[type='file']").send_keys("C://Users//정보통신공학과//Desktop//미스터션샤인.jpeg")
driver.implicitly_wait(5)

#이미지+촬영지 검색
elem = driver.find_element(By.XPATH, value='//*[@id="sbtc"]/div[2]/div[2]/input')

#검색창 초기화
elem.clear()

#검색어 입력
elem.send_keys("촬영지")
elem.send_keys(Keys.ENTER)

#본문수집하지않을 링크 검사
def not_crawl_link(link):
    not_crawl = ['youtube','twitter','pdf','pinter']
    return "youtube" in link or "twitter" in link or "pdf" in link or "pinter" in link or "pixta" in link

#class:yuRUbf->a태그->href에 구하려는 url존재
for page in range(2,5):
    #첫페이지라면
    if (page == 2):
        #class:yuRUbf->a태그->href에 구하려는 url존재
        find_url1 = driver.find_elements(By.CLASS_NAME, 'ULSxyf')
        find_url2 = find_url1[2].find_elements(By.CLASS_NAME, 'yuRUbf')
        for i in range(len(find_url2)):
            url = find_url2[i].find_element(By.TAG_NAME, 'a').get_attribute('href')
            if not(not_crawl_link(url)):
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
    print((page-1), "페이지")
    #다음페이지 이동
    try:
        driver.find_element(By.XPATH, '//*[@id="xjs"]/table/tbody/tr/td[%d]' % (page+1)).click()
        driver.implicitly_wait(5)
    except:
        continue
print(time.time()-start)
collect = time.time()

#링크별로 본문 수집 시작 -> 파일 저장
file = open("본문수집.txt",  "w", encoding="UTF-8")
map_address = open("address.txt",  "w", encoding="UTF-8")

for url in url_list:
    idx = url_list.index(url)
    driver.get(url)
    time.sleep(0.5)
    if (len(driver.window_handles) != 1):
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    try:
        print("본문 %d 수집 시작" % idx)
        html = driver.page_source
        bsoup = BeautifulSoup(html, 'lxml')

        tag = bsoup.find_all(['p','span','br','figcaption'])
        address = bsoup.select('.se_address')
    except HTTPError as e:
        print("httperror")
        continue
    except:
        print("error")
        continue
    for content in tag:
        file.write(content.text+" ")
    for add in address:
        map_address.write(add.text+"\n")
    print("본문 %d 수집 끝" % idx)


print(time.time()-collect)

for a in url_list:
    print(a)

pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
pool.map(print_fibo, num_list) # pool에 일을 던져줍니다.
# for url in url_list: # 수집한 url 만큼 반복
#     driver.get(url) # 해당 url로 이동
 
#     driver.switch_to.frame('mainFrame')
#     overlays = ".se-component.se-text.se-l-default" # 내용 크롤링
#     contents = driver.find_elements_by_css_selector(overlays)
 
#     for content in contents:
#         content_list = content_list + content.text # content_list 라는 값에 + 하면서 점점 누적
