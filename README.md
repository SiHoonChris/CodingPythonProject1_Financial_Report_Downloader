# CodingPythonProject1 - Financial Report Downloader (22.07.16 ~ 22.07.25)

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><br>

(사진)  

### 목차  
개발 동기 - 설계 - 후기 - 개선 사항 - 참고

## 개발 동기
투자를 위한 유용한 툴 개발  

## 설계
(사진)  
링크 lxml로 parse - selenium으로 페이지 이동/검색 - bs4로 태그의 content 다운로드  

## 후기
아무래도 html에 대한 개념이 부족한 상태에서 하다보니 너무 막연했다. html에 대한 개념과 이해가 제대로 잡히지 않은 상태로 프로그램을 만들다보니
많이 답답하고 힘들었던 기억이 난다.  

## 개선 사항
1) 크롬 드라이버의 버전이 웹브라우저의 버전과 맞지 않을 시 프로그램이 실행되지 않음 
&nbsp; - 크롬 드라이버 문제로 출력 안될 때는 try/except(예외 처리) 써서 예외 처리
&nbsp; - except문에서 '크롬 드라이버 버전 확인 안내' 출력
&nbsp; - 예외처리 시, 자동으로 페이지 띄우기 ; 구글 크롬 버전 확인 페이지(chrome://version/)
크롬 웹드라이버 다운로드 페이지(https://chromedriver.chromium.org/downloads)
2) pyQT 활용하여 출력 결과 시각화
&nbsp; - 터미널이나 dos창(pip exe파일)에서만 글씨만 띄우는게 아니라 보기 쉽게 만들기
&nbsp; - 링크도 하이퍼링크로 연결
&nbsp; - html로 웹페이지 만드는 방법도 고려

## 참고
- xx-xx-2022부, 별도 관리
- 현재 Repository에서의 기록  
레포 개설  
깃허브 업로드  
- 이전 Repository : ~
- 내의 Commit 기록들  
(xx-xx-2022) 주소1  
(xx-xx-2022) 주소1  