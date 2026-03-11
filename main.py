# main.py - 主程序入口

from audio_listener import AudioListener
from video_controller import VideoController
from config import COMMANDS

def main():
    listener = AudioListener()
    controller = VideoController()
    controller.start_browser()

    try:
        while True:
            if listener.listen_for_wake_word():
                command_text = listener.listen_for_command()
                if command_text:
                    for key, action in COMMANDS.items():
                        if key in command_text:
                            if action == "next":
                                controller.next_video()
                            elif action == "previous":
                                controller.previous_video()
                            break
    except KeyboardInterrupt:
        print("程序退出")
    finally:
        controller.close_browser()

if __name__ == "__main__":
    main()