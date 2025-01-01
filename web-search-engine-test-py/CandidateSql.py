from SqlCon import SqlCon
from WebPageSql import WebPageSql

class CandidateSql:
    # 수집 후보 추가
    @staticmethod
    def AddCandidate(url, depth):
        cursor = SqlCon.Cursor()
        if WebPageSql.findWid(url) != 0:
            return False
        query = str.format("INSERT INTO candidate (url, depth) VALUES ('{0}', {1})", url, depth)
        try:
            cursor.execute(query)
            SqlCon.Commit()
            return True
        except:
            return False   

    # 수집 후보 웹 페이지 주소 가져오기
    @staticmethod
    def GetCandidateId():
        cursor = SqlCon.Cursor()
        query = str.format("SELECT MIN(id) FROM candidate")
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return 0
    
    # 수집 후보 삭제
    @staticmethod
    def DeleteCandidate(id):
        cursor = SqlCon.Cursor()
        query = str.format("DELETE FROM candidate WHERE id = {0}", id)
        cursor.execute(query)
        SqlCon.Commit()
    
    # 수집 후보 웹 페이지 구하기(수집 후보 삭제 포함)
    @staticmethod
    def GetCandidate():
        id = CandidateSql.GetCandidateId()
        print("id:",id)         # id: 출력 ------------------------
        if id == 0 or id == None:
            return "", -1
        cursor = SqlCon.Cursor()
        query = str.format("SELECT url, depth FROM candidate WHERE id = {0}", id)
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            CandidateSql.DeleteCandidate(id)
            return row[0], row[1]
        else:
            return "", -1