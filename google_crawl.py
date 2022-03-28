from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(r"C:\Users\ryuhyisu\Downloads\chromedriver_win32 (1)\chromedriver")

driver.maximize_window() # 창 최대화
#C:\Users\ryuhyisu\Desktop
url = "https://www.google.co.kr/imghp?hl=ko"
driver.get(url)

#구글이미지 검색창
driver.find_element(By.XPATH, value="//*[@id='sbtc']/div/div[3]/div[2]").click()

#이미지 업로드 화면 클릭
driver.execute_script("document.getElementById('dRSWfb').style.display = 'none';")
driver.execute_script("document.getElementById('FQt3Wc').style.display = 'block';")

#이미지 업로드 & 파일 선택 버튼 클릭
driver.find_element(By.CSS_SELECTOR, value="input[type='file']").send_keys(r"C:/Users/ryuhyisu/Desktop/도깨비.PNG")
time.sleep(0.2)
#이미지+촬영지 검색임
elem = driver.find_element(By.XPATH, value='//*[@id="sbtc"]/div[2]/div[2]/input')
#검색창 초기화
elem.clear()

#검색어 입력
elem.send_keys("촬영지")
elem.send_keys(Keys.ENTER)

#정보 수집 시작
#지정한 위치로 스크롤 내리기 (유사한 이미지를 포함하는 정보)
start = driver.find_element(By.XPATH, value='//*[@id="rso"]/div[3]/div[1]/div')
actions = ActionChains(driver)
actions.move_to_element(start).perform()

time.sleep(7)

# //*[@id="rso"]/div[3]/div[2]
# //*[@id="rso"]/div[3]/div[3]


# #url 수집코드
# url_list = []
# title_list = []
# #몇개의 페이지 크롤링할지 선택
# total_page = 2
# for i in range(1,3):
#     //*[@id="rso"]/div[3]/div[2]/div/div[1]/div[1]/div/a/div/cite
    
#     link = driver.find_element_by_class_name('yuRUbf')
    
# for i in range(1, 3):  # 1~2페이지까지의 블로그 내용을 읽어옴
#     url = 'https://section.blog.naver.com/Search/Post.nhn?pageNo='+ str(i) + '&rangeType=ALL&orderBy=sim&keyword=' + text
#     driver.get(url)
#     time.sleep(0.5)
 
#     for j in range(1, 3): # 각 블로그 주소 저장
#         titles = driver.find_element_by_xpath('/html/body/ui-view/div/main/div/div/section/div[2]/div['+str(j)+']/div/div[1]/div[1]/a[1]')
#         title = titles.get_attribute('href')
#         url_list.append(title)
 
# print("url 수집 끝, 해당 url 데이터 크롤링")
 
# for url in url_list: # 수집한 url 만큼 반복
#     driver.get(url) # 해당 url로 이동
 
#     driver.switch_to.frame('mainFrame')
#     overlays = ".se-component.se-text.se-l-default" # 내용 크롤링
#     contents = driver.find_elements_by_css_selector(overlays)
 
#     for content in contents:
#         content_list = content_list + content.text # content_list 라는 값에 + 하면서 점점 누적
