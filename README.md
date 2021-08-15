## 🦄 Synopsis
- AutoWatch의 main server를 django framework를 이용해 구현 했습니다.
- 배포된 URL -> [https://118.67.131.138:30000/](https://118.67.131.138:30000/)

#### 소스 코드 실행 방법
```git bash
git clone https://github.com/openInfra-project/AutoWatch-Mange-Server.git
// 가상 환경 실행
pip install requirements.txt
py manage.py runserver
```
- 실행 전 가상환경을 실행 시켜야 합니다.

## 🎨 Preview
https://user-images.githubusercontent.com/67450413/129485577-2b1faf37-6c6e-4568-bbb1-4f6f8ad8dc71.mp4

## 💻Django
![django 설명](https://user-images.githubusercontent.com/67450413/129481501-0f8325d6-aad0-4a67-b9be-0d782f23c278.PNG)


## 🛠 **Development Stack**
- <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
- <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
- <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
- <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
- <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/>
- <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white"/>
- ajax
- Retrofit

## 🖋Features
1. Home 화면에서 Service 간단 소개
2. 회원 가입 및 로그인/ 로그아웃
    - 로그인과 동시에 `user_session` 저장
    - 중복 회원 가입 방지
    - 회원 가입시 비밀번호 재확인
3.  사용자 My Page 모달화면
    - 사용자 이미지 변경 가능
    - 기본 default 이미지 제공
4. Room을 EXAM/STUDY 2가지 모드로 생성 및 입장
    - Room 입장과 동시에 `Room_session` 저장
    - 앱 차단 미 실행 시 다음 단계로 진행 불가
    - EXAM 모드 시, 시험 명단 누락 방지
    - EXAM 모드 시, 시험 명단 속 사진과 사용자 얼굴 인식
    - Room 퇴장 후 `Room_session` 삭제
    - STUDY 모드 Room 퇴장 후 학습시간, App 접근도, 자리이탈 정도를 바탕으로

        집중도 통계 그래프 작성

    - 집중도 통계 그래프에서 각 feature의 점수에 따라 집중도 level 부여
    - 집중도 통계 그래프에서 각 level에 따라 해당 Room에서의 등수 지정
5. 생성 했던 Room을 기준으로 사용자에게 Room List 제공
6. 생성 했던 통계 자료를 기준으로 사용자에게 집중도 통계 자료 List 제공

## 🐹 API & Library
1. Luxand API - 얼굴 인식
2. SSL - https 통신
3. Animated - 애니메이션
4. Bootstrap - UI/UX
5. Lotties - loading animation

## 🌐 Rest API
`POST` /  → 사용자 아이디 중복 체크 및 비밀번호 재입력 확인 요청

`POST` / login → 사용자 아이디 및 비밀번호 요청

`GET` / logout → 로그아웃

`POST` / makeroom → STUDY/EXAM 모드에 따라 방생성

`POST` / makeroom/success → 방 생성 성공 후 방 정보 나열

`POST` / enteroom/exam1 → EXAM 모드 앱 차단 여부 요청

`POST` / enteroom/exam2 → EXAM 모드 얼굴 인식 확인 요청

`POST` / enteroom/exam3 → EXAM 모드 WebRTC 입장 가능 여부 요청 

`POST` / enteroom/study1 → STUDY 모드 앱 차단 여부 요청

`POST` / enteroom/study2 → STUDY 모드 WebRTC 입장 가능 여부 요청

`GET` / roomout/<int:time>/<str:mode> → mode가 STUDY 일때 해당 사용자의 Analytics에 time이 저장됨

`POST` / roomout/<int:time>/<str:mode> → App 접근 차단을 해제 하였는지 요청 & mode가 STUDY 일때 저장돤 time, app, person 변수를 바탕으로 level, rate를 측정하고 Analytics 모델에 저장 

`GET` / roomout/study → session에서 사용자 정보를 가져와 Analytics 모델의 가장 마지막 row를 DB에서 가져와서 집중도 그래프를 그림 

`POST` / roomout/exam → 시험이 성공적으로 종료 됐는지 요청

`GET` / list/room → Room DB에서 사용자 이름으로 만들어진 Room을nQuerySet으로 반환후 list 나타냄

`GET` / list/analytics → Analytics DB에서 사용자 이름으로 만들어진 Analytics를 QuerySet으로 반환후 list 나타냄

`POST`/ list/analytics/<int:pk> → Analytics List에서 선택한 QuerySet 객체의 Primary Key 값과 같은 row를 DB에서 가져와 집중도 그래프를 그려줌

## 🙋‍♂️Role
@황한식  
- 전체 UI/UX
- Django 풀스텍

@김혜원 

- Exam 방 입장 시 엑셀 파일 속 사진과 사용자 얼굴 인식
- https 배포

@김유림 

- 안드로이드 통신코드 구현
## License
```
MIT License

Copyright (혜몽유식) [2021-08-15] [HanSik Hwang]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
