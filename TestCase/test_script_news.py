# -*- coding:utf-8 -*-
# Author : 陈强强
#TestCase: 个人资料-实名认证-身份证号码输入正确，姓名输入10个汉字，点击“下一步”
#DateTime: 2018-1-18

import unittest
from appium import webdriver
from time import sleep
import helper
import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

#延时时间
T = 2

class test_script(unittest.TestCase):
    
    def setUp(self):  
        os.popen("adb uninstall io.appium.android.ime")   
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'MXF0215826004374'
        #desired_caps['app'] = 'C:\\Users\\root\\Downloads\\app-release.apk'
        desired_caps['appPackage'] = 'tech.yunjing.biconlife'
        desired_caps['appActivity'] = 'tech.yunjing.biconlife.LaunchActivity'
        
        #启动appium的输入法
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        

    def tearDown(self):
        
        self.driver.quit()
        #卸载appium输入法
        os.popen("adb uninstall io.appium.android.ime")
        
    #滑动查找指定元素并点击
    # item_name：元素的name属性  
    def _find_by_scroll(self,item_name):
        item=self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "'
            + item_name + '")'
            ) 
        item.click() 
            
    """
    The id number is entered correctly, the name is entered in 10 Chinese characters, and click "next".
    """
    def test_script(self):
        #操作步骤
        
        #点击我的  tab
        me_btn=self.driver.find_element_by_name("发现")
        if me_btn.is_displayed():
            me_btn.click()
            sleep(T*1)
            
        
        self.driver.find_element_by_name('新闻').click()
        sleep(T)
        helper.swipe_down(self.driver)
        sleep(T*2)
        item=self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ListView").childSelector(new UiSelector().className("android.widget.RelativeLayout").index(3))')
        item.click()
        sleep(5)
        
        
        helper.find_element_scroll(self.driver,'tech.yunjing.biconlife.app.news:id/rl_ndw_praise')
        sleep(5)
        
        
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.news:id/iv_ndf_bg_picture').click()
        

        

        
        
              
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)