# -*- coding:utf-8 -*-
# Author : 彭垚
# TestCase: 个人中心-修改密码-返回
# DateTime: 2018-03-05

import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

# 延时时间
T = 2

class test_script(unittest.TestCase):

    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'MXF0215826004374'
        # desired_caps['app'] = 'C:\\Users\\root\\Downloads\\app-release.apk'
        desired_caps['appPackage'] = 'tech.yunjing.biconlife'
        desired_caps['appActivity'] = 'tech.yunjing.biconlife.LaunchActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def tearDown(self):

        self.driver.quit()

    def test_script(self):

        # 点击“我的”button
        my_button = self.driver.find_element_by_name("我的")
        sleep(5)
        my_button.click()
        sleep(4)
        # 点击“昵称”button
        nickname_button = self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/yjuav_mf_userInfo_layout")
        nickname_button.click()
        sleep(4)
        # 点击“修改登录密码”button
        UpdatePassword_button = self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/ll_psw")
        UpdatePassword_button.click()
        sleep(4)
        # 断言
        oneName = self.driver.find_element_by_name("获取验证码")
        twoName = self.driver.find_element_by_name("新密码")
        threeName = self.driver.find_element_by_name("确定")

        assert oneName.is_displayed() == True
        assert twoName.is_displayed() == True
        assert threeName.is_displayed() == True
        # 点击“返回”button
        return_button = self.driver.find_element_by_id("tech.yunjing.biconlife:id/rl_ljtb_left_layout")
        return_button.click()
        sleep(4)
        # 断言
        fourName = self.driver.find_element_by_name("更换头像")
        fiveName = self.driver.find_element_by_name("手机号码")
        sixName = self.driver.find_element_by_name("实名认证")

        assert fourName.is_displayed() == True
        assert fiveName.is_displayed() == True
        assert sixName.is_displayed() == True

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)