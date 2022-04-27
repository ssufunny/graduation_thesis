import pandas as pd
import requests
import json

url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=5204b505ee5c0d2aa5ffa16314078b47&repNationCd=22041011&'

res = requests.get(url)
text = res.text

d = json.loads(text)

movie_list = []

for b in d['movieListResult']['movieList']:
    movie_list.append(b['movieNm'])

data = pd.DataFrame(movie_list)
data.to_csv("movie_list.txt", mode='w', encoding='utf-8', index=False)