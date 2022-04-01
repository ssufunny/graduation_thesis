# Selenium 웹드라이버 사용으로 동적페이지 크롤링
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# 창을 키지않고도 백그라운드에서 코드 자동으로 돌린 후 원하는 결과 출력되도록
webdriver_options = webdriver.ChromeOptions()
webdriver_options .add_argument('headless')
driver = webdriver.Chrome(r"C:\Users\ryuhyisu\Downloads\chromedriver_win32 (1)\chromedriver", options=webdriver_options)

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
time.sleep(0.3)

#이미지+촬영지 검색
elem = driver.find_element(By.XPATH, value='//*[@id="sbtc"]/div[2]/div[2]/input')

#검색창 초기화
elem.clear()

#검색어 입력
elem.send_keys("촬영지")
elem.send_keys(Keys.ENTER)

#링크 있는 클래스 찾기
timeout = 10
element_present = EC.presence_of_element_located((By.CLASS_NAME, 'yuRUbf'))
WebDriverWait(driver, timeout).until(element_present)

#class:yuRUbf->a태그->href에 구하려는 url존재
find_class = driver.find_elements(By.CLASS_NAME, 'yuRUbf')
for i in range(len(find_class)):
    url = find_class[i].find_element(By.TAG_NAME,'a').get_attribute('href')
    if 'pdf' not in url:
        url_list.append(url)

# urls = driver.find_elements_by_xpath("//div[@class='yuRUbf']/a")
#         url1 = urls[0].get_attribute('href')
#         url2 = urls[1].get_attribute('href')

#링크별로 본문 수집 시작 -> 파일 저장
with open("본문수집.txt",  "w", encoding="UTF-8") as file:
    i = 0
    for content in url_list:
        i += 1
        driver.get(content)
        try:
            #p태그 우선 수집
            p_tag = driver.find_elements(By.TAG_NAME,'p')
            #본문텍스트 = p태그+span태그 결과 (중복 안되게 set으로)
            body_text = set(p_tag + driver.find_elements(By.TAG_NAME,'span'))
            
            time.sleep(1)
            for content in body_text:
                file.write(content.text)
                    
            time.sleep(1)
            print("본문 %d 수집 끝"%i)
            
        except:
            
            time.sleep(1)
            continue
            
# for a in url_list:
#     print(a)

# f = open('content_crawl.txt','w',encoding='utf-8')



# print("url 수집 끝, 해당 url 데이터 크롤링")
 
# for url in url_list: # 수집한 url 만큼 반복
#     driver.get(url) # 해당 url로 이동
 
#     driver.switch_to.frame('mainFrame')
#     overlays = ".se-component.se-text.se-l-default" # 내용 크롤링
#     contents = driver.find_elements_by_css_selector(overlays)
 
#     for content in contents:
#         content_list = content_list + content.text # content_list 라는 값에 + 하면서 점점 누적
