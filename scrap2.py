from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import json5
import keyboard

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
    
            
         #  
         
        # #_GkTsZcLEG5OMvr0Pl5u98AI_24 > div.acCJ4b > div > div > div:nth-child(1) > div > div > div > a > div > div.z7T1i > div.MgUUmf.NUnG9d : 뉴스 제공자
         
         
        #_GkTsZcLEG5OMvr0Pl5u98AI_24 > div.acCJ4b > div > div > div:nth-child(1) > div > div > div > a > div > div.z7T1i > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 뉴스 내용  
        
        
        #rso > div > div > div:nth-child(1) > div > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.MBeuO.nDgy9d
        
        
        
        
        
        
        #rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(4) > div.aUSklf > div > div:nth-child(1) > div > a > div > div.SoAPf > div.MgUUmf.NUnG9d : 작은 뉴스 제공사 2
        
        #rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(4) > div.aUSklf > div > div:nth-child(3) > div > a > div > div.SoAPf > div.MgUUmf.NUnG9d : 작은 뉴스 제공사 2
        
        #rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(3) > div.aUSklf > div > div:nth-child(3) > div > a > div > div > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 작은 뉴스 제목 2
        
        #rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(3) > div.aUSklf > div > div:nth-child(1) > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 작은 뉴스 제목 2
        
        
        #-jHsZZCfA6Cfvr0PzsCpoAU__17 > div > a > div > div.OKCt1 > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 작은 뉴스 제목
        
        #rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(2) > div.aUSklf > div > div:nth-child(3) > div.vu9Nlb.HdAYZc > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 작은 뉴스 제목
        
        # //*[@id="rso"]/div[1]/div/g-section-with-header/div[2]/div[2]/div/div[3]/div[1]/div/a/div/div[2]/div[2] : 작은 뉴스 제목
        
        #rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(2) > div.aUSklf > div > div:nth-child(3) > div.vu9Nlb.HdAYZc > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 작은 뉴스 제목
        
        #-jHsZZCfA6Cfvr0PzsCpoAU__17 > div > a > div > div.OKCt1 > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 작은 뉴스 제목
        
        #rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(2) > div.aUSklf > div > div:nth-child(3) > div:nth-child(1) > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 작은 뉴스 제목
        
        #rso > div:nth-child(1) > div > g-section-with-header > div:nth-child(2) > div.aUSklf > div > div:nth-child(3) > div:nth-child(1) > div > a > div > div.SoAPf > div.MgUUmf.NUnG9d : 작은 뉴스 제공사
        
        #GTLsZYK7ObL71e8PmrWkyAM__17 > div > a > div > div.OKCt1 > div.MgUUmf.NUnG9d : 작은 뉴스 제공사
        
        #_IzHsZcqcD_GP2roPzfaS4AU_24 > div.acCJ4b > div > div > div:nth-child(1) > div > div > div > a > div > div.z7T1i > div.MgUUmf.NUnG9d : 작은 뉴스 제공사
        
        #_IzHsZcqcD_GP2roPzfaS4AU_24 > div.acCJ4b > div > div > div:nth-child(1) > div > div > div > a > div > div.z7T1i > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 뉴스 제목
        
        #rso > div > div > div:nth-child(1) > div > div > a > div > div.SoAPf > div.OSrXXb.rbYSKb.LfVVr : 업로드 시간
        
        #crypto-updatable_2 > div.card-section.PZPZlf > div:nth-child(2) > span.pclqee : 가격
        
        #crypto-updatable_2 > div.card-section.PZPZlf > span : 값 변화량(증감)
        
        #fw-_EDDsZaH3EeGP2roPgO6yoAQ_39 > div > div.VADlJf > div.uch-svg > div.uch-path > svg : 주식이나 코인 그래프 사진
        
        #rso > div:nth-child(2) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span : 사이트 URL 최상위
        
        #rso > div:nth-child(3) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > div > cite : 사이트 URL 세부사항

        #rso > div:nth-child(2) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > div > cite : 사이트 URL 세부사항
        
        #rso > div:nth-child(3) > div > div > div:nth-child(2) > div > span:nth-child(2) : 사이트 정보 일부
        
        #rso > div:nth-child(3) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3 : 사이트 내용 제목
        
        #rso > div:nth-child(2) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3 : 사이트 내용 제목
        
        
            # 이후에 검색된 결과 (첫번째 검색 결과 제외한)
        
        #rso > div:nth-child(3) > div:nth-child(1) > div > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > div > cite
        
        
        
        


        
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
