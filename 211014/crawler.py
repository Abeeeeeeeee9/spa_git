import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9D%BC%EC%B6%9C%EC%9D%BC%EB%AA%B0%EB%AA%85%EC%86%8C',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#places=soup.select('#_sunrise_infoLayer > ul:nth-child(1) > li:nth-child(1)')
places=soup.select('#_sunrise_infoLayer>ul>li')
#_sunrise_infoLayer > ul:nth-child(1) > li:nth-child(1) > a > span.bd
#_sunrise_infoLayer > ul:nth-child(1) > li:nth-child(1) > a > img
for place in places:

        one_title=place.select_one('dl > dt > a')
        one_location=place.select_one('dl > dd:nth-child(2)')
        one_image=place.select_one(' a > img')
        if one_title is not None:
            print('명소:',  one_title.text)
        if one_location is not None:
            print('장소:', one_location.text)
        if one_image is not None:
            print('이미지 :', one_image['src'])
