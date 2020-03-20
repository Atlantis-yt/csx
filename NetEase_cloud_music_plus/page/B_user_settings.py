import unittest
from utils import DriverUtil
from base.base_page import BasePage, BaseHandle,BaseProxy
from selenium.webdriver.common.by import By
import time

class user_settings_page(BasePage):
    def __init__(self):
        super().__init__()

        # 点击签到
        self.sign_in =(By.XPATH,"//a[@class='u-btn2 u-btn2-dis']")

        # 点击头像
        self.Click_on_the_picture=(By.XPATH,"//div[@class='head f-fl f-pr']//img")


    def find_sign_in(self):
        self.find_element(self.sign_in)

    def find_Click_on_the_picture(self):
        self.find_element(self.Click_on_the_picture)




class user_settings_handle(BaseHandle):
    def __init__(self):
        super().__init__()
        self.user_setting_Page=user_settings_page()

    def  click_sign_in(self):
        self.click_object(self.user_setting_Page.find_sign_in())

    def click_Click_on_the_picture(self):
        self.click_object(self.user_setting_Page.find_Click_on_the_picture())


class user_settings_proxy(BaseProxy):
    def __init__(self):
        super().__init__()
        self.user_settings_Handle=user_settings_handle()


    def set_music(self):
        self.user_settings_Handle.click_sign_in()
        self.user_settings_Handle.click_Click_on_the_picture()