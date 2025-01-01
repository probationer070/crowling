class EHhelper:
    @staticmethod
    def EmitTagAndSpecialCh(str):
        src = EHhelper.RemoveTag(str)
        src = EHhelper.RemoveSymbol(str)
        src = EHhelper.RemoveHtmlSpecialCh(str)
        return str

    # FindTag - 태그 찾기, 태그의 위치를 찾아서 반환
    @staticmethod
    def FindTag(src):
        s = src.index('<')
        e = src.index('>')
        return s,e
    
    # RemoveTag - 태그 제거
    @staticmethod
    def RemoveTag(src):
        try:
            while True:
                s,e = EHhelper.FindTag(src)
                if s<e:
                    src = src[:s]+src[e+1:] #태그를 제거하는 구문
                else:#'>'가 '<'보다 앞에 있을 때
                    src = src[:e]+src[e+1:]#'>'만 제거하는 구문
        except:# 더 이상 태그가 없음
            return src
        
    # RemoveSpecial - 특수 문자 제거, 알파벳과 공백을 제외한 나머지 문자는 특수문자로 취급해 제거하고 공백으로 대체
    @staticmethod
    def RemoveSymbol(src):
        #특수문자 리스트
        special = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|','\\',':',';','"',"'",'<','>',',','.','?','/']
        for ch in special:
            src = src.replace(ch,' ')
        return src
    
    # RemoveHtml - HTML 특수 문자 제거, &로 시작해서 ;로 끝나는 문자열 제거
    @staticmethod
    def FindHtmlSpecialCh(src):
        s = src.index('&')
        e = src.index(';',s)
        return s,e

    @staticmethod
    def RemoveHtmlSpecialCh(src):
        try:
            while True:
                s,e = EHhelper.FindHtmlSpecialCh(src)
                if s<e:
                    src = src[:s]+src[e+1:]
                else:
                    src = src[:e]+src[e+1:]
        except:
            return src
        
    # TransformHangul - SQL에 한글 문자열을 파이썬 한글 문자열로 변환
    @staticmethod
    def SQLstrtoStrKo(src):
        try:
            src = src.encode('ISO-8859-1')
            src = src.decode('euc-kr')
        except:
            return ""
        else:
            return src
