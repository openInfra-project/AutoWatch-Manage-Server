## ๐ฆ Synopsis
- AutoWatch์ main server๋ฅผ django framework๋ฅผ ์ด์ฉํด ๊ตฌํ ํ์ต๋๋ค.
- ๋ฐฐํฌ๋ URL -> [https://118.67.131.138:30000/](https://118.67.131.138:30000/)

#### ์์ค ์ฝ๋ ์คํ ๋ฐฉ๋ฒ
```git bash
git clone https://github.com/openInfra-project/AutoWatch-Mange-Server.git
// ๊ฐ์ ํ๊ฒฝ ์คํ
pip install requirements.txt
py manage.py runserver
```
- ์คํ ์  ๊ฐ์ํ๊ฒฝ์ ์คํ ์์ผ์ผ ํฉ๋๋ค.

## ๐จ Preview
https://user-images.githubusercontent.com/67450413/129485577-2b1faf37-6c6e-4568-bbb1-4f6f8ad8dc71.mp4

## ๐ปDjango
![django ์ค๋ช](https://user-images.githubusercontent.com/67450413/129481501-0f8325d6-aad0-4a67-b9be-0d782f23c278.PNG)


## ๐ ย **Development Stack**
- <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
- <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
- <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
- <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
- <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/>
- <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white"/>
- ajax
- Retrofit

## ๐Features
1. Home ํ๋ฉด์์ Service ๊ฐ๋จ ์๊ฐ
2. ํ์ ๊ฐ์ ๋ฐ ๋ก๊ทธ์ธ/ ๋ก๊ทธ์์
    - ๋ก๊ทธ์ธ๊ณผ ๋์์ `user_session` ์ ์ฅ
    - ์ค๋ณต ํ์ ๊ฐ์ ๋ฐฉ์ง
    - ํ์ ๊ฐ์์ ๋น๋ฐ๋ฒํธ ์ฌํ์ธ
3.  ์ฌ์ฉ์ My Page ๋ชจ๋ฌํ๋ฉด
    - ์ฌ์ฉ์ ์ด๋ฏธ์ง ๋ณ๊ฒฝ ๊ฐ๋ฅ
    - ๊ธฐ๋ณธ default ์ด๋ฏธ์ง ์ ๊ณต
4. Room์ EXAM/STUDY 2๊ฐ์ง ๋ชจ๋๋ก ์์ฑ ๋ฐ ์์ฅ
    - Room ์์ฅ๊ณผ ๋์์ `Room_session` ์ ์ฅ
    - ์ฑ ์ฐจ๋จ ๋ฏธ ์คํ ์ ๋ค์ ๋จ๊ณ๋ก ์งํ ๋ถ๊ฐ
    - EXAM ๋ชจ๋ ์, ์ํ ๋ช๋จ ๋๋ฝ ๋ฐฉ์ง
    - EXAM ๋ชจ๋ ์, ์ํ ๋ช๋จ ์ ์ฌ์ง๊ณผ ์ฌ์ฉ์ ์ผ๊ตด ์ธ์
    - Room ํด์ฅ ํ `Room_session` ์ญ์ 
    - STUDY ๋ชจ๋ Room ํด์ฅ ํ ํ์ต์๊ฐ, App ์ ๊ทผ๋, ์๋ฆฌ์ดํ ์ ๋๋ฅผ ๋ฐํ์ผ๋ก

        ์ง์ค๋ ํต๊ณ ๊ทธ๋ํ ์์ฑ

    - ์ง์ค๋ ํต๊ณ ๊ทธ๋ํ์์ ๊ฐ feature์ ์ ์์ ๋ฐ๋ผ ์ง์ค๋ level ๋ถ์ฌ
    - ์ง์ค๋ ํต๊ณ ๊ทธ๋ํ์์ ๊ฐ level์ ๋ฐ๋ผ ํด๋น Room์์์ ๋ฑ์ ์ง์ 
5. ์์ฑ ํ๋ Room์ ๊ธฐ์ค์ผ๋ก ์ฌ์ฉ์์๊ฒ Room List ์ ๊ณต
6. ์์ฑ ํ๋ ํต๊ณ ์๋ฃ๋ฅผ ๊ธฐ์ค์ผ๋ก ์ฌ์ฉ์์๊ฒ ์ง์ค๋ ํต๊ณ ์๋ฃ List ์ ๊ณต

## ๐น API & Library
1. Luxand API - ์ผ๊ตด ์ธ์
2. SSL - https ํต์ 
3. Animated - ์ ๋๋ฉ์ด์
4. Bootstrap - UI/UX
5. Lotties - loading animation

## ๐ Rest API
`POST` /  โ ์ฌ์ฉ์ ์์ด๋ ์ค๋ณต ์ฒดํฌ ๋ฐ ๋น๋ฐ๋ฒํธ ์ฌ์๋ ฅ ํ์ธ ์์ฒญ

`POST` / login โ ์ฌ์ฉ์ ์์ด๋ ๋ฐ ๋น๋ฐ๋ฒํธ ์์ฒญ

`GET` / logout โ ๋ก๊ทธ์์

`POST` / makeroom โ STUDY/EXAM ๋ชจ๋์ ๋ฐ๋ผ ๋ฐฉ์์ฑ

`POST` / makeroom/success โ ๋ฐฉ ์์ฑ ์ฑ๊ณต ํ ๋ฐฉ ์ ๋ณด ๋์ด

`POST` / enteroom/exam1 โ EXAM ๋ชจ๋ ์ฑ ์ฐจ๋จ ์ฌ๋ถ ์์ฒญ

`POST` / enteroom/exam2 โ EXAM ๋ชจ๋ ์ผ๊ตด ์ธ์ ํ์ธ ์์ฒญ

`POST` / enteroom/exam3 โ EXAM ๋ชจ๋ WebRTC ์์ฅ ๊ฐ๋ฅ ์ฌ๋ถ ์์ฒญ 

`POST` / enteroom/study1 โ STUDY ๋ชจ๋ ์ฑ ์ฐจ๋จ ์ฌ๋ถ ์์ฒญ

`POST` / enteroom/study2 โ STUDY ๋ชจ๋ WebRTC ์์ฅ ๊ฐ๋ฅ ์ฌ๋ถ ์์ฒญ

`GET` / roomout/<int:time>/<str:mode> โ mode๊ฐ STUDY ์ผ๋ ํด๋น ์ฌ์ฉ์์ Analytics์ time์ด ์ ์ฅ๋จ

`POST` / roomout/<int:time>/<str:mode> โ App ์ ๊ทผ ์ฐจ๋จ์ ํด์  ํ์๋์ง ์์ฒญ & mode๊ฐ STUDY ์ผ๋ ์ ์ฅ๋ค time, app, person ๋ณ์๋ฅผ ๋ฐํ์ผ๋ก level, rate๋ฅผ ์ธก์ ํ๊ณ  Analytics ๋ชจ๋ธ์ ์ ์ฅ 

`GET` / roomout/study โ session์์ ์ฌ์ฉ์ ์ ๋ณด๋ฅผ ๊ฐ์ ธ์ Analytics ๋ชจ๋ธ์ ๊ฐ์ฅ ๋ง์ง๋ง row๋ฅผ DB์์ ๊ฐ์ ธ์์ ์ง์ค๋ ๊ทธ๋ํ๋ฅผ ๊ทธ๋ฆผ 

`POST` / roomout/exam โ ์ํ์ด ์ฑ๊ณต์ ์ผ๋ก ์ข๋ฃ ๋๋์ง ์์ฒญ

`GET` / list/room โ Room DB์์ ์ฌ์ฉ์ ์ด๋ฆ์ผ๋ก ๋ง๋ค์ด์ง Room์nQuerySet์ผ๋ก ๋ฐํํ list ๋ํ๋

`GET` / list/analytics โ Analytics DB์์ ์ฌ์ฉ์ ์ด๋ฆ์ผ๋ก ๋ง๋ค์ด์ง Analytics๋ฅผ QuerySet์ผ๋ก ๋ฐํํ list ๋ํ๋

`POST`/ list/analytics/<int:pk> โ Analytics List์์ ์ ํํ QuerySet ๊ฐ์ฒด์ Primary Key ๊ฐ๊ณผ ๊ฐ์ row๋ฅผ DB์์ ๊ฐ์ ธ์ ์ง์ค๋ ๊ทธ๋ํ๋ฅผ ๊ทธ๋ ค์ค

## ๐โโ๏ธMy Role
- django UI/UX ์ ์ฒด frontend ๊ฐ๋ฐ
- django Rest API ์ค๊ณ ๋ฐ ๊ฐ๋ฐ
- Luxand API ์ผ๊ตด์ธ์์ ํตํ ์ฌ์ฉ์ ์ธ์ฆ ๊ธฐ๋ฅ ๊ฐ๋ฐ
- ๋ก๊ทธ์ธ/ํ์๊ฐ์ ๊ฐ๋ฐ
- ์ฌ์ฉ์ ์ด๋ฏธ์ง ๋ณ๊ฒฝ์ด ๊ฐ๋ฅํ my page ๊ฐ๋ฐ
- Class ์์ฑ ๋ฐ ์์ฅ ๊ฐ๋ฐ
- ์ง์ค๋ ํต๊ณ์๋ฃ ๊ทธ๋ํ ๊ธฐ๋ฅ ๊ฐ๋ฐ
## License
```
MIT License

Copyright (ํ๋ชฝ์ ์) [2021-08-15] [HanSik Hwang]

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
