import pymysql
class SqlCon:
    conn = pymysql.connect(
        host="localhost", 
        port=3306, 
        user="root", 
        password="0000", 
        database="webscraping"
    )

    @staticmethod
    def Cursor():
        return SqlCon.conn.cursor()
    @staticmethod
    def Close():
        SqlCon.conn.close()
    @staticmethod
    def Commit():
        SqlCon.conn.commit()


