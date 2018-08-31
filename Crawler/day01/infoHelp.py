# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:34:58 2018

@author: Administrator
"""

## 巧妙的运用逻辑运算符来实现一个开关的功能
#0 and 'a' or 'b'
##'b'
#1 and 'a' or 'b'
##'a'

from urllib import request
#list的生成式
def info(object,collapse=0,spacing=15):
    """
    这个函数是用来实现把任意模块的可以调用的方法及说明
    按照一定的格式打印出来的方法。
    """
    #第一步
    # list的生成器,把原来的list做一次过滤，
    #只取可以被调用的方法
    methodList = [method for 
                  method in dir(object) 
                  if callable(getattr(object,method))]
    #print(methodList)
    
    # 第二步
    # 按照一定格式来显示doc string的信息
    # collapse是一个开关
    # collapse = 0 保持原来的格式
    # collapse = 1 去掉换行
    processFun = collapse and (lambda 
                               s:" ".join(s.split())
                               ) or (lambda s:s)
    
    
    # print打印一个大的字符串
    #这个字符串是一个list组成的
    #这个list中每一个又是一个字符串
    #list中的字符串由两部分组成:
    # 1.方法的名称，这里使用ljust做一次规整化
    # 2.对这个方法的说明文档做了一个格式的规整化
    print( '\n'.join(["%s %s"%( method.ljust(spacing),
                     processFun(str(getattr(object,method).__doc__)) ) 
    for method in methodList]) )
    
info(request,1)
#s = 123
#info(s)











