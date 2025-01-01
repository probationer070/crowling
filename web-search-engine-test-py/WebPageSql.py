from SqlCon import SqlCon
from WebPage import WebPage 

class WebPageSql:
    # Page 수집시 테이블에 추가하는 함수
    @staticmethod
    def AddPage(wpage):
        cursor = SqlCon.Cursor()
        try:
            query = str.format("INSERT INTO WebPage (title, url, description, mcnt) VALUES ('{0}', '{1}', '{2}', '{3}')", wpage.title, wpage.url, wpage.description, wpage.mcnt)
            cursor.execute(query)
            SqlCon.Commit()
        except:
            return False
        else:
            return True
    
    # 페이지 내 포함 단어 항목 갱신
    @staticmethod
    def UpdateMcnt(url, mcnt):
        cursor = SqlCon.Cursor()
        try:
            query = str.format("UPDATE WebPage SET mcnt = {0} WHERE url = '{1}'", mcnt, url)
            cursor.execute(query)
            SqlCon.Commit()
        except:
            return False
        else:
            return True
        
    # 웹 페이지 주소로 일련번호 구하기
    @staticmethod
    def findWid(url):
        cursor = SqlCon.Cursor()
        query = str.format("SELECT wid FROM WebPage WHERE url = '{0}'", url)
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            return row[0]
        return 0
    
    # 수집한 전체 문서 개수 구하기
    @staticmethod
    def TotalDocumentCount():
        cursor = SqlCon.Cursor()
        query = "SELECT COUNT(*) FROM WebPage"
        cursor.execute(query)
        row = cursor.fetchone()
        return row[0]