#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 基础包：图片对比机制
# author：马柱柱
# date:2017-9-21

from PIL import Image
import math
from functools import reduce
import operator

def cmp_png(path1,path2):
    image1=Image.open(path1)
    image3=Image.open(path2)
    h1=image1.histogram()
    h2=image3.histogram()
    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
#    print "切换前后图片二进制对比差异："
    print (result) 
    return (result)

