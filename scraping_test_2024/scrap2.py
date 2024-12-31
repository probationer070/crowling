from selenium import webdriver
from selenium.webdriver.common.by import By

import time
# import json5
# import keyboard

def scrape_top_sites(search_query, num_results=5):
    # 크롬 브라우저 열기
    driver = webdriver.Chrome()
    
    
    try:
        # 네이버 메인 페이지 열기 (예시로 네이버 사용)
        driver.get("https://www.google.com/")

        # 검색어 입력
        search_box = driver.find_element(By.CSS_SELECTOR, 'textarea[name="q"]')
        search_box.send_keys(search_query+"news")
        search_box.submit()
        
        search_result_url = driver.current_url
        print(f"검색 결과 페이지 URL: {search_result_url}")
        
        
        
        
        # 검색 결과 스크랩
        sites = driver.find_elements(By.XPATH, '//*[@id="rcnt"]')[:num_results]
        
        # if len(sites) <= num_results:
        #     for i in range(num_results - len(sites)):
        #         sites.append(driver.find_elements(By.CSS_SELECTOR, f'#rso > div:nth-child(3) > div:nth-child({i})')[0])

        # 페이지 최상단 검색 결과
        site_name = sites[0].find_element(By.CSS_SELECTOR, '#rso > div > div > div:nth-child(2) > div > div > a > div > div.SoAPf > div.MgUUmf.NUnG9d').text # span.VuuXrf
        site_url = sites[0].find_element(By.CSS_SELECTOR, '#rso > div > div > div:nth-child(7) > div > div > a > div > div.SoAPf > div.OSrXXb.rbYSKb.LfVVr').text # cite.qLRx3b.tjvcx.GvPZzd.cHaqb
        site_topic = sites[0].find_element(By.CSS_SELECTOR, '#rso > div > div > div:nth-child(2) > div > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.MBeuO.nDgy9d').text # h3.LC20lb.MBeuO.DKV0Md
        site_info = sites[0].find_element(By.CSS_SELECTOR, '#rso > div > div > div.SoaBEf.pvFOzb > div > div > a > div > div.SoAPf > div.GI74Re.nDgy9d').text # div.VwiC3b.yXK7lf.lVm3ye.r025kc.hJNv6b.Hdw6tb
            
            
            
        
        print(f"[ Site {1} ]")
        print(f"Name: {site_name}")
        print(f"URL: {site_url}")
        print(f"Topic: {site_topic}")
        print(f"Info: {site_info}")
    
            
        
        print("Press 'q' to close the browser.")    # q 입력 시 창 닫기
        keyboard.wait("q")

    finally:
        # 브라우저 닫기
        driver.quit()

if __name__ == "__main__":
    search_query = input("검색할 단어를 입력하세요: ")
    num_results = int(input("검색 결과에서 출력할 사이트 개수를 입력하세요: "))
    scrape_top_sites(search_query, num_results)


#---------------------------------------------------------------
