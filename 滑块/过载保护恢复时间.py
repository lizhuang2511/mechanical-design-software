import numpy as np
class 过负荷防止装置():
    def __init__(self):
        self.油缸直径=585
        self.行程=30
        self.油缸数=1
        self.吐出量=72
    def 计算(self):
        self.体积=(np.pi/4)*(self.油缸直径)**2*self.油缸数*self.行程*0.001
        self.t=self.体积*60/self.吐出量*0.001

        return
if __name__ == "__main__":
    测试=过负荷防止装置()
    测试.计算()