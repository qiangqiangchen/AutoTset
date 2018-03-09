# -*- coding:utf-8 -*-
# Author : 陈强强
#TestCase: 个人资料-修改登录密码-验证码为空
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
        self.driver.implicitly_wait(10)

    def tearDown(self):
        
        self.driver.quit()
        
    def test_script(self):
        #操作步骤
        print "=======successfully!======="
        
        #点击我的  tab
        me_btn=self.driver.find_element_by_name("我的")
        if me_btn.is_displayed():
            me_btn.click()
            sleep(T*1)
            
        #判断用户用户头像是否存在
        image_btn=self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/yjuav_mf_userAvatar')
        if image_btn.is_displayed():
            #点击用户头像
            image_btn.click()
            sleep(T*1)
       
        #寻找修改登录密码按钮，点击修改登录密码按钮
        resetpwd_btn=self.driver.find_element_by_name('修改登录密码')
        if resetpwd_btn.is_displayed():
            resetpwd_btn.click()
            sleep(T*1)
        
        #验证码输入框
        code_edit_text=self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/et_code')
        #密码输入框
        pwd_edit_text=self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/et_asomlp_password')
        #清空验证码输入框，密码框中输入123456789
        if code_edit_text.is_displayed() and pwd_edit_text.is_displayed():
            code_edit_text.clear()
            sleep(T*1)
            
            pwd_edit_text.send_keys("123456789")
            
            sleep(T*1)
        
        #隐藏键盘
        resetpwd_text=self.driver.find_element_by_name('修改登录密码')
        if resetpwd_text.is_displayed():
            resetpwd_text.click()
        
        #点击确定按钮
        ok_btn=self.driver.find_element_by_name('确定')
        if ok_btn.is_displayed():
            ok_btn.click()
            sleep(T*3)
        
        #通过判断验证码输入框判断页面是否跳转
        assert code_edit_text.is_displayed() == True
        print"=======finish======="
        
            

                
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)