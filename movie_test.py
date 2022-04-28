from urllib.request import urlopen , Request
import json
import pandas as pd


# 한국 영화 목록 api
# 국가 코드 한국=22041011
url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=5204b505ee5c0d2aa5ffa16314078b47&repNationCd=22041011'

movie_list = []

for j in range(0,100): # 반복 범위 늘려야하는데 너무 느림 방법 찾기
    request = Request(url+"&curPage="+str(j)) # 영화 목록 api에 request 요청
    response_body = urlopen(request).read()
    # print(response_body)
    getJson = json.loads(response_body)["movieListResult"]["movieList"] # request로 요청 받은 response (json file)
    for i in range(0,len(getJson)):
        list = getJson[i]
        # print(list)
        movieNm = list["movieNm"]
        genreAlt = list["genreAlt"]
        # print(movieNm, genreAlt)
        if "성인물(에로)" not in genreAlt:
            if "애니메이션" not in genreAlt:
                if "기타" not in genreAlt:
                    movie_list.append(movieNm)

# txt 파일로 저장
data = pd.DataFrame(movie_list)
data.to_csv("movie_list.txt", mode='w', encoding='utf-8', index=False)
# print(movie_list)
        # #기본 정보 저장
        # movie = MovieList(movieNm=list["movieNm"]) # response에서 원하는 data 추출 후 삽입
        # movie.save()
    # return render(request,'review.html')