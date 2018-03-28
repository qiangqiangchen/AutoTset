# -*- coding:utf-8 -*-
# Author : 陈强强
#TestCase: 我的收藏-社交-列表为空
#DateTime: 2018-3-22

import unittest
from appium import webdriver
from time import sleep
import os

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
    Name, id number input space, special characters, line feed and other abnormal data.
    """      
    def test_script(self):
        
        #操作步骤
        
        #点击我的  tab
        me_btn=self.driver.find_element_by_name("我的")
        if me_btn.is_displayed():
            me_btn.click()
            sleep(T*1)
            
        #点击我的收藏按钮
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/ll_mf_myFocus').click()
        sleep(T)
        
        #点击标题
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/tv_amc_title').click()
        sleep(T)
        
        #切换到社交
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/tv_pmc_socical').click()
        
        
        
        #断言无界面文字显示是否正确
        flag=u"暂时还没有收藏过任何内容···" in self.driver.page_source
        if flag:
            print "The page content is empty"
        else:
            print "The page content is not empty"
        assert flag==True
        
        #断言缺省图是否显示
        iv_jni_defaultNoData=self.driver.find_element_by_id('tech.yunjing.biconlife:id/iv_jni_defaultNoData')
        assert iv_jni_defaultNoData.is_displayed()==True 
            
        
        
               
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)