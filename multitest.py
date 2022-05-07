# Selenium 웹드라이버 사용으로 동적페이지 크롤링
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from selenium import webdriver
from multiprocessing import Pool, Manager, freeze_support
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

manager = Manager()
url_list = []


def app_list():
    global url_list
    url_list.append("https://forcar.tistory.com/535")
    url_list.append("https://m.blog.naver.com/feb2nd/221349052189")
    url_list.append(
        "https://m.blog.naver.com/PostView.nhn?blogId=soje1234&logNo=221480289268&referrerCode=0&searchKeyword=%EB%A7%8C%ED%9C%B4%EC%A0%95")
    url_list.append("https://leemsw.tistory.com/508")
    url_list.append(
        "https://withbbang.tistory.com/entry/%EC%95%88%EB%8F%99-%EB%A7%8C%ED%9C%B4%EC%A0%95-%ED%95%A9%EC%8B%9C%EB%8B%A4-%EB%9F%AC%EB%B8%8C-%EB%AF%B8%EC%8A%A4%ED%84%B0-%EC%85%98%EC%83%A4%EC%9D%B8-%EC%B")
    url_list.append("https://allets.com/contents/?contentsId=25877")
    url_list.append("https://blog.daum.net/skh7678/1728")
    url_list.append("http://www.mhns.co.kr/news/articleView.html?idxno=262865")
    url_list.append("http://www.toolmagazine.kr/webzine/sub/wz_view.jsp?bid=10&num=2349")
    url_list.append("http://www.ynamnews.co.kr/news/6703")
    url_list.append(
        "http://www.snubugo.net/index.php?vid=mountain&mid=mountain_notice&document_srl=559822&listStyle=viewer&page=8")
    url_list.append("https://www.mimint.co.kr/bbs/view.asp?strBoardID=place&bidx=248")
    url_list.append("http://www.snubugo.net/chungu/mountain_notice/559822")
    url_list.append("http://snubugo.net/559822")
    url_list.append("https://comple.co.kr/167")
    url_list.append(
        "http://korea.dreamwiz.com/?cddtc=&sword=%EB%AF%B8%EC%8A%A4%ED%84%B0+%EC%84%A0%EC%83%A4%EC%9D%B8&focus=rik")
    url_list.append("https://blog.allstay.com/domestic-travel/andong-spot-and-guesthouse/")
    url_list.append("https://blog.daum.net/deersunny/2796")
    url_list.append("http://mbiz.heraldcorp.com/view.php?ud=20200813000174")
    url_list.append("https://blog.daum.net/maimboy/7580535")
    url_list.append("https://www.segye.com/newsView/20180803003070")
    url_list.append("https://newsis.com/view/?id=NISX20180723_0000370765&cid=10609")


def content_crawling(url):
    global file, map_address
    # idx = url_list.index(url)
    driver.get(url)
    time.sleep(0.5)
    if (len(driver.window_handles) != 1):
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    try:
        # print("본문 %d 수집 시작" % idx)
        html = driver.page_source
        bsoup = BeautifulSoup(html, 'lxml')

        tag = bsoup.find_all(['p', 'span', 'br', 'figcaption'])
        address = bsoup.select('.se_address')
    except HTTPError as e:
        print("httperror")

    except:
        print("error")

    for content in tag:
        file.write(content.text + " ")
    for add in address:
        map_address.write(add.text + "\n")
    # print("본문 %d 수집 끝" % idx)


if __name__ == '__main__':
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_argument('headless')
    driver = webdriver.Chrome("C://graduation_thesis//chromedriver.exe")

    app_list()
    start_time = time.time()
    file = open("본문수집.txt", "w", encoding="UTF-8")
    map_address = open("address.txt", "w", encoding="UTF-8")

    pool = Pool(4)
    results = pool.map(content_crawling, url_list)
    pool.close()
    pool.join()

    print(time.time() - start_time)
