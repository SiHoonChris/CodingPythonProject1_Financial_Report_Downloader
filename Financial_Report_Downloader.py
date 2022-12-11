from bs4 import BeautifulSoup
headers="Mozilla/5.0" # user-agent 전체 안써도 문제 없음
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent="+headers)
import time
import datetime


# ---------- 조회 기간 입력 / SearchDate() ---------- #
From_date=datetime.date.today
To_date=datetime.date.today

def SearchDate():
    class Date_Sequence_Error(Exception):
        def __init__(self, msg):
            self.msg=msg
        def __str__(self):
            return self.msg

    while True:
        try:
            example="<입력 예시>\n\n(시작) 연 : 2021\n(시작) 월 : 12\n(시작) 일 : 20\n(종료) 연 : 2022\n(종료) 월 : 3\n(종료) 일 : 5\n"
            print(example+"\n----------------------")

            print("<조회 기간 입력>\n")
            from_year=input("(시작) 연 : ")
            from_month=input("(시작) 월 : ")
            from_day=input("(시작) 일 : ")
            to_year=input("(종료) 연 : ")
            to_month=input("(종료) 월 : ")
            to_day=input("(종료) 일 : ")
            Today=datetime.date.today()
            global From_date
            From_date=datetime.date(int(from_year),int(from_month),int(from_day))
            global To_date
            To_date=datetime.date(int(to_year),int(to_month),int(to_day))

            if str(To_date) < str(From_date) :
                raise Date_Sequence_Error("*** '시작 날짜'가 '종료 날짜' 보다 늦음 ***\n")
            if str(Today) < str(From_date):
                raise Date_Sequence_Error("*** '시작 날짜'가 '오늘' 이후 임 ***\n")
            if str(Today) < str(To_date):
                raise Date_Sequence_Error("*** '종료 날짜'가 '오늘' 이후 임 ***\n")

            print("\n----------------------")

            break
        except ValueError:
            print("*** 입력 내용 다시 확인! - 문자나 기호 X / <입력 예시> 참고 ***")
        except Date_Sequence_Error as err:
            print(err)
# ---------- 조회 기간 입력 / SearchDate() ---------- #


# ---------- 미국 주식 공시자료 다운로드 / US_Report() ---------- #
def US_Report(*CIKs):

    browser=webdriver.Chrome(options=options)
    CNTs=0

    print("[해외 : 미국]")
    print(f"START ( 종목 : {len(CIKs)} )")
    print("-"*100)

    for CIK in CIKs:
        url = "https://www.sec.gov/edgar/browse/?CIK={}&owner=exclude".format(CIK)
        browser.get(url)
        time.sleep(2)
        browser.find_element(By.XPATH, "//*[@id='btnViewAllFilings']").click()
        time.sleep(2)

        soup = BeautifulSoup(browser.page_source, "lxml")
        name=soup.find("span", attrs={"id":"name"})
        number_of_lists=soup.find("tbody").find_all("tr")

        CNT=0
        for i in range(0, len(number_of_lists)):
            filing_dates=soup.find("tbody").find_all("td", attrs={"class":"sorting_1"})[i].get_text()
            if str(From_date) <= filing_dates <= str(To_date):
                CNT+=1
        print("[{0}]({1})".format(name.get_text(), CNT))
        CNTs += CNT

        idx=0
        for i in range(0, len(number_of_lists)):
            form_types=soup.find("tbody").find_all("td", attrs={"class":"dtr-control"})[i].get_text()
            form_descriptions=soup.find("tbody").find_all("a", attrs={"class":"document-link"})[i].get_text().replace("Open document", "")
            links=soup.find("tbody").find_all("a", attrs={"class":"document-link"})[i]["href"]
            filing_dates=soup.find("tbody").find_all("td", attrs={"class":"sorting_1"})[i].get_text()
            if str(From_date) <= filing_dates <= str(To_date):
                idx += 1
                print("   {0}. [{1}] ".format(idx, form_types), form_descriptions, " ({0})".format(filing_dates))
                if idx < 10:
                    print("      https://www.sec.gov"+links)
                else:
                    print("       https://www.sec.gov"+links)
            else:
                continue
        
        print("-"*100)

    print(f"END ( 종목 : {len(CIKs)}, 내용 : {CNTs} )\n")
    browser.quit()
# ---------- 미국 주식 공시자료 다운로드 / US_Report() ---------- #


