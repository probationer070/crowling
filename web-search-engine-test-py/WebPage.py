from EHhelper import EHhelper
class WebPage:
    def __init__(self, url, title, description, text):
        self.url = url  # 웹 페이지의 URL
        self.title = EHhelper.EmitTagAndSpecialCh(title)    # 웹 페이지의 제목
        self.description = EHhelper.EmitTagAndSpecialCh(description)    # 웹 페이지의 설명
        self.text = text   # 웹 페이지의 본문
        self.mcnt = 0  # 웹 페이지 내의 전체 단어 수

    # Webpage 개체를 만드는 정적 메서드
    @staticmethod
    def MakeWebPage(url, cpage):
        try:
            title = cpage.title.text
            atags = cpage.find_all('a')
            links = WebPage.ExtractionUrl(atags)
        except:
            return None
        else:
            return WebPage(url, title, cpage.text, links)

    # 웹 페이지의 URL을 추출하는 정적 메서드
    def ExtractionUrls(atags):
        links = list()
        for atag in atags:
            if atag.has_attr('href') == False:
                try:
                    link = atag['href']
                except:
                    continue
                else:
                    link = WebPage.ExtractionUrl(link)
                    if str.startswith(link, 'http') or str.startswith(link, 'https'):
                        links.append(link)
        return links

    # URL에서 '#'과 '?'를 제거하는 정적 메서드
    @staticmethod
    def ExtractionUrl(url):
        index = url.find('#')
        if (index != -1):
            url = url[:index] + url[index+1:] # '#'을 제거
        index = url.find('?')
        if (index != -1):
            url = url[:index] + url[index+1:] # '?'을 제거
        return url

