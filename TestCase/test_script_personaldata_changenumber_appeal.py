# -*- coding:utf-8 -*-
# Author : 王党军
#TestCase: 个人资料-更换手机号-立即申诉测试用例
#          点击“手机号无接收短信？立即申诉”
#          页面跳转至申诉页面
#DateTime: 2018-3-7

import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

#延时时间
T = 2

class test_script_order_display(unittest.TestCase):
    
    def setUp(self):
         
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'MXF0215826004374'
        #desired_caps['app'] = 'C:\\Users\\root\\Downloads\\app-release.apk'
        desired_caps['appPackage'] = 'tech.yunjing.biconlife'
        desired_caps['appActivity'] = 'tech.yunjing.biconlife.LaunchActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def tearDown(self):
        
        self.driver.quit()
        
    def test_script_order_display(self):
        #操作步骤
        sleep(5*T)
        #点击“我的”tab
        self.driver.find_element_by_name("我的").click()
        sleep(1*T)
        
        #点击“个人资料"头像
        self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/yjuav_mf_userAvatar").click()
        sleep(1*T)

        #进入个人资料，点击手机号码
        self.driver.find_element_by_name("手机号码").click()
        sleep(2*T)
        
        #进入更换手机号码，点击立即申诉
        self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/tv_nowAppeal").click()
        sleep(T)
        #断言
        appeal_page = self.driver.find_element_by_id("tech.yunjing.biconlife:id/tv_ljtb_title")
        print appeal_page.text
        assert appeal_page.text == u"填写信息"

        name = self.driver.find_element_by_name("真实姓名")
        number = self.driver.find_element_by_name("身份证号")
        assert name.is_displayed()==True
        assert number.is_displayed()==True

                
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script_order_display)
    unittest.TextTestRunner(verbosity=2).run(suite)

