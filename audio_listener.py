# audio_listener.py - 语音输入和唤醒词检测

import speech_recognition as sr
from config import WAKE_WORD

class AudioListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_for_wake_word(self):
        """监听唤醒词"""
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("监听唤醒词...")
            while True:
                audio = self.recognizer.listen(source)
                try:
                    text = self.recognizer.recognize_google(audio, language="zh-CN")
                    if WAKE_WORD in text.lower():
                        print(f"检测到唤醒词: {text}")
                        return True
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    print(f"语音服务错误: {e}")

    def listen_for_command(self):
        """监听指令"""
        with self.microphone as source:
            print("请说出指令...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language="zh-CN")
                print(f"识别到: {text}")
                return text.lower()
            except sr.UnknownValueError:
                print("无法识别语音")
                return None
            except sr.RequestError as e:
                print(f"语音服务错误: {e}")
                return None