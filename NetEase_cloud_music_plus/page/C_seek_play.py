from NetEase_cloud_music_plus.base.base_page import BaseHandle,BaseProxy,BASE_DIR,BasePage
from NetEase_cloud_music_plus.utils import  DriverUtil
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class seek_play_page(BasePage):
    def __init__(self):
        super().__init__()

        ##定位搜索框
        self.search=(By.ID,"auto-id-auDmzTTRmhmq2WTy")



    def find_search(self):
        return self.find_element(self.search)





class seek_play_handle(BaseHandle):
    def __init__(self):
        self.seek_play_Page=seek_play_page()


    def input_search(self):
        self.input_text(self.seek_play_Page.find_search(),"吻别")



class seek_play_proxy(BaseProxy):
    def __init__(self):
        super().__init__()
        self.seek_play_Handle= seek_play_handle()

    def seek_play_kessgoodbye(self):
        "搜索吻别播放"
        self.seek_play_Handle.input_search()
        time.sleep(3)



