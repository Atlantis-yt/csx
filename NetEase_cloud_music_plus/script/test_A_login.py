import unittest

from selenium.webdriver.common.by import By

import utils
import time
from page.A_login import LoginProxy
from utils import DriverUtil
from config import init_log_config
import logging

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.GetDriver()
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        DriverUtil.QuitDriver()

    def test_A_usmpwd_login(self):
        driver = self.driver
        self.login_proxy.login_music(269986702,"hyt12300")
        init_log_config()
        logging.info("登录")
        time.sleep(3)







