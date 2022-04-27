import requests

headers = {
    'Host' : 'openapi.naver.com',
    'User-Agent' : 'curl/7.9.1',
    'Accept' : '*/*',
    'X-Naver-Client-Id' : 'Sxg_kgi_H18Ty2iCZeyG',
    'X-Naver-Client-Secret' : 'mH7Av8f4Ap',
}

url = 'https://openapi.naver.com/v1/search/movie.json'

params = {
    'query' : '',   # 필수
    'display' : '100',   # 출력 수
    'country' : 'KR',   # 제작국가
    'yearfrom' : '2005' # 제작년도 시작
}

response = requests.get(url, headers=headers, params=params)

print(response.text)