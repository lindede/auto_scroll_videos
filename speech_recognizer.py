# speech_recognizer.py - 语音识别（已集成在audio_listener.py中，此文件备用）

# 如果需要单独使用
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("请说话...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="zh-CN")
            return text.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None