import numpy as np
class 过载保护口径计算():
    def __init__(self):
        self.油缸直径=457
        self.油缸数量=2
        self.油缸行程=25
        self.下死点25mm速度=510
        self.配管内径=67.9
    def 计算(self):
        self.体积=np.pi/4*self.油缸直径**2*self.油缸行程*0.00000001*self.油缸数量
        self.平均速度=self.下死点25mm速度/2
        self.回复时间=self.油缸行程/self.平均速度
        self.配管面积=np.pi/4*self.配管内径**2*0.0001
        self.流速=self.体积/self.配管面积/self.回复时间#小于4M/s
        return
if __name__=="__main__":
    测试=过载保护口径计算()
    测试.计算()