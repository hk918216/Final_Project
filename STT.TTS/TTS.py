#TTS ( Text To Speech)

#!pip install gTTS
#!pip install playsound==1.2.2


from gtts import gTTS
from playsound import playsound

# 영어 문장
# text = 'Can I help you?'
# file_name = 'sample.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)
# playsound(file_name)

# 한글 문장
text = '제가 생각하기에는 오늘의 감정은 감사인 것 같아요! 오늘 미션임파서블을(를) 추천드려요!'
file_name = 'sample.mp3'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)

# 긴 문장 (파일에서 불러와서 처리)
# with open('sample.txt', 'r', encoding='utf8') as f:
#     text = f.read()
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name)