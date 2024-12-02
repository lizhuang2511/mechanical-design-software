# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:34:40 2022

@author: cptek053
"""

import pyautogui
# 默认这项功能为True, 这项功能意味着：当鼠标的指针在屏幕的最坐上方，程序会报错；目的是为了防止程序无法停止
pyautogui.FAILSAFE =False  
# 意味着所有pyautogui的指令都要暂停一秒；其他指令不会停顿；这样做，可以防止键盘鼠标操作太快；
pyautogui.PAUSE = 1    
print(pyautogui.size())   # 返回所用显示器的分辨率； 输出：Size(width=1920, height=1080)
width,height = pyautogui.size()
print(width,height)  # 1920 1080
# 将鼠标移动到指定的坐标；duration 的作用是设置移动时间，所有的gui函数都有这个参数，而且都是可选参数；
# 向右移动100px，68下移动500px, 这个过程持续 1 秒钟；
#pyautogui.moveTo(1798,10,duration=1)   
print(pyautogui.position())   # 得到当前鼠标位置；输出：Point(x=200, y=800)
