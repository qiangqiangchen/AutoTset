# -*- coding:utf-8 -*-
# Author : 陈强强
#TestCase: 点击热门搜索里面的任意一个热搜词
#TestResult:1.跳入对应文章详情/文章列表；Notice：显示热搜词不超过8个
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
        
        
        #查看热搜个数：小于8个就通过
        hot_word=self.driver.find_elements_by_id('tech.yunjing.biconlife.app.news:id/tv_vssi_content')
        hot_word_count=len(hot_word)
        if hot_word_count>8:
            print 'hot_word count error '
            
        elif hot_word_count<1:
            print 'hot_word is null'
            flag=True
        else:
            #点击第一个热词
            hot_word[0].click()
            sleep(T*2)
        
            if u"搜索无结果！" in self.driver.page_source:
                print 'search result is null' 
                flag=True
            elif self.driver.find_element_by_class_name('android.widget.ListView').is_displayed():
                print 'list not is null'
                flag=True
            
           
        #断言热搜是否小于等于8个
        assert hot_word_count<=8
        assert flag==True
        
        #清除搜索记录
        #self.driver.keyevent('4')
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.news:id/tv_sna_clear_history').click()
        sleep(T)
        self.driver.find_element_by_id('tech.yunjing.biconlife:id/btn_jcacd_confirm').click()
        sleep(T*2)
        
        
        
        
              
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)