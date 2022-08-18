# 1인가구 레시피 추천 웹, 혼자서도 잘해요리

내일배움캠프 팀 F4 추천 시스템 프로젝트 - 혼자서도 잘해요리

# 🤹‍♀️ 팀 구성원

### 👨‍💻 김태인 [블로그 링크](https://velog.io/@kti0940)

### 👨‍💻 김희정 [블로그 링크](https://khjhj3808.tistory.com/)

### 👨‍💻 한예슬 [블로그 링크](https://velog.io/@tasha_han_1234)

### 👨‍💻 황영상 [블로그 링크](http://velog.io/@migdracios)

# 📌프로젝트 소개

- 혼자서도 잘해요리는 1인가구 사용자에게 레시피를 검색, 추천 기능을 제공하는 웹입니다.
- 사용자는 게시된 다양한 레시피를 참조할 수 있습니다.
- 또한 자신이 레시피를 직접 작성하여 다른 사용자와 공유할 수 있습니다.
- 형태소로 분리된 재료들을 바탕으로 다른 레시피를 또한 추천받을 수 있습니다.

# 📌기술스택

## 백엔드

<div style="display:flex">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
</div>

## 프론트엔드

<div style="display:flex">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
</div>

## 데이터베이스

<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white">

## 프로젝트 기능 요약
![혼자서도 잘해요리 메인1](https://user-images.githubusercontent.com/61997714/185313870-7d35923f-d6a4-4e83-8cbe-67ff324f760f.gif)
![혼자서도잘해요리 상세페이지](https://user-images.githubusercontent.com/61997714/185320540-e293b468-3841-4a1e-b921-8ad669055f42.gif)
![혼자서도 잘해요리 나만의레시피](https://user-images.githubusercontent.com/61997714/185320657-c82b5f27-4073-4e2c-811b-42ed471f9195.gif)
![혼자서도잘해요리 댓글](https://user-images.githubusercontent.com/61997714/185320720-9170f77e-0825-4ec9-8640-cf80724738a4.gif)
![혼자서도잘해요리 추천서비스](https://user-images.githubusercontent.com/61997714/185320775-b915c0d2-f59b-4a47-8497-e9259eb2725f.gif)
![혼자서도잘해요리 필터링](https://user-images.githubusercontent.com/61997714/185320806-2db6fe56-8231-4d7f-92bf-e13d031caa74.gif)

# 📌프로젝트 구조

## 프로젝트 아키텍쳐

- 혼자서도 잘해요리는 서버 사이드 렌더링으로 EC2를 통하여 프론트와 백엔드가 모두 한 번에 구현되었습니다.

## 서비스 플로우

### 회원기능

- 사용자는 사이트 자체에서 회원가입과 로그인을 사용하여 웹에 접근할 수 있습니다.
- 회원가입은 아이디, 비밀번호, 닉네임을 기입하여 회원가입 버튼을 클릭해서 회원 데이터를 저장합니다.

### 레시피 조회

- 사용자는 작성된 레시피의 목록을 조회하고, 목록 중 원하는 레시피 카드를 클릭하여 레시피의 상세 내용을 볼 수 있습니다.
- 사용자는 조회한 레시피의 재료 및 조리시간, 난이도, 조리순서 등을 확인할 수 있습니다.
- 사용자는 검색, 정렬, 필터 기능을 사용하여 원하는 레시피를 찾아서 확인할 수 있습니다.
- 2000여개에 달하는 레시피를 서버 부하를 줄이며 보여주기 위해 장고 페이지네이션 기능을 사용했습니다.

### 레시피 작성

- 로그인 한 사용자는 이미지를 포함한 레시피를 작성할 수 있습니다

### 레시피 추천

- Mecab 토크나이저를 사용해 레시피를 키워드로 나누고 이를 벡터모델을 사용해 유사한 다른 레시피를 추천했습니다. 결과적으로 96%이상에 육박하는 높은 정확도를 보였습니다.

### 레시피 댓글 작성

- 로그인 한 사용자는 다른이용자가 작성한 게시물에 댓글을 작성 할 수 있으며, 좋아요도 달 수 있습니다

### 마이페이지

- 내가 작성한 글, 댓글, 북마크한 요리를 모아볼 수 있습니다

# 📌[Starting Assignment](https://github.com/tunEmvegnomb/cook_alone/wiki/Project-Starting-Assignment)
