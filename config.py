# config.py - 配置文件

# 唤醒词
WAKE_WORD = "小林"

# 指令映射
COMMANDS = {
    "下一个": "next",
    "上一个": "previous"
}

# 视频平台URL（示例：YouTube）
VIDEO_URL = "https://www.youtube.com"

# 可选的 Chrome 浏览器可执行路径，留空使用系统默认查找
CHROME_PATH =  r"C:\Users\15009\AppData\Local\Google\Chrome\Application\chrome.exe"

# 其他配置
MICROPHONE_INDEX = None  # 麦克风索引，None为默认
LANGUAGE = "zh-CN"  # 语音识别语言