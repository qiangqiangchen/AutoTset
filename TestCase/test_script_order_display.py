# -*- coding:utf-8 -*-
# Author : 王党军
#TestCase: 登录伯图全景，订单展示测试用例
#          点击“订单”，查看页面展示信息
#          页面显示用户所购买商品的订单信息，“全部”、“待付款”、“待发货”、“待收货”、“待评价”
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
        
        #进入订单列表
        titlebar = self.driver.find_element_by_id("tech.yunjing.biconlife:id/tv_ljtb_title")
        if titlebar.is_displayed():
            
            #断言
            oneName = self.driver.find_element_by_name("全部")
            twoName = self.driver.find_element_by_name("待付款")
            threeName = self.driver.find_element_by_name("待发货")
            fourName = self.driver.find_element_by_name("待收货")
            fiveName = self.driver.find_element_by_name("待评价")

            assert oneName.is_displayed() == True
            assert twoName.is_displayed() == True
            assert threeName.is_displayed() == True
            assert fourName.is_displayed() == True
            assert fiveName.is_displayed() == True
        else:
            print "Testcase Fail!"

                
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script_order_display)
    unittest.TextTestRunner(verbosity=2).run(suite)

