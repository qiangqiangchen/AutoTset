#!/usr/bin/env python  
#coding=utf-8 
'''
Created on 2017-9-19

@author: Administrator
'''
import os  
import tempfile  
import shutil  
from PIL import Image
import math  
import operator   
import time
import sys

#PATH1 = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
PATH = lambda p: os.path.abspath(p)  
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")  
  
class Appium_Utils(object):  
    def __init__(self, driver):  
        self.driver = driver  
   
    def get_screenshot(self, name):
#        fp = "\\result\\"+name+".png"
#        self.driver.get_screenshot_as_file(fp)
        tm =  time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        type = ".png"
        fp = "result\\" + day + "\\image"
        if os.path.exists(fp):
            filename = str(fp)+"\\" + str(tm)+str("_")+str(name)+str(type)
            print filename
        else:
            os.makedirs(fp)
            filename = str(fp)+ "\\" + str(tm)+str("_")+str(name)+str(type)
            print filename
        
        self.driver.get_screenshot_as_file(filename)
        
    def get_screenshot_by_element(self, element):  
        self.driver.get_screenshot_as_file(TEMP_FILE)
        print "TEMP_FILE:-"+TEMP_FILE
#        获取元素bounds  
        location = element.location  
        size = element.size  
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])  
        #截取图片  
        image = Image.open(TEMP_FILE)  
        newImage = image.crop(box)  
        newImage.save(TEMP_FILE)  
        return self  
  
    def get_screenshot_by_custom_size(self, start_x, start_y, end_x, end_y):  
        #自定义截取范围  
        self.driver.get_screenshot_as_file(TEMP_FILE)  
        box = (start_x, start_y, end_x, end_y)  
  
        image = Image.open(TEMP_FILE)  
        newImage = image.crop(box)  
        newImage.save(TEMP_FILE)  
  
        return self  
  
    def write_to_file( self, dirPath, imageName, form = "png"):  
        #将截屏文件复制到指定目录下  
#        if os.path.isdir(dirPath):
#            shutil.rmtree(dirPath,True)
#            print dirPath + " was removed!"  
#        sleep(2)
        if not os.path.isdir(dirPath):  
            print "makedir"
            os.makedirs(dirPath)
        
        shutil.copyfile(TEMP_FILE, PATH(dirPath + "/" + imageName + "." + form))
  
    def load_image(self, image_path):  
        #加载目标图片供对比用  
        if os.path.isfile(image_path):  
            load = Image.open(image_path)  
            return load  
        else:  
            raise Exception("%s is not exist" %image_path)  
  
    def same_as(self, load_image, percent):  
        #对比图片，percent值设为0，则100%相似时返回True，设置的值越大，相差越大  
        
        image1 = Image.open(TEMP_FILE)  
        image2 = load_image  
  
        histogram1 = image1.histogram()  
        histogram2 = image2.histogram()  
  
        differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,   
                                                        histogram1, histogram2)))/len(histogram1))  
        print "differ--:"+str(differ)
        if differ <= percent:  
            return True  
        else:  
            return False  
        
    def get_module(self):  
  
        def main_module_name():  
            mod = sys.modules['__main__']  
            file = getattr(mod, '__file__', None)  
            return file and os.path.splitext(os.path.basename(file))[0]  
      
        def modname(fvars):  
      
            file, name = fvars.get('__file__'), fvars.get('__name__')  
            if file is None or name is None:  
                return None  
      
            if name == '__main__':  
                name = main_module_name()  
            return name  
  
        module_name = modname(globals())  
        return module_name
    
    def screencap_save(self,element,name):
        type = ".png"
        fp = "resource\\image"
        if os.path.exists(fp):
            filename = str(fp)+"\\" + str(name)+str(type)
            print filename
        else:
            os.makedirs(fp)
            filename = str(fp)+ "\\" + str(name)+str(type)
            print filename
        
        self.driver.get_screenshot_as_file(TEMP_FILE)
        print "TEMP_FILE:-"+TEMP_FILE
#        获取元素bounds  
        location = element.location  
        size = element.size  
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])  
        #截取图片  
        image = Image.open(TEMP_FILE)  
        newImage = image.crop(box)  
        newImage.save(filename)
        
    # print globals()  
    # print module_name  