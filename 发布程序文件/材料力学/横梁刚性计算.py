import numpy as np
class 横梁刚性计算左右():
    def __init__(self):
        self.上板宽度=400
        self.上板高度=60
        self.下板宽度=1330
        self.下板高度=40
        self.中间板高度=2590
        self.中间板宽度=80
        self.导柱间距=3200
        self.拉紧螺栓间距=5120
        self.载荷=300000
    def 横梁刚性计算(self):
        self.断面积计算=self.上板宽度*self.上板高度+self.下板宽度*self.下板高度+(self.中间板高度-self.上板高度-self.下板高度)*self.中间板宽度
        self.中性轴位置=(self.中间板宽度*self.中间板高度**2+(self.下板宽度-self.中间板宽度)*self.下板高度**2+ \
                    (self.上板宽度-self.中间板宽度)*self.上板高度*(2*self.中间板高度-self.上板高度))/2/self.断面积计算
        self.断面二次矩=(self.上板宽度*(self.中间板高度-self.中性轴位置)**3-(self.上板宽度-self.中间板宽度)*(self.中间板高度-self.中性轴位置-self.上板高度)**3 \
                    +self.下板宽度*self.中性轴位置**3-(self.下板宽度-self.中间板宽度)*(self.中性轴位置-self.下板高度)**3)/3
        self.拉应力=(self.载荷*(self.拉紧螺栓间距-self.导柱间距)/2)*(self.中间板高度-self.中性轴位置)/self.断面二次矩
        self.压应力=(self.载荷*(self.拉紧螺栓间距-self.导柱间距)/2)*self.中性轴位置/self.断面二次矩
        self.剪切系数=(self.断面积计算*(self.中间板宽度*(self.中性轴位置-self.下板高度)**2+ \
                               self.下板宽度*(self.中性轴位置**2-(self.中性轴位置-self.下板高度)**2)))/2/self.中间板宽度/self.断面二次矩
        self.剪切应力=self.剪切系数*self.载荷/self.断面积计算
        self.弯曲变形=((self.载荷*((self.拉紧螺栓间距-self.导柱间距)/2))*(3*self.拉紧螺栓间距**2-4*((self.拉紧螺栓间距-self.导柱间距)/2)**2)/24/21000/self.断面二次矩)
        self.剪切变形=self.剪切系数*(self.载荷*(self.拉紧螺栓间距-self.导柱间距)/2)/8100/self.断面积计算
        self.总变形=self.弯曲变形+self.剪切变形
        self.最大变形率=self.总变形*1000/self.拉紧螺栓间距
        print(self.最大变形率)
        print(self.拉紧螺栓间距/self.总变形)
        return
if __name__=="__main__":
    测试=横梁刚性计算左右()
    测试.横梁刚性计算()