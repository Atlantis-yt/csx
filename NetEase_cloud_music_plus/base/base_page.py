from utils import DriverUtil
import logging
import time
import os
from config import BASE_DIR
class BasePage:
    """
    对象库层-基类
    """
    def __init__(self):
        self.driver = DriverUtil.GetDriver()


    def find_element(self, location):
        logging.info("location={}".format(location))
        return self.driver.find_element(location[0], location[1])


class BaseHandle:
    """
    操作层-基类
    """

    def input_text(self, element, text):
        """
        在输入框里输入文本内容，先清空再输入
        :param element: 要操作的元素
        :param text: 要输入的文本内容
        """
        element.clear()
        element.send_keys(text)


    def click_object(self,element):
        "定位元素并点击"
        element.click()

class BaseProxy:
    """
    业务层-基类
    """
    def __init__(self):
        self.driver = DriverUtil.GetDriver()


    def ScreenShot(self):
        try:
            t = time.strftime("%Y-%m-%d-%H-%M-%S")
            print(t)
            img_path = "{}/screenshot/-{}.png".format(BASE_DIR,t)
            print(img_path)
            self.driver.get_screenshot_as_file(img_path)
        except BaseException as msg:
            print("%s:截图失败!!!!!!!!!!!!!!" %msg)


    def obtain_title(self):
        self.driver.title()

    # 获取当前句柄切换
    def Windows_switch(self):
        driver = DriverUtil.GetDriver()
        handle = driver.window_handles
        print(handle)
        driver.switch_to_window(handle[1])



    def Windows_switch_return(self):
        driver = DriverUtil.GetDriver()
        handle = driver.window_handles
        driver.switch_to_window(handle[0])






