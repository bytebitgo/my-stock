from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.utils import platform
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
import webview
import os

# 设置全屏和横屏
Window.fullscreen = 'auto'
Window.orientation = 'landscape'

KV = '''
BoxLayout:
    WebView:
        id: webview
'''

class WebView(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 获取HTML文件的绝对路径
        html_path = os.path.abspath('index.html')
        # 将文件路径转换为URL格式
        self.url = f'file://{html_path}'
        
        # 创建WebView
        if platform == 'android':
            from android.runnable import run_on_ui_thread
            
            @run_on_ui_thread
            def create_webview():
                webview.WebView(self).loadUrl(self.url)
        else:
            Clock.schedule_once(lambda dt: webview.WebView(self).loadUrl(self.url), 0)

class StockMarketTV(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    StockMarketTV().run() 