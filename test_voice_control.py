# test_voice_control.py - 语音控制测试（不需要浏览器）

from audio_listener import AudioListener
from config import COMMANDS

def test_voice_control():
    """测试语音识别和指令识别"""
    listener = AudioListener()
    
    print("=" * 50)
    print("语音控制测试模式")
    print("=" * 50)
    print(f"唤醒词: 小林")
    print(f"支持指令: {', '.join(COMMANDS.keys())}")
    print("=" * 50)
    
    try:
        while True:
            print("\n正在等待唤醒词...")
            if listener.listen_for_wake_word():
                print("\n✓ 唤醒成功！")
                
                command_text = listener.listen_for_command()
                if command_text:
                    print(f"\n识别到的文本: {command_text}")
                    
                    # 检查指令
                    found_command = False
                    for key, action in COMMANDS.items():
                        if key in command_text:
                            print(f"✓ 指令识别成功: {key} -> {action}")
                            found_command = True
                            break
                    
                    if not found_command:
                        print(f"✗ 未识别的指令，支持的指令: {', '.join(COMMANDS.keys())}")
                else:
                    print("✗ 无法识别语音，请重试")
            
            print("\n继续等待...")
            
    except KeyboardInterrupt:
        print("\n\n测试结束")

if __name__ == "__main__":
    test_voice_control()
