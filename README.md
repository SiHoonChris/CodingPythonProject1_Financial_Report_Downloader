# CodingPythonProject1 - Financial Report Downloader (22.07.16 ~ 22.07.25)

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><br>

(사진)  
<div align="right">최초 제작 : 22.07.16 ~ 22.07.25 , 개선 및 보완 : 22.11.29 ~ </div>  
<br><br>  

### 목차  
&nbsp; &nbsp; 개발 동기 - 설계 - 후기 - 개선 사항 - 참고

<hr>

## 개발 동기
유튜브에서 배운 내용 실습 (웹 스크래핑 : BeautifulSoup4, Selenium)  
투자를 위한 유용한 툴 개발  

## 설계
(사진)  
링크 lxml로 parse - selenium으로 페이지 이동/검색 - bs4로 태그의 content 다운로드  

## 후기
아무래도 html에 대한 개념이 부족한 상태에서 하다보니 너무 막연했다. html에 대한 개념과 이해가 제대로 잡히지 않은 상태로 프로그램을 만들다보니
많이 답답하고 힘들었던 기억이 난다.  
최근에 다시 수정/개선하면서 드는 생각인데, 이 프로그램은 파이썬보다는 자바가 더 유리할 것 같다.

## 개선 사항
1) 크롬 드라이버의 버전이 웹브라우저의 버전과 맞지 않을 시 프로그램이 실행되지 않음 
&nbsp; - 크롬 드라이버 문제로 출력 안될 때는 try/except(예외 처리) 써서 예외 처리
&nbsp; - except문에서 '크롬 드라이버 버전 확인 안내' 출력
&nbsp; - 예외처리 시, 자동으로 페이지 띄우기 ; 구글 크롬 버전 확인 페이지(chrome://version/)  
&nbsp; &nbsp; 크롬 웹드라이버 다운로드 페이지(https://chromedriver.chromium.org/downloads)
2) pyQT 활용하여 출력 결과 시각화
&nbsp; - 터미널이나 dos창(pip exe파일)에서만 글씨만 띄우는게 아니라 보기 쉽게 만들기
&nbsp; - 링크도 하이퍼링크로 연결
&nbsp; - html로 웹페이지 만드는 방법도 고려

## 참고
- 11-29-2022부, 별도 관리
- 현재 Repository에서의 기록  
11-29-2022 / Selenium 버전 업그레이드에 따른 코드 수정  
12-11-2022 / 코드 정리, 출력문의 가독성 높임  
- 이전 Repository : Mercenary_Chris (https://github.com/SiHoonChris/Mercenary_Chris)  
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