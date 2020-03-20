from selenium import webdriver
import time


# 驱动操作工具类
class DriverUtil:

    _driver=None  #驱动对象
    _auto_quit = True


    # 获取驱动，并完成初始化
    @classmethod
    def GetDriver(cls):
        if cls._driver is None:

            cls._driver=webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(30)
            cls._driver.get("https://music.163.com/")
        return cls._driver

     # 关闭驱动
    @classmethod
    def QuitDriver(cls):
        if cls._auto_quit and cls._driver:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def set_auto_quit(cls, auto_quit):
        """设置是否自动退出驱动"""
        cls._auto_quit = auto_quit



# 滚动条下拉致最下
def roll():
    driver=DriverUtil.GetDriver()
    js="window.scrollTo(0, 10000000)"
    driver.execute_script(js)





#





