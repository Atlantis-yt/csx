import unittest
from NetEase_cloud_music_plus.base.base_page import BasePage, BaseHandle,BaseProxy
from NetEase_cloud_music_plus.utils import DriverUtil
from selenium.webdriver.common.by import By
import time

##登录网易云音乐

class login_page(BasePage):
    def __init__(self):
        super().__init__()

        ##点击登录按钮
        self.login_one =(By.XPATH,"//a[@class='link s-fc3']")

        ##点击勾选服务条款
        self.Check_the_service =(By.XPATH,"//input[@id='j-official-terms']")

        ##QQ登录
        self.QQ_login =(By.LINK_TEXT,"QQ登录")

        ##账号密码登录
        self.userpwd_login =(By.ID,"switcher_plogin")

        ##定位输入账号框
        self.username =(By.ID,"u")

        ##定位输入密码框
        self.password =(By.ID,"p")

        ##定位登录按钮
        self.button =(By.ID,"login_button")

    def find_login_one(self):
            return self.find_element(self.login_one)

    def find_Check_the_service(self):
            return self.find_element(self.Check_the_service)

    def find_QQ_login(self):
            return  self.find_element(self.QQ_login)

    def find_userpwd_login(self):
            return  self.find_element(self.userpwd_login)

    def find_username(self):
            return  self.find_element(self.username)

    def find_password(self):
            return  self.find_element(self.password)

    def find_button(self):
            return  self.find_element(self.button)


class Login_Handle(BaseHandle):

    def __init__(self):
        self.Login_Page = login_page()

    def click_login_one(self):
        self.click_object(self.Login_Page.find_login_one())

    def click_Check_the_service(self,):
        self.click_object(self.Login_Page.find_Check_the_service())

    def click_QQ_login(self):
        self.click_object(self.Login_Page.find_QQ_login())

    def click_userpwd_login(self):
        self.click_object(self.Login_Page.find_userpwd_login())

    def input_username(self,user):
        self.input_text(self.Login_Page.find_username(),user)

    def input_password(self,pwd):
        self.input_text(self.Login_Page.find_password(),pwd)

    def click_button(self):
        self.click_object(self.Login_Page.find_button())



class LoginProxy(BaseProxy):
    def __init__(self):
        super().__init__()
        self.login_handle = Login_Handle()

    #登录业务
    def login_music(self,user,pwd):
        music_handle=self.driver.current_window_handle
        self.login_handle.click_login_one()
        self.login_handle.click_Check_the_service()
        self.login_handle.click_QQ_login()
        time.sleep(1)
        self.Windows_switch()
        self.driver.switch_to.frame("ptlogin_iframe")
        self.login_handle.click_userpwd_login()
        self.login_handle.input_username(user)
        self.login_handle.input_password(pwd)
        self.login_handle.click_button()
        self.driver.switch_to_window(music_handle)
        self.driver.switch_to.frame("g_iframe")
        time.sleep(2)
        self.ScreenShot()




