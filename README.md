# 语音指令刷视频软件

## 简介
这是一个基于语音指令的视频自动刷取软件，支持唤醒词“小林”激活，并可通过语音指令“下一个”或“上一个”切换视频。

## 安装
1. 安装Python 3.8+。
2. 安装依赖：`pip install -r requirements.txt`
3. 运行：`python main.py`

## 使用
- 启动程序后，说“小林”唤醒。
- 然后说“下一个”或“上一个”切换视频。

## 注意
- 需要麦克风权限。
- 视频平台为YouTube（可修改config.py）。
- 如果出现浏览器无法启动错误，可以在 config.py 中设置 `CHROME_PATH` 为 Chrome 可执行文件路径。
- 语音识别依赖网络。

## 测试
- 使用 `test_voice_control.py` 可在命令行通过语音测试指令识别。
- 使用 `test_video_controller_keyboard.py` 可通过键盘的上/下方向键手动触发视频切换。