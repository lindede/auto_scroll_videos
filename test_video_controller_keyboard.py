# test_video_controller_keyboard.py - 使用键盘上下键测试 VideoController

from video_controller import VideoController
from config import CHROME_PATH
import msvcrt
import time


def test_keyboard_control():
    """通过键盘上下方向键控制视频切换"""
    controller = VideoController()

    print(f"配置的Chrome路径: {CHROME_PATH}")
    print("启动浏览器并打开视频页面...")
    controller.start_browser()
    print("按上方向键(↑)切换到上一个视频，按下方向键(↓)切换到下一个视频。")
    print("按'q'退出。")

    try:
        while True:
            # msvcrt.getch() 是阻塞的，先读一个字节
            key = msvcrt.getch()
            # 方向键及功能键会先返回0或\xe0，需要再读取一个字节
            if key in (b"\x00", b"\xe0"):
                key2 = msvcrt.getch()
                if key2 == b'H':  # 上箭头
                    print("检测到上箭头，切换到上一个视频")
                    controller.previous_video()
                elif key2 == b'P':  # 下箭头
                    print("检测到下箭头，切换到下一个视频")
                    controller.next_video()
            elif key.lower() == b'q':
                print("退出测试")
                break
            # 其余按键忽略
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n测试通过Ctrl-C中断")
    finally:
        controller.close_browser()


if __name__ == "__main__":
    test_keyboard_control()
