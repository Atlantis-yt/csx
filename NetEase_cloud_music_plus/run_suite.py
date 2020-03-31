import logging
import time
import unittest
from NetEase_cloud_music_plus.script.test_A_login import TestLogin
from NetEase_cloud_music_plus.script.test_B_user_settinngs import Test_user_settings
from NetEase_cloud_music_plus.script.test_C_seek_play import Test_seek_play
from NetEase_cloud_music_plus.tools.HTMLTestRunner import HTMLTestRunner
from NetEase_cloud_music_plus.utils import DriverUtil
from NetEase_cloud_music_plus.config import init_log_config

    ##构建测试套件
try:
    DriverUtil.set_auto_quit(False)
    suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestLogin))
    suite.addTest(unittest.makeSuite(Test_user_settings))


    report_file = "./report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
    with open(report_file, "wb") as f:
        runner = HTMLTestRunner(f, title="WMS自动化测试报告", description="Win10.Chrome_郑文强")
        runner.run(suite)
except Exception as e:
    logging.exception(e)

finally:
    DriverUtil.set_auto_quit(True)
    DriverUtil.QuitDriver()
