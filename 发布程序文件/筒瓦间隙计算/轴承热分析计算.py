# -*- coding = utf-8 -*-
# @time:2023/12/25 10:04
# Author:lizhuang
# @File:轴承热分析计算.py
# @Software:PyCharm
class test():
    def __init__(self):
        print('Python')
if __name__ == '__main__': 
  test=test()
  q=1.8/1000/60#m**3/s 0.75l/s
  ro=850#kg/m**3
  c=2090#j/(kg*du)
  ti=10#油温输入温度
  环境温度=7
  d=320/1000#轴承直径m
  b=350/1000#轴承宽度m
  散热系数=80#w/（m**2*度）
  Q=1291/2#w
  #油空气散热面积=0.5
  import sympy as sy
  to=sy.symbols("to")
  eq=sy.Eq(散热系数*sy.pi*d*b*(to-环境温度)+q*ro*c*(to-ti),Q)
  sol=sy.solve(eq,to)
  print(sol)

