# -*- coding:utf-8 -*-
# Author : 陈强强
#TestCase: 新闻-搜索界面-热门搜索-返回搜索页
#TestResult:返回新闻首页
#DateTime: 2018-3-14

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
    The id number is entered correctly, the name is entered in 10 Chinese characters, and click "next".
    """
    def test_script(self):
        #操作步骤
        
        #结果标识，搜索无内容或者有内容后置为True
        flag=False
        
        #点击我的  tab
        me_btn=self.driver.find_element_by_name("发现")
        if me_btn.is_displayed():
            me_btn.click()
            sleep(T*1)
            
        #点击新闻
        self.driver.find_element_by_id("tech.yunjing.biconlife.app.find:id/rl_found_news").click()
        sleep(T)
        

        #点击搜索按钮
        self.driver.find_element_by_id('tech.yunjing.biconlife:id/iv_ljtb_right_back').click()
        sleep(T)
        
        #循环输入搜索记录
        test_text="test_test_"
        et_sna_search_key=self.driver.find_element_by_id('tech.yunjing.biconlife.app.news:id/et_sna_search_key')
        print et_sna_search_key.text
        
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.news:id/tv_vhsii_history_search_info_title').click()
        
#         for i in range(i,21):
#             et_sna_search_key.send_keys(test_text+str(i))
#             sleep(T)
#             self.driver.keyevent('66')
#             sleep(T*2)
#             et_sna_search_key.clear()
#             
#         et_sna_search_key.click()
        
        
        sleep(5)
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)