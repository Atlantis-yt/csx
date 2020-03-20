from utils import DriverUtil
from page.C_seek_play import seek_play_proxy
import unittest
import time
import utils


class Test_seek_play(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=DriverUtil.GetDriver()
        cls.seek_play_Proxy=seek_play_proxy()


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        DriverUtil.QuitDriver()


    def test_B_seek_play(self):
        driver=self.driver
        self.seek_play_Proxy.seek_play_kessgoodbye()