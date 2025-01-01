import urllib.request as ureq
from bs4 import BeautifulSoup

def Collect(url):
    request = ureq.Request(url)
    response = ureq.urlopen(request)
    if response.getcode()!=200:
        return None
    else:
        return response

url = input("수집할 URL:")
result =  Collect(url)
html = BeautifulSoup(result,'html.parser')
print("제목:",html.title.text)
print("내용:")
print(html.text)