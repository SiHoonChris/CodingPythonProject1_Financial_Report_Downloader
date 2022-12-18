# CodingPythonProject1 - Financial Report Downloader (22.07.16 ~ 22.07.25)  

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><br>  

1. 구글(알파벳), 애플, 삼성전자, SK하이닉스에 대한 자료 가져올 예정  
![FinancialReportDownloader1](https://user-images.githubusercontent.com/109140000/208286069-6862aab6-b7c8-4c16-9274-59b75d40526e.png)  
2. 조회기간 입력 (2022년 상반기)  
![FinancialReportDownloader2](https://user-images.githubusercontent.com/109140000/208286072-dc72a57c-b123-4209-bab1-ed8f7eda3c32.png)  
3. 자료 출력  
![FinancialReportDownloader3](https://user-images.githubusercontent.com/109140000/208286079-c5e25b13-96c1-4f1b-8313-36fcdbe7bc5f.png)  
4. 정상적으로 정보가 가져와졌음을 알 수 있음
![FinancialReportDownloader4](https://user-images.githubusercontent.com/109140000/208286083-9e18abb2-263a-4e78-ba4b-73219a8e2936.png)  
5. 소요 시간 (60.0521초)
![FinancialReportDownloader5](https://user-images.githubusercontent.com/109140000/208286086-01ace92a-de57-4178-b7c6-8e5c6f6f06db.png)  


<div align="right">최초 제작 : 22.07.16 ~ 22.07.25 , 개선 및 보완 : 22.11.29 ~ 22.12.17</div>  
<br><br>  

### 목차  
&nbsp; &nbsp; 개발 동기 - 설계 - 후기 - 개선 사항 - 참고  

<hr>  

## 개발 동기  
- 처음 이 프로그램을 계획했을 때가 한참 Youtube로 Python을 독학하고 있을 때였다. 그 때 당시 '웹 스크래핑'에 대한 강좌 * 를 봤었고, 내가 그 동안 학습한 내용들을 통해 유용한 프로그램을 하나 만들어 보고 싶었다. 어떤 프로그램을 만들어볼지 고민하던 중, 내가 평소 관심 있던 주식투자에 이 내용들을 활용해보자는 생각이 들었다. 그래서 특정 종목에 대한 재무제표와 기타 여러 보고서들을 손쉽게 확인할 수 있도록 도와주는, 이 프로그램을 만들게 됐다.  
&nbsp;* 파이썬 코딩 무료 강의 (활용편3) - 웹 크롤링? 웹 스크래핑! 제가 가진 모든 비법을 알려드리겠습니다. [나도코딩] ( https://www.youtube.com/watch?v=yQ20jZwDjTE )  
- 이후에 내가 작성했던 코드들을 다시 보는데, 개선/수정하면 좋을 것 같은 내용들, 현재 프로그램에서 더 추가하면 좋은 것 같은 기능들이 떠올랐고, 그래서 다시 이 프로그램에 대한 작업을 진행하게 됐다.  


## 설계  
1) Selenium 활용  
&nbsp; - 필요한 정보를 가져올 웹 페이지로 이동  
&nbsp; - 동적 웹 페이지에서 웹 스크래핑을 하기 위한 기초 작업 실행  
2) BeautifulSoup4 활용  
&nbsp; - 해당 웹 페이지 내의 HTML Element들을 통해 필요한 정보 찾기  
3) 위 과정의 반복  


## 후기  
1) 이 프로그램을 만들기로 처음 생각했을 때는, 그저 Youtube에서 Python 강의 몇 개 본게 전부인 상태였다. 그래서 웹이나 HTML 등에 대한 이해가 전혀 없던 상태로 코딩을 했기에 어찌보면 굉장히 무모한 방식으로 작업을 진행했던 것이 기억이 난다. 하지만 최근에 이 프로그램을 다시 다루면서는, (Selenium의 버전이 달라져서 코드에 수정이 어느 정도 필요하기는 했지만, 그것만 조금 손 봐주니 다시 잘 돌아가는 것을 보았을 때) 그 때 당시에 어찌저찌 괜찮게 만들어낸 것 같다는 생각이 들었다.  
2) 학원에 다니며 프로그래밍을 배우고 그 때 보다는 프로그래밍에 대한 시야가 넓어진 상태에서 이 프로그램을 다시 작업하면서, 이 프로그램은 Python보다는 병렬처리에 유리한 Java를 활용하는 것이 훨씬 더 좋을 것 같다는 생각이 들었다. Java로 구현한다면 실행 처리 속도가 더 빨라질 것 같다는 판단이 들어서이다. 거기에 더불어 JSP 등을 활용해 웹 상에서 바로 내용들을 보여지게 할 수 있다면 더 유용한 프로그램이 만들어질 것 같다.  
3) 올해 9월부터 학원에 다니면서 줄곧 Java만 해왔더니 이번에 Python을 다루면서 낯설었다. 그 동안 쌓아 왔던 것들이 증발된 것 같아 아쉽기도 했지만, 나 스스로 여러 언어를 활용해 프로그래밍을 진행해 봤다는 사실에, 그 경험에 가치를 두고 싶다.


