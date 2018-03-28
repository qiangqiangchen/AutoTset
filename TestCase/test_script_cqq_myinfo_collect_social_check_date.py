# -*- coding:utf-8 -*-
# Author : 陈强强
#TestCase: 我的收藏-社交-收藏时间显示
#DateTime: 2018-3-21

import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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
        
        #测试数据
        test_text='hello world'
        
        action = TouchAction(self.driver)
        
        #操作步骤
        
        #点击社交按钮
        self.driver.find_element_by_name('社交').click()
        sleep(T)
        #点击通讯录
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/rl_address_book').click()
        sleep(T)
        #点击第一个好友
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/rl_friendClick').click()
        sleep(T)
        #点击发消息
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/tv_afd_send_msg').click()
        sleep(T)
        #输入测试数据
        self.driver.find_element_by_id('tech.yunjing.biconlife.libbaselib:id/et_message').send_keys(test_text)
        sleep(T)
        #点击发送按钮
        btn_send=self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/bt_send')
        if btn_send.is_enabled():
            btn_send.click()
            
        #长按聊天气泡
        tv_myText=self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/tv_myText')
        action.press(tv_myText).wait(4000).perform()
        sleep(T)
        #收藏文字消息
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/tv_collect').click()
        sleep(T*2)
        #返回到首页
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/image_back').click()
        sleep(T)
        
        #点击我的，进入我的主页
        self.driver.find_element_by_name("我的").click()
        sleep(T)
        #点击收藏
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/ll_mf_myFocus').click()
        sleep(T)
        
        #点击标题
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/tv_amc_title').click()
        sleep(T)
        #切换到社交
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/tv_pmc_socical').click()
        sleep(3)
        #判断收藏列表是否为空
        flag=u"暂时还没有收藏过任何内容···" in self.driver.page_source
        
        if flag:
            print "The page content is empty"
        else:
            print "The page content is not empty"
        
        
        assert flag==False 
        
        
        #获取创建时间进行断言
        tv_shv_create_date=self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/tv_shv_create_date')
        assert tv_shv_create_date.text==u'今天'
        #进入详情
        hv_cst_head_view=self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/hv_cst_head_view')
        hv_cst_head_view.click()
        sleep(T)
        
        #断言页面标题和创建时间
        tv_ljtb_title=self.driver.find_element_by_id('tech.yunjing.biconlife:id/tv_ljtb_title')
        tv_details_date=self.driver.find_element_by_id('tech.yunjing.biconlife.app.mine:id/tv_details_date')
        
        assert tv_ljtb_title.text==u'详情'
        assert u'今天' in tv_details_date.text
        
        
        #清除操作记录
        
        #返回收藏列表
        self.driver.find_element_by_id('tech.yunjing.biconlife:id/iv_ljtb_left_back').click()
        sleep(T)
        #删除收藏内容
        action.long_press(hv_cst_head_view).wait(4000).perform()
        self.driver.find_element_by_id('tech.yunjing.biconlife:id/btn_jcacd_confirm').click()
        sleep(3)
        
        #返回到主页
        self.driver.find_element_by_id('tech.yunjing.biconlife:id/iv_ljtb_left_back').click()
        sleep(T)
        #进入社交
        self.driver.find_element_by_name('社交').click()
        sleep(T)
        #进入聊天页面
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/tv_hha_week').click()
        sleep(T)
        #长按第一条消息
        tv_userNick=self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/tv_userNick')
        action.press(tv_userNick).wait(3000).perform()
        #删除
        self.driver.find_element_by_id('tech.yunjing.biconlife.app.social:id/tv_deleteConversation').click()
        sleep(T)
        
        
               
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite)