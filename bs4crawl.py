# Selenium 웹드라이버 사용으로 동적페이지 크롤링
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
driver.implicitly_wait(5)

def not_crawl_link(link):
    not_crawl = ['youtube','twitter','pdf','pinter']
    return "youtube" in link or "twitter" in link or "pdf" in link or "pinter" in link

print("-----------페이지 수집 시작-----------")
#1,2,3페이지까지 수집
for page in range(2,4):
    html = driver.page_source
    bsoup = BeautifulSoup(html, 'lxml')
    #첫페이지라면
    if (page == 2):
    #class:yuRUbf->a태그->href에 구하려는 url존재
        find_url1 = bsoup.select('.ULSxyf')
        find_url2 = find_url1[2].select('.yuRUbf')
        for i in range(len(find_url2)):
            url = find_url2[i].find('a')['href']
            if not(not_crawl_link(url)):
                url_list.append(url) 
        print("-----------페이지 1 수집 끝-----------") 
    else:
        find_url3 = bsoup.select('.ULSxyf')
        find_url4 = find_url3[0].select('.yuRUbf')
        for i in range(len(find_url4)):
            url = find_url4[i].find('a')['href']
            if not(not_crawl_link(url)):
                url_list.append(url) 
        print("-----------페이지 2 수집 끝-----------") 
    print((page-1), "페이지")
    #다음페이지 이동
    try:
        driver.find_element_by_xpath('//*[@id="xjs"]/table/tbody/tr/td[%d]/a' %(page+1)).click()
        driver.implicitly_wait(5)
    except:
        continue
print(time.time()-start)  

collect = time.time()
# 링크별로 본문 수집 시작 -> 파일 저장
with open("본문수집.txt",  "w", encoding="UTF-8") as file:
    i = 0
    for content in url_list:
        i += 1
        # crawling_main_text(content)
        driver.get(content)
        driver.implicitly_wait(5)
        try:
            #p태그 우선 수집
            
            p_tag = driver.find_elements(By.TAG_NAME,'p')
            driver.implicitly_wait(5)
            span_tag = driver.find_elements(By.TAG_NAME, 'span')
            driver.implicitly_wait(5)

            body = p_tag + span_tag
            try:
                br_tag = driver.find_elements(By.TAG_NAME, 'br')
                driver.implicitly_wait(5)
            except:
                print("")
                
            body += br_tag
            driver.implicitly_wait(5)
                        
        except:       
            # time.sleep(1)
            continue
        for content in body:
            file.write(content.text)
            driver.implicitly_wait(5)
        print("본문 %d 수집 끝"%i)    
print(time.time()-collect)            
for a in url_list:
     print(a)

