import numpy as np
class 中间齿轮轴计算():
    def __init__(self):
       self.输入扭矩=4*1e7#kg*mm
       self.轴径=320
       self.齿轮位置=225
       self.齿轮pcd=1645#齿轮圆直径
    def 计算应力(self):
        self.齿轮荷重=self.输入扭矩*2/self.齿轮pcd
        self.断面积=np.pi*self.轴径**2/4
        self.弯力矩=self.齿轮荷重*self.齿轮位置
        self.剪切断面系数=np.pi*self.轴径**3/16
        self.弯曲断面系数=np.pi*self.轴径**3/32
        self.弯曲应力=self.弯力矩/self.弯曲断面系数
        self.剪切应力=self.输入扭矩/self.剪切断面系数
        self.合成弯矩=0.5*self.弯力矩*(1+np.sqrt(1+(self.输入扭矩/self.弯力矩)**2))
        self.合成剪切力矩=self.弯力矩*np.sqrt(1+((self.输入扭矩/self.弯力矩)**2))
        self.合成曲应力=self.合成弯矩/ self.弯曲断面系数#小于9
        self.合成切应力=self.合成剪切力矩/self.剪切断面系数#小于7#这个计算和书本不一致
        return
class 中间齿轮轴计算两点(中间齿轮轴计算):
    def __init__(self):
       self.输入扭矩=1.11*1e7#kg*mm
       self.轴径=310
       self.齿轮位置=410
       self.齿轮pcd=454.6#齿轮圆直径
       self.轴间距=2396
    def 计算应力(self):
        self.齿轮荷重=self.输入扭矩*2/self.齿轮pcd
        self.断面积=np.pi*self.轴径**2/4
        self.弯力矩=self.齿轮荷重*(self.轴间距-self.齿轮位置)*self.齿轮位置/self.轴间距#
        self.剪切断面系数=np.pi*self.轴径**3/16
        self.弯曲断面系数=np.pi*self.轴径**3/32
        self.弯曲应力=self.弯力矩/self.弯曲断面系数
        self.剪切应力=self.输入扭矩/self.剪切断面系数
        self.合成弯矩=0.5*self.弯力矩*(1+np.sqrt(1+(self.输入扭矩/self.弯力矩)**2))
        self.合成剪切力矩=self.弯力矩*np.sqrt(1+((self.输入扭矩/self.弯力矩)**2))
        self.合成曲应力=self.合成弯矩/ self.弯曲断面系数#小于9
        self.合成切应力=self.合成剪切力矩/self.剪切断面系数#小于7#这个计算和书本不一致
        return
if __name__=="__main__":
    测试=中间齿轮轴计算()
    测试.计算应力()
    测试=中间齿轮轴计算两点()
    测试.计算应力()