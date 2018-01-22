# -*- coding:utf-8 -*-
# Author : 王党军
#TestCase: 登录伯图全景测试
#DateTime: 2018-1-18

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
        #点击登录button        
        login_button = self.driver.find_element_by_id("tech.yunjing.biconlife.app.login:id/tv_rala_login")
        if login_button.is_displayed():
            login_button.click()
            sleep(T*1)
        #输入手机号码和密码        
        number =self.driver.find_element_by_id("tech.yunjing.biconlife.app.login:id/et_la_user_phone")
        number.clear()
        sleep(T*1)
        number.send_keys("13772081342")
        sleep(T*1)
        
        password =self.driver.find_element_by_id("tech.yunjing.biconlife.app.login:id/et_al_user_password")
        password.send_keys("123456wang")
        sleep(T*2)
        #关闭输入法弹出框
        self.driver.find_element_by_id("tech.yunjing.biconlife.app.login:id/tv_la_login").click()
        sleep(T)
        #点击登录button
        self.driver.find_element_by_id("tech.yunjing.biconlife.app.login:id/tv_la_btn_login").click()
        sleep(T*2) 
        #断言
        oneName = self.driver.find_element_by_name("首页")
        twoName = self.driver.find_element_by_name("社交")
        threeName = self.driver.find_element_by_name("发现")
        fourName = self.driver.find_element_by_name("我的")

        assert oneName.is_displayed() == True
        assert twoName.is_displayed() == True
        assert threeName.is_displayed() == True
        assert fourName.is_displayed() == True
        flag = True
        assertTrue(flag) 
                
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)

