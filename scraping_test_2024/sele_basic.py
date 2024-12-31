from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def crawl_google_news(search_query, num_results=5):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # 크롬 브라우저 열기
    driver = webdriver.Chrome()

    try:
        # 구글 검색 페이지 열기
        driver.get("https://www.google.com/")

        # 검색어 입력
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(search_query + " 뉴스")
        search_box.send_keys(Keys.RETURN)

        # 검색 결과 페이지 URL 출력
        search_result_url = driver.current_url
        print(f"검색 결과 페이지 URL: {search_result_url}")
        search_result_url = search_result_url + "&tbm=nws" # 추후 변경 예정

        # 검색 결과 스크랩
        # results = WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By.XPATH, '//*[@id="rso"]'))
        # )
        
        results = driver.find_elements(By.XPATH, '//*[@id="rso"]')

        for index, result in enumerate(results[:num_results], start=1):
            print(f"New total n : {len(results)}")
            if result == None:
                result = "_Blank_"
                # 사이트 제목
            title = result.find_element(By.CSS_SELECTOR, f'#rso > div:nth-child({index}) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span').text

            # # 사이트 출처
            source = result.find_element(By.CSS_SELECTOR, f'#rso > div:nth-child({index}) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > div > cite').text

            # # 사이트 내용 (텍스트만 추출)
            content = result.find_element(By.CSS_SELECTOR, f'#rso > div:nth-child({index}) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3').text

            # # 업로드된 시간
            upload_time = result.find_element(By.CSS_SELECTOR, f'#rso > div:nth-child({index}) > div > div > div:nth-child(2) > div > span').text

            # 결과 출력
            print(f"\n[ Site {index} ]")
            print(f"Title: {title}")
            print(f"Source: {source}")
            print(f"Content: {content}")
            print(f"Upload Time: {upload_time}")
            



#rso > div:nth-child(1) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span : 사이트 이름
#rso > div:nth-child(2) > div > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span

#rso > div:nth-child(1) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > div > cite : 사이트 URL

#rso > div:nth-child(2) > div > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > div > cite
#rso > div:nth-child(5) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > div > cite
#rso > div:nth-child(6) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > div > cite

#rso > div:nth-child(1) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3 :  뉴스 제목

#rso > div:nth-child(1) > div > div > div:nth-child(2) > div > span : 뉴스 정보 일부


#rso > div > div > div:nth-child(1) > div > div > a > div > div.SoAPf > div.MgUUmf.NUnG9d > span
#rso > div > div > div:nth-child(2) > div > div > a > div > div.SoAPf > div.MgUUmf.NUnG9d > span

#rso > div:nth-child(5) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span
#rso > div:nth-child(5) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span

#rso > div > div > div:nth-child(1) > div > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.MBeuO.nDgy9d
#rso > div > div > div:nth-child(2) > div > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.MBeuO.nDgy9d

#rso > div > div > div:nth-child(2) > div > div > a > div > div.SoAPf > div.GI74Re.nDgy9d
#rso > div > div > div:nth-child(1) > div > div > a > div > div.SoAPf > div.GI74Re.nDgy9d

#rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(7) > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d
#rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(5) > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d
#rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(3) > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d

#rso > div:nth-child(4) > div > div > div.e4xoPb > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div:nth-child(1) > div > div > a:nth-child(2) > div > div.ZxS7Db > div > span
#rso > div:nth-child(4) > div > div > div.e4xoPb > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div > div > a:nth-child(2) > div > div.ZxS7Db > div > span

#rso > div:nth-child(5) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3
#rso > div:nth-child(6) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3
#rso > div:nth-child(7) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3

#rso > div:nth-child(2) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span            
#rso > div:nth-child(3) > div > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span
#rso > div:nth-child(5) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span

#rso > div:nth-child(1) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3
#rso > div:nth-child(2) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3
#rso > div:nth-child(3) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3

#rso > div:nth-child(5) > div > g-section-with-header > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(1) > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d
#rso > div:nth-child(5) > div > g-section-with-header > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(1) > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d
#rso > div:nth-child(5) > div > g-section-with-header > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(3) > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d
#rso > div:nth-child(5) > div > g-section-with-header > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d



    finally:
        # WebDriver 종료
        driver.quit()

# 크롤링 실행
user_input = input("검색어를 입력하세요: ")
crawl_google_news(user_input)