## 개선 사항  
1) 웹 드라이버의 버전이 웹 브라우저의 버전과 맞지 않을 시 프로그램이 실행되지 않음<br>(2022.12.17 부 개선 완료)    
&nbsp; - 웹 드라이버의 버전 문제로 출력이 되지 않을 때는 try/except(예외 처리) 활용하여 예외 처리  
&nbsp; - except문에서 크롬 웹 드라이버 버전 확인에 대한 안내문 출력  
&nbsp; - 예외 처리 시, 자동으로 페이지 띄우기 : 크롬 웹 브라우저 버전 확인 ( chrome://version/ )  
&nbsp; - 예외 처리 시, 자동으로 페이지 띄우기 : 크롬 웹 드라이버 다운로드 ( https://chromedriver.chromium.org/downloads )  
2) pyQT 또는 HTML 등을 활용하여 출력 결과를 시각화  
&nbsp; - VS Code 내의 터미널 창을 활용하여 내용을 출력하는 것은 가독성, 접근/편의성 등에 있어 한계가 있다고 판단  
&nbsp; - pyQT 또는 HTML 등을 활용하여 터미널 외부에서 내용들을 출력하면 현재보다 더 편리해질 것이라 생각함  


## 참고
- 11-29-2022부, 별도 관리  
- 현재 Repository에서의 기록  
11-29-2022 / Selenium 버전 업그레이드에 따른 코드 수정  
12-11-2022 / 코드 정리, 출력문의 가독성 높임  
12-17-2022 / 종목별 코드/CIK 종합( Code.txt ), 웹 드라이버 버전 차이에서 발생할 수 있는 예외 처리  
- 이전 Repository : Mercenary_Chris ( https://github.com/SiHoonChris/Mercenary_Chris )  
- Mercenary_Chris 내의 Commit 기록들  
(파일명 : REPORT_DOWNLOADER.py)  
(07-16-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/35d741373e9fbb93391b260e83368f2f78c8150d  
(07-17-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/5af4815ec0f3d39b93cb978378c77925852b4339  
(07-18-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/a67862bfc0444427489de4f2ea93713e6ae850c7  
(07-19-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/e7b74ff392bac488d2ee43ef4b63cf44d2712394  
(07-20-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/bbe475d09278365de36e98733a6c2b7c53923ef3  
(07-21-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/cdea1cb1cd565c21a6f9ece449f431512dfa997d  
(07-22-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/4b538cc4a519af8a359707a0359c2c03c02988c8  
(07-23-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/cc16fd856b5d70241f8df33b5830a7572f405123  
(07-24-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/e81383d4416497a43c43d13decb1c3b448fe808e  
(07-25-2022) https://github.com/SiHoonChris/Mercenary_Chris/commit/17e1ede19332974a96c13fd0245d5a4b03adf64d