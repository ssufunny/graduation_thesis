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
driver = webdriver.Chrome(r"C:\Users\ryuhyisu\Downloads\chromedriver_win32 (1)\chromedriver")
driver.implicitly_wait(5)
# 빅데이터 수집을 위한 url 리스트
url_list = []
google = "https://post.naver.com/viewer/postView.nhn?volumeNo=23610539&memberNo=41596968"
driver.get(google)

driver.get_text()



