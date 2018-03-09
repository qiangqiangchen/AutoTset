# -*- coding:utf-8 -*-
# Author : jxc
#TestCase: 个人资料-更换手机号-返回

import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

#延时时间
T = 2

class test_script(unittest.TestCase):
    
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
        
    def test_script(self):
        #操作步骤
        print "successfully!"
        sleep(5*T)

        #点击我的进入个人中心页面
        self.driver.find_element_by_name("我的").click()
        sleep(T)
        #点击我的头像进入个人资料页面
        self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/yjuav_mf_userAvatar").click()
        sleep(T)
        #点击手机号码查看页面展示
        self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/ll_phone").click()
        #点击返回按钮到个人资料页面
        self.driver.find_element_by_id("tech.yunjing.biconlife:id/iv_ljtb_left_back").click()
        #断言
        oneName = self.driver.find_element_by_name("个人资料")
        id = self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/yjuav_userAvatar")

        assert oneName.is_displayed() == True
        assert id.is_displayed() == True

      
                
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)

