import requests
from bs4 import  BeautifulSoup
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"   }
img = requests.get(url = "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDEsNiw0LDIsNSw3LDgsOQ%3D%3D&word=%E7%8B%AD%E5%8F%B6%E7%93%B6%E5%B0%94%E5%B0%8F%E8%8D%89",headers = headers)
img.encoding='utf-8'
html = BeautifulSoup(img.text,"html.parser")

lay1 = html.find('div',id_='imgid',style_="width: 950px;")
print(lay1)


