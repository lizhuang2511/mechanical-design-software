# -*- coding = utf-8 -*-
# @time:2023/5/26 15:12
# Author:lizhuang
# @File:拉紧螺栓的制定.py
# @Software:PyCharm
import numpy as np

class 拉紧螺栓计算():
    def __init__(self,立柱长度 = 240,拉紧螺栓长度 = 500,pn = 300000):
        self.立柱长度 =立柱长度  # cm
        self.拉紧螺栓长度 = 拉紧螺栓长度  # cm
        self.pn = pn  # kg
        self.k8=1.2
        self.螺栓许用应力=1300
        self.E=2100000
        self.立柱许用应力=600 # 公斤厘米方
    def 拉紧螺栓预估直径(self,d=0):
        self.pt = self.k8 * self.pn
        if d==0:
            self.d = np.sqrt(self.pt / np.pi / self.螺栓许用应力)  # cm #等效于pt/截面积
        else:
            self.d=d
        # d=d*10#mm
        return self.d
    def 立柱面积(self,a=0):
        if a==0:
          self.A = self.pt / 2 / self.立柱许用应力
        else:
            self.A=a
        return self.A
    def 拉紧螺栓伸长量(self):
        e = self.pt * self.拉紧螺栓长度 / np.pi / (self.d ** 2) / self.E
        return e
    def 立柱压缩量(self):
        el = self.pt * self.拉紧螺栓长度 / 2 / self.A / self.E
        return el
    def 拉紧螺栓冷却后力(self):
        self.p = 2 * self.A * self.拉紧螺栓长度 / (2 * self.A * self.拉紧螺栓长度 + np.pi * self.d ** 2 * self.立柱长度) * self.pt
        return
    def 冷却后立柱压缩量(self):  # 冷却后
        el = self.p * self.立柱长度 / 2 / self.A /self.E
        return el
    def 滑块不受载荷的应力(self):
        滑块不受载荷应力 = self.p / np.pi / (self.d ** 2)
        return 滑块不受载荷应力
    def 滑块受载荷应力(self):
        滑块受载应力 = self.pt / np.pi / (self.d ** 2)
        return 滑块受载应力
    def 螺栓产生的总应力(self,d=0,a=0):
        self.拉紧螺栓预估直径(d=d)
        self.立柱面积(a=a)
        self.拉紧螺栓冷却后力()
        self.滑块不受载荷应力1=self.滑块不受载荷的应力()
        self.滑块受载荷应力1 = self.滑块受载荷应力()
        self.总应力 = self.滑块不受载荷应力1 + (self.滑块受载荷应力1 - self.滑块不受载荷应力1) / self.k8
        return self.总应力
    def 立柱的最大压应力(self,p,A):
        应力 = p / 2 / A
        return 应力
    def 整体高度差(self,d=0,a=0):
        self.螺栓产生的总应力(d=d,a=a)
        变形 = (self.总应力 - self.滑块不受载荷应力1) / self.E * self.拉紧螺栓长度#cm
        return 变形
