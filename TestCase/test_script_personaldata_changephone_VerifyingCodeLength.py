'''
-*- coding:utf-8 -*-
Author : 李朋军
TestCase: 登录伯图全景测试
DateTime: 2018-1-18
用例标题：个人资料-更换手机号-验证码长度
测试步骤：1.验证码不足6位，点击“下一步”
		  2.验证码输入超过6位
预期结果：1.验证码错误，有相关提示信息
		  2.超过6位不可输入
'''
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class test_script_personaldata_modifyphone_VerficationCodeLength(unittest.TestCase):

	def setUp(self):

		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '7.0'
		desired_caps['deviceName'] = 'MAY9X17716W02032'
		desired_caps['appPackage'] = 'tech.yunjing.biconlife'
		desired_caps['appActivity'] = 'tech.yunjing.biconlife.LaunchActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
		self.driver.implicitly_wait(15)

 
	def tearDown(self):

		self.driver.quit()


	def test_script(self):
		sleep(5)
		#定位“我的”并点击
		self.driver.find_element_by_name("我的").click()

		sleep(2)
		nick = self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/tv_mf_userNick")
		#判断昵称是否显示
		if nick.is_displayed:
			nick.click()
		else:
			print("nick not found")

		sleep(2)
		phone = self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/ll_phone")
		#判断手机号字段是否存在
		if phone.is_displayed:
			phone.click()
		else:
			print("phone not found")

		sleep(2)
		EditText = self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/et_code")
		EditText.send_keys("111")
		
		#定义“下一步”按钮并点击
		next_btn = self.driver.find_element_by_id("tech.yunjing.biconlife.app.mine:id/tv_next")
		next_btn.click()
		
		#断言
		self.assertTrue(next_btn.is_displayed)

		sleep(2)
		EditText.send_keys("123456789")
		value = EditText.get_attribute('value')
		assertTrue(value == '123456')


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(test_script_personaldata_modifyphone_VerficationCodeLength)
	unittest.TextTestRunner(verbosity=2).run(suite)