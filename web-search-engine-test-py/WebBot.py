# 구글,네이버와 같은 웹 검색 서비스를 제공하기 위해선 방대한 양의 웹 페이지를 수집해야 한다.

# 해당 방법은 사람이 혼자서 불가능한 작업이다.
# 초기에 수집할 Seed 사이트는 전달하지만 이 후에 수집할 웹 페이지는 전달 필요가 없다.
# 이를 도와주기 위한 웹 수집 로봇을 만들어보자

# 테이블을 만들어서 수집한 웹 페이지의 URL을 저장하고, 수집할 URL을 가져와서 수집하는 방식으로 만들어보자
# heidisql을 이용해서 데이터베이스를 만들어보자. (heidi를 사용할 떄 반드시 Mysql이나 MariaDB가 설치되어 있어야 한다.)

# 테이블은 crawling 외부 webscraping_table.sql 참고

import urllib.request as req
from bs4 import BeautifulSoup
from CandidateSql import CandidateSql
from WebPage import WebPage
from WebPageSql import WebPageSql
import threading

class WebBot:
    # 웹 페이지 수집 (Resopnse 객체 반환)
    @staticmethod
    def Collect(url):
        print("수집:",url)       # 수집: 출력 ------------------------
        request = req.Request(url)
        try:
            response = req.urlopen(request)
        except:
            return None
        else:
            if response.getcode() != 200:
                return None
            return response

    # 웹 페이지 수집(BeautifulSoup 개체 반환)
    @staticmethod
    def CollectHtml(url):
        response = WebBot.Collect(url)
        try:
            html = BeautifulSoup(response, 'html.parser')
        except:
            return None
        else:
            return html
    
    # 주기적으로 수집
    @staticmethod
    def CollectTM(period, tm_callback):      
        url,depth = CandidateSql.GetCandidate()    # 현재 url 값 안 가져옴
        res = WebBot.CollectHtml(url)    
        if res != None: 
            wp = WebPage.MakeWebPage(url,res)
            if wp != None:                
                WebPageSql.AddPage(wp)
                for url in wp.links:
                    CandidateSql.AddCandidate(url,depth+1)
                if tm_callback!=None:
                    tm_callback(url,depth,wp)
        timer = threading.Timer(period,WebBot.CollectTM,[period,tm_callback])
        timer.start()
    


# 수집했을 때 수행할 함수
cnt=0
def DoIt(url,depth,wp):
    global cnt
    print("{0}번째 페이지 {1},{2} 수집".format(cnt,url,depth))


seed_url = input("Seed 사이트 주소(ex:http://sample.co.kr):")
CandidateSql.AddCandidate(seed_url,0)   # 수집 후보 총 1개 추가 -> 1번째 페이지 수집
WebBot.CollectTM(5,DoIt)

        