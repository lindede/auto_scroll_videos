# video_controller.py - 视频控制

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import VIDEO_URL, CHROME_PATH
import time
import os

class VideoController:
    def __init__(self, chrome_path: str | None = None):
        """Initialize controller.

        :param chrome_path: optional path to Chrome binary; if not provided,
            the value from ``config.CHROME_PATH`` will be used (may be None).
        """
        self.driver = None
        # allow override or fallback to config setting
        self.chrome_path = chrome_path or CHROME_PATH

    def start_browser(self):
        """启动浏览器并打开视频页面.

        Attempts to start Chrome using ``webdriver.Chrome``.  If a chrome
        binary path is configured, we set ``binary_location``; otherwise
        Selenium will try to locate Chrome automatically.
        """
        options = webdriver.ChromeOptions()
        if self.chrome_path:
            print(f"使用的chrome可执行路径: {self.chrome_path}")
            options.binary_location = self.chrome_path
        else:
            print("未指定chrome路径，将由系统自动查找")

        def _normalize_driver_path(path: str) -> str:
            # webdriver-manager may sometimes return a path to a file inside
            # the downloaded zip (e.g. THIRD_PARTY_NOTICES.chromedriver) rather
            # than the actual executable.  Attempt to locate the real
            # chromedriver.exe in the same directory tree.
            if path.lower().endswith(".exe") and os.path.isfile(path):
                return path

            base = os.path.dirname(path)
            if os.path.isdir(base):
                for root, dirs, files in os.walk(base):
                    for fname in files:
                        if fname.lower().startswith("chromedriver") and fname.lower().endswith(".exe"):
                            candidate = os.path.join(root, fname)
                            print(f"找到chromedriver可执行文件: {candidate}")
                            return candidate
            # last resort: return original path
            return path

        try:
            driver_path = ChromeDriverManager().install()
            print(f"初始ChromeDriver路径: {driver_path}")
            driver_path = _normalize_driver_path(driver_path)
            print(f"规范化后的ChromeDriver路径: {driver_path}")
            self.driver = webdriver.Chrome(
                service=Service(driver_path),
                options=options,
            )
        except OSError as e:
            # provide more context if the binary or driver could not be launched
            print(f"无法启动Chrome驱动: {e}")
            print("请确认下载的驱动与系统架构匹配，并且不是一个损坏文件。")
            print(f"尝试启动的可执行路径: {driver_path if 'driver_path' in locals() else '<unknown>'}")
            raise

        self.driver.get(VIDEO_URL)
        time.sleep(2)  # 等待页面加载

    def next_video(self):
        """切换到下一个视频"""
        if self.driver:
            try:
                # YouTube的next按钮（可能需要调整选择器）
                next_button = self.driver.find_element(By.CSS_SELECTOR, "#navigation-button-down .yt-spec-button-shape-next")
                next_button.click()
                print("切换到下一个视频")
            except Exception as e:
                print(f"无法切换视频: {e}")

    def previous_video(self):
        """切换到上一个视频（YouTube可能没有直接previous）"""
        if self.driver:
            try:
                # 模拟或使用历史
                next_button = self.driver.find_element(By.CSS_SELECTOR, "#navigation-button-up .yt-spec-button-shape-next")
                next_button.click()
                print("切换到上一个视频")
            except Exception as e:
                print(f"无法切换视频: {e}")

    def close_browser(self):
        """关闭浏览器"""
        if self.driver:
            self.driver.quit()