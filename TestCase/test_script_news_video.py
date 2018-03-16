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
        self.driver.implicitly_wait(15)
        

    def tearDown(self):
        
        self.driver.quit()
        #卸载appium输入法
        os.popen("adb uninstall io.appium.android.ime")
        
    def test_script1(self):
        
        print 'test_script1'
        #操作步骤
        
        #点击我的  tab
        me_btn=self.driver.find_element_by_name("发现")
        if me_btn.is_displayed():
            me_btn.click()
            sleep(T*1)
            
        
        self.driver.find_element_by_name('新闻').click()
        sleep(T)
        #进入小视频界面
        self.driver.find_element_by_name('小视频').click()
        sleep(T*2)
        
        #点击更多按钮
        item=self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ListView").childSelector(new UiSelector().className("android.widget.LinearLayout").index(2))')        
        item.find_element_by_id('tech.yunjing.biconlife.app.news:id/ll_videoMore').click()
        
        #点赞按钮
        lists=self.driver.find_elements_by_class_name('android.widget.HorizontalScrollView')
        items=lists[1].find_elements_by_id('tech.yunjing.biconlife.app.news:id/iv_tag')
        sleep(2)
        flag = items[0].is_selected()
        items[0].click()
        sleep(5)
        
        helper.swipe_down(self.driver)
        sleep(2)
        #点击更多按钮
        item=self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ListView").childSelector(new UiSelector().className("android.widget.LinearLayout").index(2))')        
        item.find_element_by_id('tech.yunjing.biconlife.app.news:id/ll_videoMore').click()
        
        for i in range(5):
            #点击更多按钮
            item=self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ListView").childSelector(new UiSelector().className("android.widget.LinearLayout").index(2))')        
            item.find_element_by_id('tech.yunjing.biconlife.app.news:id/ll_videoMore').click()
            sleep(2)
            self.driver.tap([(200,200)], 500)
        
        
        
#     def test_script2(self):
#         print 'test_script2'
#         #点击更多按钮
#         item=self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ListView").childSelector(new UiSelector().className("android.widget.LinearLayout").index(2))')        
#         item.find_element_by_id('tech.yunjing.biconlife.app.news:id/ll_videoMore').click()
#             
#         #点赞按钮
#         lists=self.driver.find_elements_by_class_name('android.widget.HorizontalScrollView')
#         items=lists[1].find_elements_by_id('tech.yunjing.biconlife.app.news:id/iv_tag')
#         sleep(2)
#               

        
        
              
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)