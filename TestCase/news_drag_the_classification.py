# -*- coding:utf-8 -*-
# author: 彭垚
# testcase：新闻-编辑分类-拖动
# datatime: 2018-03-28
import unittest
from appium import webdriver
from time import sleep
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

#延迟时间
T = 2

class test_script(unittest.TestCase):

    def setUp(self):
        os.popen('adb uninstall io.appium.android.ime')

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'MAY9X17716W02032'
        desired_caps['appPackage'] = 'tech.yunjing.biconlife'
        desired_caps['appActivity'] = 'tech.yunjing.biconlife.LaunchActivity'
        # 启动appium输入法
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def tearDown(self):

        self.driver.quit()
        os.popen('adb uninstall io.appium.android.ime')

    def Drag(self,element1,element2):
        print 'start Drag'
        #获取第一个元素的大小和位置
        size=element1.size
        
        location_1=element1.location
        x1=size['width']/2+location_1['x']
        y1=size['height']/2+location_1['y']
        
        #获取第二个元素的大小和位置
        location_2=element2.location
        x2=size['width']/2+location_2['x']
        y2=size['height']/2+location_2['y']
        
        #通过坐标判断移动的坐标
        
        if x1<x2 and y1==y2:
            #右滑
            print 'right'
            self.driver.swipe(x1,y1,x2+30,y2,5000)
        elif x1>x2 and y1==y2:
            #左滑
            print 'left'
            self.driver.swipe(x1,y1,x2-30,y2,5000)
        elif x1==x2 and y1>y2:
            #上滑
            print 'up'
            self.driver.swipe(x1,y1,x2,y2-30,5000)
        elif x1==x2 and y1<y2:
            #上滑
            print 'dowm'
            self.driver.swipe(x1,y1,x2,y2+30,5000)
        elif x1<x2 and y1<y2:
            #右下
            print 'right-dowm'
            self.driver.swipe(x1,y1,x2+30,y2+30,5000)
        elif x1<x2 and y1>y2:
            #右上
            print 'right-dowm'
            self.driver.swipe(x1,y1,x2+30,y2-30,5000)
        elif x1>x2 and y1<y2:
            #左下
            print 'right-dowm'
            self.driver.swipe(x1,y1,x2-30,y2+30,5000)
        elif x1>x2 and y1>y2:
            #左上
            print 'right-dowm'
            self.driver.swipe(x1,y1,x2-30,y2-30,5000)
        
            
            

    def test_script(self):

        sleep(4*T)
        # 点击“发现”
        self.driver.find_element_by_name('发现').click()
        sleep(1 * T)
        # 点击“新闻”
        self.driver.find_element_by_name('新闻').click()
        sleep(1*T)
        #点击“+”
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.news:id/iv_nha_channelAdd').click()
        sleep(1*T)
        #点击“编辑”
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.news:id/tv_action').click()
        sleep(1*T)
        #判断可拖动排序中的分类数
        count = self.driver.find_elements_by_id('tech.yunjing.biconlife.app.news:id/tv_name_selected_news')
        if len(count) > 1:
            for i in range(1, 3):
                self.driver.find_elements_by_id('tech.yunjing.biconlife.app.news:id/tv_name_un')[0].click()
            sleep(1*T)
            classify1 = self.driver.find_elements_by_id('tech.yunjing.biconlife.app.news:id/tv_name_selected_news')[0].text
            el1 = self.driver.find_elements_by_id('tech.yunjing.biconlife.app.news:id/tv_name_selected_news')[1]
            el2 = self.driver.find_elements_by_id('tech.yunjing.biconlife.app.news:id/tv_name_selected_news')[2]
            self.Drag(el1,el2)
            sleep(5)
            


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)