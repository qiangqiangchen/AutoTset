# -*- coding:utf-8 -*-
# Author : 王党军
#TestCase: 登录伯图全景，订单返回测试用例
#          进入订单页面
#          点击“返回”
#          返回到个人中心页面
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

        #进入个人中心，点击订单
        self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/ll_fm_order").click()
        sleep(2*T)
        
        #在订单列表页，点击返回按钮
        self.driver.find_element_by_id("tech.yunjing.biconlife:id/iv_ljtb_left_back").click()
        sleep(T)
        #断言返回个人中心页面
   
        oneName = self.driver.find_element_by_name("活动中心")
        twoName = self.driver.find_element_by_name("实名认证")
        threeName = self.driver.find_element_by_name("我的优惠")
        fourName = self.driver.find_element_by_name("地址管理")

        assert oneName.is_displayed() == True
        assert twoName.is_displayed() == True
        assert threeName.is_displayed() == True
        assert fourName.is_displayed() == True
               
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script_order_display)
    unittest.TextTestRunner(verbosity=2).run(suite)