# ---------- 한국 주식 공시자료 다운로드 / KR_Report() ---------- #
def KR_Report(*CODEs):

    browser=webdriver.Chrome(options=options)
    if_num=0
    else_num=0

    print("[국내 : 한국]")
    print(f"START ( 종목 : {len(CODEs)} )")
    print("-"*100)

    for CODE in CODEs:
        url="https://dart.fss.or.kr/"
        browser.get(url)
        time.sleep(2)
        browser.find_element(By.XPATH, "//*[@id='textCrpNm2']").send_keys(CODE)
        browser.find_element(By.XPATH, "//*[@id='searchForm2']/div[1]/div[3]/a").click()
        time.sleep(2)
        Start_date=str(From_date).replace("-", "")
        End_date=str(To_date).replace("-", "")
        browser.find_element(By.XPATH, "//*[@id='startDate']").clear()
        browser.find_element(By.XPATH, "//*[@id='startDate']").send_keys(Start_date)
        browser.find_element(By.XPATH, "//*[@id='endDate']").clear()
        browser.find_element(By.XPATH, "//*[@id='endDate']").send_keys(End_date)
        browser.find_element(By.XPATH, "//*[@id='maxResultsCb']/option[4]").click()
        browser.find_element(By.XPATH, "//*[@id='searchForm']/div[2]/div[2]/a[1]").click()
        time.sleep(2)

        soup = BeautifulSoup(browser.page_source, "lxml")
        name = soup.find("span", attrs={"class":"innerWrap"}).find("a").get_text().strip()
        pages=soup.find("div", attrs={"class":"pageSkip"}).find_all("li")

        if len(pages) <= 1:
            number_of_lists=soup.find("tbody").find_all("tr")
            print("[{0}]({1})".format(name, len(number_of_lists)))

            for idx, i in enumerate(range(0, len(number_of_lists)), start=1):
                file_name=soup.find("tbody").find_all("tr")[i].find_all("td", attrs={"class":"tL"})[1].find("a")
                file_names=file_name.get_text().strip()
                filing_dates=soup.find("tbody").find_all("tr")[i].find_all("td")[4].get_text()
                links=file_name["href"]
                print("   {0:<3} {1}  ({2})".format(str(idx)+".", file_names, filing_dates))
                if idx < 10:
                    print("      https://dart.fss.or.kr"+links)
                elif 10 <= idx < 100:
                    print("       https://dart.fss.or.kr"+links)
                else:
                    print("        https://dart.fss.or.kr"+links)

            if_num += len(number_of_lists)
            print("-"*100)

        else:
            browser.find_element(By.XPATH, f"//*[@id='psWrap']/div[2]/ul/li[{len(pages)}]/a").click()
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, "lxml")
            lists_on_lastpg=soup.find("tbody").find_all("tr")
            list_num=(len(pages)-1)*100+len(lists_on_lastpg)
            print("[{0}]({1})".format(name, list_num))

            for pg in range(1, len(pages)+1):
                browser.find_element(By.XPATH, f"//*[@id='psWrap']/div[2]/ul/li[{pg}]/a").click()
                
                time.sleep(2)
                soup = BeautifulSoup(browser.page_source, "lxml")

                number_of_lists=soup.find("tbody").find_all("tr")
                
                for idx, i in enumerate(range(0, len(number_of_lists)), start=1):
                    file_name=soup.find("tbody").find_all("tr")[i].find_all("td", attrs={"class":"tL"})[1].find("a")
                    file_names=file_name.get_text().strip()
                    filing_dates=soup.find("tbody").find_all("tr")[i].find_all("td")[4].get_text()
                    links=file_name["href"]

                    if pg <= 1:
                        print("   {0:<3} {1}  ({2})".format(str(idx)+".", file_names, filing_dates))
                        if idx < 10:
                            print("      https://dart.fss.or.kr"+links)
                        elif 10 <= idx < 100:
                            print("       https://dart.fss.or.kr"+links)
                        else:
                            print("        https://dart.fss.or.kr"+links)

                    else:
                        print("   {0:<3} {1}  ({2})".format(str((pg-1)*100+idx)+".", file_names, filing_dates))
                        print("        https://dart.fss.or.kr"+links)

            else_num += list_num
            print("-"*100)

    total_num = if_num + else_num
    print(f"----- END ( 종목 : {len(CODEs)}, 내용 : {total_num} ) -----\n")
    browser.quit()
# ---------- 한국 주식 공시자료 다운로드 / KR_Report() ---------- #


# ---------- 전체(한국, 미국) 자료 다운로드 / Report_Downloader() ---------- #
def Report_Downloader():
    SearchDate()
    start_time=time.time()
    US_Report("320193", "1652044")  # AAPL , GOOGL
    KR_Report("005930", "000660")   # 삼성전자 , SK하이닉스
    end_time=time.time()
    time_spent = end_time - start_time
    print(f"({str(round((time_spent), 4))} sec.)")
# ---------- 전체(한국, 미국) 자료 다운로드 / Report_Downloader() ---------- #



# ---------- 전체(한국, 미국) 자료 다운로드 실행 ---------- #
if __name__=="__main__":
    Report_Downloader()
# ---------- 전체(한국, 미국) 자료 다운로드 실행 ---------- #