if __name__ == '__main__': 
  '''test=拉紧螺栓计算(立柱长度 = 247,拉紧螺栓长度 = 135,pn = 300000)
  test.k8=1.35
  test.拉紧螺栓预估直径(d=0)
  print('预估直径',test.d)
  实际直径=13.5
  test.拉紧螺栓预估直径(d=实际直径)
  拉紧螺栓伸长量=test.拉紧螺栓伸长量()
  print('拉紧螺栓伸长量cm', 拉紧螺栓伸长量)
  test.立柱面积()
  print('预估立柱面积cm', test.A)
  实际立柱面积=4920
  test.螺栓产生的总应力(d=实际直径,a=实际立柱面积)
  print('总应力kg/cm2', test.总应力)
  变形=test.立柱高度差为(d=实际直径, a=实际立柱面积)
  print('立柱变形', 变形)'''
  test = 拉紧螺栓计算(立柱长度=570, 拉紧螺栓长度=1000, pn=4000000)
  test.k8 = 1.5
  test.拉紧螺栓预估直径(d=0)
  print('预估直径', test.d)
  实际直径 = 37
  test.拉紧螺栓预估直径(d=实际直径)
  拉紧螺栓伸长量 = test.拉紧螺栓伸长量()
  print('拉紧螺栓伸长量cm', 拉紧螺栓伸长量)
  test.立柱面积()
  print('预估立柱面积cm', test.A)
  实际立柱面积 = 6000
  test.螺栓产生的总应力(d=实际直径, a=实际立柱面积)
  print('总应力kg/cm2', test.总应力,test.滑块不受载荷应力1,test.滑块受载荷应力1)
  变形 = test.立柱压缩量()
  print('立柱变形', 变形)
  整体变形 = test.整体高度差(d=实际直径, a=实际立柱面积)
  print('整体变形', 整体变形)
  #a=test.立柱高度差为(d=22,a=2400)
  '''立柱长度=240#cm
  拉紧螺栓长度=500#cm
  pn=300000#kg
  k8=2
  def 拉紧螺栓预估直径(pn):
      pt=2*pn
      d=np.sqrt(pt/np.pi/1300)#cm #等效于pt/截面积
      #d=d*10#mm
      return d
  拉紧螺栓直径=拉紧螺栓预估直径(pn)
  print(拉紧螺栓直径)
  def 拉紧螺栓伸长量(pn,拉紧螺栓长度,d):
      pt = 2 * pn
      E=210000
      e=pt*拉紧螺栓长度/np.pi/(d**2)/E
      return e
  拉紧螺栓伸长量1=拉紧螺栓伸长量(pn,拉紧螺栓长度,拉紧螺栓直径)
  print(拉紧螺栓伸长量1)
  def 立柱压缩量(pn,拉紧螺栓长度,A):
      pt = 2 * pn
      E = 210000
      el = pt * 拉紧螺栓长度 / 2/A / E
      return el
  def 立柱面积(pn):
      许用应力=700#公斤厘米方
      pt = 2 * pn
      A=pt/2/许用应力
      return A
  立柱面积1=立柱面积(pn)
  print(立柱面积1)
  def 拉紧螺栓冷却后力(pn,拉紧螺栓长度,立柱长度,d,A):
      pt = 2 * pn
      P=2*A*拉紧螺栓长度/(2*A*拉紧螺栓长度+np.pi*d**2*立柱长度)*pt
      return P
  def 冷却后立柱压缩量(p,立柱长度,A):#冷却后
      E = 210000
      el = p * 立柱长度 / 2 / A / E
      return el
  冷却后力=拉紧螺栓冷却后力(pn,拉紧螺栓长度,立柱长度,拉紧螺栓直径,立柱面积1)
  print(冷却后力)
  def 滑块不受载荷的应力(p,d):
      应力=p/np.pi/(d**2)
      return 应力
  滑块不受载荷的应力1=滑块不受载荷的应力(冷却后力,拉紧螺栓直径)
  def 滑块受载荷应力(pn,d):
      pt = 2 * pn
      应力 = pt / np.pi / (d ** 2)
      return 应力
  滑块受载荷的应力1 = 滑块受载荷应力(pn, 拉紧螺栓直径)
  def 螺栓产生的总应力(应力受载,应力不受载):
      应力=应力不受载+(应力受载-应力不受载)/2
      return 应力


  螺栓产生的总应力1=螺栓产生的总应力(滑块受载荷的应力1, 滑块不受载荷的应力1)
  print(螺栓产生的总应力1)
  def 立柱的最大压应力(p,A):
      应力=p/2/A
      return 应力


  立柱的最大压应力1=立柱的最大压应力(冷却后力,立柱面积1)
  print(立柱的最大压应力1)
  def 立柱高度差为(总应力,不受载应力,立柱长度):
      E=210000
      变形=(总应力-不受载应力)/E*立柱长度
      return 变形
  立柱变形=立柱高度差为(螺栓产生的总应力1,滑块不受载荷的应力1,立柱长度)
  print(立柱变形)'''