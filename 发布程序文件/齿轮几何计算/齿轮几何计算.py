import numpy as np
from decimal import Decimal
from math import *
class 齿轮精度计算():
    def __init__(self):
        self.m=10;self.alf=20;self.z1=98;self.z2=15;
        self.x1=0;self.x2=0.5162;
        self.au=0.05;
        self.ai=0;
        self.螺旋角=15
    def 渐开线函数(self):
        self.inva=np.tan(np.deg2rad(self.alf))-np.deg2rad(self.alf)
        self.invαb = np.tan(np.deg2rad(self.alf)) - np.deg2rad(self.alf) + 2 * np.tan(np.deg2rad(self.alf)) * (
                    (self.x1 + self.x2) / (self.z2 + self.z1))
        #print(invα)
        a1 = 1 + (self.invαb - np.tan(1) + 1) / np.tan(1) ** 2
        for i in range(7):
            a1 = a1 + (self.invαb - np.tan(a1) + a1) / np.tan(a1) ** 2
        self.alfb = np.rad2deg(a1)
        return
    def 垮齿厚(self,zm1=0,zm2=0):
        alf=np.deg2rad(self.alf)
        alfb=np.deg2rad(self.alfb)
        self.y=(self.z1+self.z2)/2*(np.cos(alf)/np.cos(alfb)-1)#中心距增加系数
        self.ax=((self.z1+self.z2)/2+self.y)*self.m#中心距
        self.d1=self.z1*self.m;self.d2=self.z2*self.m#分度圆
        #self.zv1=self.计算zv(螺旋角=self.螺旋角,压力角=self.alf,z=self.z1)
        #self.zv2=self.计算zv(螺旋角=self.螺旋角,压力角=self.alf,z=self.z2)
        f1=self.x1/self.z1;f2=self.x2/self.z2
        self.kf1=1/np.pi*((1/np.cos(alf))*np.sqrt((1+2*f1)**2-np.cos(alf)**2)-self.inva-2*f1*np.tan(alf))
        self.kf2=1/np.pi*((1/np.cos(alf))*np.sqrt((1+2*f2)**2-np.cos(alf)**2)-self.inva-2*f2*np.tan(alf))

        self.zm1=self.kf1*self.z1+0.5;self.zm2=self.kf2*self.z2+0.5
        self.zm1=int(Decimal(str(self.zm1)).quantize(Decimal("1."),rounding="ROUND_HALF_UP"))
        self.zm2 = int(Decimal(str(self.zm2)).quantize(Decimal("1."), rounding="ROUND_HALF_UP"))
        self.sm1=self.m*np.cos(alf)*(np.pi*(self.zm1-0.5)+self.z1*self.inva)+2*self.x1*self.m*np.sin(alf)
        self.sm2 = self.m * np.cos(alf) * (
                    np.pi * (self.zm2 - 0.5) + self.z2 * self.inva) + 2 * self.x2 * self.m * np.sin(alf)
        return
    def 齿侧间隙(self):
        alf = np.deg2rad(self.alf)
        self.B=0.02*self.m
        self.w1=np.power(self.d1,1/3)+0.65*self.m
        self.w2 = np.power(self.d2,1/3) + 0.65 * self.m
        self.k=-((self.B-(self.au+self.ai)*np.sin(alf))/(self.w1+self.w2))*1000-1
        self.su1=(self.k+2)*self.w1/1000;self.su2=(self.k+2)*self.w2/1000#跨齿厚公差
        self.si1 = (self.k) * self.w1 / 1000;self.si2 = (self.k) * self.w2 / 1000  # 跨齿厚公差下
        self.bu=-(self.si1+self.si2)+2*self.au*np.sin(alf)
        self.bi=-(self.su1+self.su2)+2*self.ai*np.sin(alf)
        self.BC=(self.bu+self.bi)/2
        return
    def 重合度(self):
        alf = np.deg2rad(self.alf)
        alfb = np.deg2rad(self.alfb)
        self.dz1=self.d1*np.cos(alf);self.dz2=self.d2*np.cos(alf)
        self.db1=self.dz1/np.cos(alfb);self.db2=self.dz2/np.cos(alfb);
        self.hk1=(1+self.y-self.x2)*self.m;self.hk2=(1+self.y-self.x1)*self.m;
        self.h=(2.25+self.y-(self.x1+self.x2))*self.m
        self.dk1=self.d1+2*self.hk1;self.dk2=self.d2+2*self.hk2;
        self.dr1=self.dk1-2*self.h;self.dr2=self.dk2-2*self.h;
        self.yebx=(np.sqrt((self.dk1/2)**2-(self.dz1/2)**2)+np.sqrt((self.dk2/2)**2-(self.dz2/2)**2)-self.ax*np.sin(alfb))/(np.pi*self.m*np.cos(alf))#重合度
        self.g=(np.sqrt((self.dk1/2)**2-(self.dz1/2)**2)+np.sqrt((self.dk2/2)**2-(self.dz2/2)**2)-self.ax*np.sin(alfb))#啮合线长度
        return
    def 校核啮合角(self):
        alf=np.deg2rad(self.alfb)
        self.alfc=np.tan(alf)-alf
        return
    def 数据处理(self):
        self.sm1=round(self.sm1,4);self.sm2 = round(self.sm2, 4);
        self.su1 = round(self.su1, 4);self.su2= round(self.su2, 4);
        self.si1=round(self.si1,4);self.si2 = round(self.si2, 4);
        self.bu = round(self.bu, 4);self.bi = round(self.bi, 4);
        self.ax=round(self.ax,4);self.yebx = round(self.yebx, 4);
        return
    def 计算k(self,螺旋角=15,压力角=20,z=130,xn=0,模数=14):
        压力角=np.deg2rad(压力角)
        螺旋角 = np.deg2rad(螺旋角)
        at=np.arctan(np.tan(压力角)/np.cos(螺旋角))
        betb=np.arccos(np.cos(螺旋角)*np.cos(压力角)/np.cos(at))
        zv=z/(np.cos(betb)**2*np.cos(螺旋角))
        #zv = z / (np.cos(螺旋角) ** 2 * np.cos(螺旋角))
        anh=压力角
        bath=螺旋角
        invan = tan(anh) - anh;
        # 计算跨齿数和公法线长度
        ath = atan(tan(anh) / cos(bath));
        invan = tan(anh) - anh;
        invat = tan(ath) - ath;
        zp = z * invat / invan;
        if xn==0:
            k=round(压力角/np.pi*zp+0.5)
        else:
            k=round(zv/np.pi*np.arccos(zv*np.cos(压力角)/(zv+2*xn))+0.5)
        Mn=模数
        wxx=cos(anh) * (pi * (k - 0.5) + zp * invan);
        detw=sin(anh)*2*xn
        Wkn = Mn * (wxx+detw)
        print('跨齿数',k,'公法线',Wkn )
        return k,Wkn
    def 最小侧间隙计算(self,中心距=1050.8,模数=14,压力角=20,中心距偏差=-0.05,jn=0,Ebns1u=0.05,Ebns1d=0.05,Ebns2u=0.05,Ebns2d=0.05):
        压力角 = np.deg2rad(压力角)
        #jbmin=abs(-2/3*(0.06+0.0005*abs(中心距)+0.03*模数)-中心距偏差*2*np.tan(压力角)*np.cos(压力角)+jn)
        jbmin = abs(-2 / 3 * (0.06 + 0.0005 * abs(中心距) + 0.03 * 模数))
        Esns1u=Ebns1u/cos(压力角)
        Esns2u=Ebns2u/cos(压力角)
        Esns1d = Ebns1d/cos(压力角)
        Esns2d = Ebns2d/cos(压力角)
        tsn1=Esns1d-Esns1u
        tsn2=Esns2d-Esns2u
        jbn=abs(Esns1u+Esns1u)*cos(压力角)-jn
        jbnmax=abs(Esns1d+Esns1d)*cos(压力角)+中心距偏差*2*np.tan(压力角)*np.cos(压力角)-jn
        print(jbmin,jbn,jbnmax,tsn1,tsn2)
        return
if __name__ == "__main__":
    测试=齿轮精度计算()
    测试.渐开线函数()
    测试.垮齿厚()
    测试.校核啮合角()
    测试.齿侧间隙()
    测试.重合度()
    a=测试.计算k(螺旋角=25,压力角=20,z=56,xn=0,模数=22)
    print(a)
    测试.最小侧间隙计算(中心距=1050.8, 模数=14, 压力角=20, 中心距偏差=0.05, jn=0, Ebns1u=-0.20, Ebns1d=-0.250, Ebns2u=-0.11, Ebns2d=-0.16)
