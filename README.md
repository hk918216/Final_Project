# Final_Project
## 말하는 일기장
### 1. 목적
####  a. 음성, 텍스트 데이터의 일기장 구현
####  b. 일기장 내용 요약, 감성분석, 워드클라우드 등

### 2. 데이터 수집
####  a. 녹음 데이터 저장(DB)
#####    - Kospeech 모델 사용하여 음성 녹음
#####    - 음성이 실시간으로 텍스트로 저장
####  b. 텍스트 데이터 저장(DB)
#####    - 직접 타이핑. 실시간 저장

### 3. 구현
####  a. KoBART
#####    - 한국어 요약 모델
#####    - 저장된 텍스트를 요약
####  b. KoBERT
#####    - 한국어 감성분석 모델
#####    - 수만건의 데이터가 미리 학습되어 있음
#####    - 공개되어있는 한국어 감성사전(리뷰, 댓글 등)은 클래스가 다양하지 않아 직접 사전 제작
####  c. WorldCloud
#####    - 입력한 텍스트 기반 토큰화, 빈도분석 후 시각화
####  d. django
#####    - 웹 구현. 모바일 사용가능
#####    - 녹음, 타이핑, 회원가입, 감성분석, 워드클라우드 구현

### 4. 한계점
#####    - 웹 호스팅 불가능하여 개인 노트북 또는 휴대전화에서 녹음 불가
#####    - kobart 모델 사용시 일기장 같은 일상문을 요약하기엔 원본상 의미가 맞지 않게 요약
#####    - GPU 사용을 위해 코랩 사용. django 연동이 어려워 감성분석 시 코랩을 따로 돌려야함 




