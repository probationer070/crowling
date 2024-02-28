from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def search_with_selenium_chrome(search_query):
    # 크롬 드라이버 경로 설정 (다운로드 받은 드라이버의 경로로 수정)
    # chrome_driver_path = 'A:\crowling\chromedriver.exe'

    # 크롬 브라우저 열기
    driver = webdriver.Chrome()
    
    try:
        # 구글 홈페이지 열기
        driver.get("https://www.google.com/")
        
        # CSS 선택자를 사용하여 검색어 입력
        search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')
        search_box.send_keys(search_query)
        
        # Enter 키 눌러 검색 실행
        search_box.send_keys(Keys.RETURN)
        
        # 잠시 대기 (검색 결과 확인을 위해)
        time.sleep(5)
        
    finally:
        # 브라우저 닫기
        driver.quit()

if __name__ == "__main__":
    search_query = input("검색할 단어를 입력하세요: ")
    search_with_selenium_chrome(search_query)
