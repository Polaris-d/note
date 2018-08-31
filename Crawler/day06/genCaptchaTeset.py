# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:42:16 2018

@author: Administrator
"""

# 这个库会帮我们生成验证码
#pip install captcha
from captcha.image import ImageCaptcha
import random
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 生成包含有数字，字母(大小写)
number = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 从包含52个数字和字母的集合中，随机取出四个元素，生成数字和字母的组合
def random_captcha_text(char_set=number+alphabet+ALPHABET, 
                        captcha_size=4):
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text

#print(random_captcha_text())

# 生成验证码字符集及图片
def gen_captcha_text_and_image():
    # 用来生成验证码图片的对象
    image = ImageCaptcha()
    
    # 生成四个字符的集合 
    captcha_text = random_captcha_text()
    # 利用list生成字符串
    captcha_text = ''.join(captcha_text)
    # 得到验证码图片
    captch_Image = image.generate(captcha_text)
    # 使用Image读取图片数据，转成np的矩阵表达，以显示图片
    captch_I = Image.open(captch_Image)
    captch_I = np.array(captch_I)
    return captcha_text,captch_I
    
if __name__ == "__main__":
    text, image = gen_captcha_text_and_image() 
    
    # 将生成的验证码及图片显示出来
    f = plt.figure()
    ax = f.add_subplot(111)
    ax.text(0.1, 0.9, text)
    plt.imshow(image)
    plt.show()









