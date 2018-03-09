# -*- coding:utf-8 -*-
# Author : 王党军
#TestCase: 登录伯图全景测试
#DateTime: 2018-1-18
'''（1）用例标题：点击“我的”，进入个人资料页面
前置条件：1.登录账号
          步骤：1.个人资料页面，查看菜单名称
预期结果：1.菜单名称为“修改登录密码”
（2）用例标题：个人资料-修改登录密码-展示
前置条件：1.登录账号
          2.进入个人资料页面
步骤：1.个人资料页面，点击“修改登录密码”，查看页面跳转结果
预期结果：1.页面成功跳转至“修改登录密码”页面，页面布局与UI设计保持一致'''
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

#延时时间
T = 3

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
   
        #点击“我的”按钮
        sleep(5)
        fourName = self.driver.find_element_by_name("我的")
        fourName.click()
        #点击用户头像
        sleep(1)
        zl = self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/yjuav_mf_userInfo_layout")
        zl.click()
        #断言
        oneName = self.driver.find_element_by_name("个人资料")
        twoName = self.driver.find_element_by_name("退出登录")
        threeName = self.driver.find_element_by_name("修改登录密码")
        
        assert oneName.is_displayed() == True
        assert twoName.is_displayed() == True
        assert threeName.is_displayed() == True 

        
        #点击“修改登录密码”按钮
        sleep(5)
        change = self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/tv_psw")
        change.click()
        sleep(2)
        #断言
        fiveName = self.driver.find_element_by_name("修改登录密码")
        sixName = self.driver.find_element_by_name("获取验证码")
        sevenName = self.driver.find_element_by_name("新密码")

        assert fiveName.is_displayed() == True
        assert sixName.is_displayed() == True
        assert sevenName.is_displayed() == True 
        
                
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)

