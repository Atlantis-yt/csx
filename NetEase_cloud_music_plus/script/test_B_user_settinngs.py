import unittest
import NetEase_cloud_music_plus.utils
import time
from NetEase_cloud_music_plus.page.B_user_settings import user_settings_proxy
from NetEase_cloud_music_plus.utils import DriverUtil
import logging


class Test_user_settings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=DriverUtil.GetDriver()
        cls.user_settings_Proxy=user_settings_proxy()


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        DriverUtil.QuitDriver()


    def test_user_settings(self):
        driver=self.driver
        self.user_settings_Proxy.set_music()
        logging.info("签到")

