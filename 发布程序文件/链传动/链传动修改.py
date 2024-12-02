from excel公式python版本链传动 import IF,PulleyMass,ODD,yuce,monik8,nihejingtai,nihedongtai,nihemoca
from excel公式python版本链传动 import ROUND,CAprox
from math import *
import matplotlib
#matplotlib.use('TkAgg')  # 或者尝试其他后端，如 'Agg', 'GTK3Agg' 等
import matplotlib.pyplot as plt
    # 原始变量赋值，将值替换为相应的变量名
def 链轮计算(TeethOdd_1_value = 1,
    TeethOdd_2_value = 1,
    Lubrication_value = 1,
    LinksEven_value = 1,
    P1_value = 40,
    n1_value = 970,
    z1_value = 21,
    C_req_value = 40.18,
    ChLinks_value = 118,
    K1_value = 1,
    K2_value = 1.04761910438538,
    K3_value = 1,
    K4_value = 0.999113976955414,
    K5_value = 1,
    K6_value = 1,
    K7_value = 1,
    n2_req_value = 390,
    S_Units_value = True,
    Temperature_value = -39.9945102994005,
    Density_value = 7800,
    Life_value = 15000,
    K9_value = 1,
    X155_value = 1,
    Efficiency_value = 1,
    W165_value = 1 * 0.001,
    Chain_ex_value = 1,
    Chain_e_value = 1,
    Chain_s2_value = 1,
    Chain_s1_value = 1,
    Chain_g_value = 1,
    Chain_L_value = 1,
    Chain_d3_value = 1,
    Chain_d3_mm_value = 1,
    Chain_d1_value = 1,
    Chain_d1_mm_value = 1,
    Chain_b2_value = 1,
    Chain_b1_value = 1,
    RA_value = 2 ,
    Pitch_value = 1,
    rows_value = 4,
    PiMPa_value = 1,
    OddChLinksCoeff_value = 1,
    W208_value = 1,
    K8_value = 0.74,
    BArrea_value = 1,
    Massm_value = 1,
         G9=1,
         I9=1,
         _FB=1):

    # 使用变量名进行赋值
    _TeethOdd_1 = TeethOdd_1_value  # 链轮1齿数奇数标志
    _TeethOdd_2 = TeethOdd_2_value  # 链轮2齿数奇数标志
    _Lubrication = Lubrication_value  # 润滑类型
    _LinksEven = LinksEven_value  # 链节奇数偶数标志
    _P1 = P1_value  # 传递功率
    _n1 = n1_value  # 小链轮速度
    _z1 = z1_value  # 链齿轮齿数
    _C_req = C_req_value  # 需求轴向距离
    _ChLinks = ChLinks_value  # 链节数
    _K1 = K1_value  # 齿数系数
    _K2 = K2_value # 传动比系数
    _K3 = K3_value  # 冲击系数 (保险系数)
    _K4 = K4_value  # 轴距系数
    _K5 = K5_value  # 润滑系数
    _K6 = K6_value  # 温度系数
    _K7 = K7_value  # 寿命系数
    _n2_req = n2_req_value  # 链轮转速2
    S_Units = S_Units_value  # 单位标志
    _Temperature = Temperature_value  # 温度
    _Density = Density_value  # 密度
    _Life = Life_value  # 工作时间或寿命
    _K9 = K9_value  # 摩擦条件系数
    #X155 = X155_value  # 最大转速条件
    _Efficiency = Efficiency_value  # 链的效率
    W165 = W165_value  # 特定工作负载
    _Chain_ex = Chain_ex_value  # 链的某种特性或系数
    _Chain_e = Chain_e_value  # 链的某种特性或系数
    _Chain_s2 = Chain_s2_value  # 链的某种特性或系数
    _Chain_s1 = Chain_s1_value  # 链的某种特性或系数
    _Chain_g = Chain_g_value  # 链的某种特性或系数
    _Chain_L = Chain_L_value  # 链的某种特性或系数
    _Chain_d3 = Chain_d3_value  # 滚子直径
    _Chain_d3_mm = Chain_d3_value  # 滚子直径（毫米）
    _Chain_d1 = Chain_d1_value  # 销轴直径
    _Chain_d1_mm = Chain_d1_value   # 销轴直径（毫米）
    _Chain_b2 = Chain_b2_value  # 链的某种特性或系数
    _Chain_b1 = Chain_b1_value  # 链的某种特性或系数
    _RA = RA_value  # 小数点位数设置
    _Pitch = Pitch_value  # 链距
    _rows = rows_value  # 链数
    _PiMPa = PiMPa_value  # 轴承压力
    _OddChLinksCoeff = OddChLinksCoeff_value  # 奇数链节系数
    W208 = W208_value  # 特定工作负载
    _K8 = K8_value  # 链类型/摩擦系数
    _BArrea = BArrea_value  # 链承载面积
    _Massm = Massm_value  # 链轮质量
    _TemperatureC =IF(S_Units,_Temperature,5/9*(_Temperature-32))
    _D1 =_Pitch/sin(pi/_z1)
    N122 =IF(S_Units,_P1*9550/_n1,_P1*63000/_n1)
    _Pitch_i =IF(S_Units,_Pitch/25.4,_Pitch)
    _v =IF(S_Units,pi*_D1*_n1/60000,_D1*_n1/3.82)
    _Fu =IF(S_Units,_P1*1000/_v,_P1*33000/_v)
    _Fu_lbf =IF(S_Units,_Fu*0.22481,_Fu)
    X155=min(0.6, 0.3 + _Pitch_i / 2)
    W155 =1000*(82.5/((7.95**_Pitch_i)*(1.0278**_z1)*(1.323**(_Fu_lbf*0.001))))**(1/(1.59*log10(_Pitch_i)+1.873))
    W166 =ROUND((1.2*10000000*IF(S_Units,_P1,_P1*0.7457)/_n1)**0.333,1)/1000
    W143 =IF(int(_z1/2)>_z1/2,0,IF(_TeethOdd_1==1,1,0))
    _FB =_FB*_OddChLinksCoeff
    _C_optimal =40*_Pitch#推荐值轴向距离
    _alfa1_max =140-90/_z1
    _alfa1_min =120-90/_z1
    W180 =1/(15000/_Life)**0.4
    _rx =1.5*_Chain_d1
    _f =0.7*_Pitch
    _R1max =0.505*_Chain_d3+0.069*_Chain_d3_mm**0.33*IF(S_Units,1,1/25.4)
    _R1min =0.505*_Chain_d3_mm*IF(S_Units,1,1/25.4)
    _R2_1_min =0.12*_Chain_d3_mm*(_z1+2)*IF(S_Units,1,1/25.4)
    _R2_1_max =0.008*_Chain_d3_mm*(_z1**2+180)*IF(S_Units,1,1/25.4)
    S2 =_z1
    Q2 =_rx
    _Pitch_mm =_Pitch_i*25.4
    G2 =_Pitch
    _Chain_t =_Pitch

    _Pp =_P1*_K1*_K2*_K3*_K4*_K5*_K6*_K7#设计功率
    _P2 =_P1*_Efficiency/100
    _i_req =_n1/_n2_req
    N120 =_n1
    R2 =_f
    _da1_max =_D1+1.25*_Pitch-_Chain_d3
    _da1_min =_D1+0.5*_Chain_d3
    U2 =_D1
    _L =_ChLinks*_Pitch
    B2 =_ChLinks
    M2 =_Chain_s2
    L2 =_Chain_s1
    I2 =_Chain_L
    H2 =_Chain_g
    K2 =_Chain_ex
    J2 =_Chain_e
    X190 =_Chain_d3_mm/25.4
    X209 =_Chain_d3*0.15
    W209 =_Chain_d3*0.1
    D2 =_Chain_d3
    X189 =_Chain_d1_mm/25.4
    C2 =_Chain_d1
    F2 =_Chain_b2
    E2 =_Chain_b1
    _ba =(W209+X209)/2
    _dp1 =ROUND(_D1,_RA+1)
    AA143 =int(9+0.2*_Pitch_mm)
    X154 =_Massm*0.6723
    _v_m =IF(S_Units,_v,_v/196.8503937)
    _Fu =IF(S_Units,_P1*1000/_v,_P1*33000/_v)#张力有效圆周力
    _Fc =IF(S_Units,_Massm*_v**2,_Massm*0.6723*(_v**2)/115900)#惯性力
    W144 =_z1*_i_req
    _v_var_min =_v*cos(pi/_z1)
    P157 =_L*_Massm*IF(S_Units,0.001,0.0254/0.45359237)
    _Fr =_Fu+_Fc#链力有效圆周力
    _Safety_S =_FB/_Fr#静态安全系数
    _Safety_D =_FB/(_Fr*_K3)#动态安全系数
    P2 =_ba
    _Sigma =IF(S_Units,ROUND(_Fr/_BArrea,2),ROUND(_Fr/_BArrea,0))#计算压力
    Z144 =int(W144+0.5)
    X144 =int(W144)
    Y144 =IF(int(X144/2)!=X144/2,X144,X144+1)
    _z2 =IF(_TeethOdd_2==1,Y144,Z144)
    _i =_z2/_z1
    _i_1 =IF(_i<1,1/_i,_i)
    _K2_prop =CAprox('1;1.25; 2; 1.1; 3; 1; 5; 0.9; 7; 0.85; 12; 0.8; 100; 0.75', _i_1)
    W150 =2*_C_req/_Pitch+(_z1+_z2)/2+((_z2-_z1)/(2*pi))**2*_Pitch/_C_req
    _alfa2_max =140-90/_z2
    _alfa2_min =120-90/_z2
    _C =1/4*(_ChLinks-(_z2+_z1)/2+((_ChLinks-(_z2+_z1)/2)**2-(8*(_z2-_z1)**2/(4*pi**2)))**0.5)*_Pitch#中心距
    _R2_2_min =0.12*_Chain_d3_mm*(_z2+2)*IF(S_Units,1,1/25.4)
    N184 =0.02*_C
    _R2_2_max =0.008*_Chain_d3_mm*(_z2**2+180)*IF(S_Units,1,1/25.4)
    Z2 =_z2
    _v_var_max =_v/cos(pi/_z2)#链轮2最大最小速度
    _D2 =_Pitch/sin(pi/_z2)
    _n2 =_n1/_i
    _da2_max =_D2+1.25*_Pitch-_Chain_d3
    _da2_min =_D2+0.5*_Chain_d3
    AB2 =_D2
    _C_Pitch =_C/_Pitch
    _Y=_K3
    _K8=nihemoca( _i_1, _C_Pitch) * (1 / _Y)
    _PiMPa_cor =_PiMPa*_K9*_K8#许用压力
    _sigma_tbl =_PiMPa_cor*IF(S_Units,1,145.037)#许用压力
    _Safety_P =_sigma_tbl/_Sigma
    A2 =_C
    O186 =(_v_var_max-_v_var_min)/((_v_var_max+_v_var_min)/2)*100
    _dp2 =ROUND(_D2,_RA+1)
    X166 =ROUND((1.2*10000000*IF(S_Units,_P2,_P2*0.7457)/_n2)**0.333,1)/1000
    _SS_Z =min(_z1,_z2)
    _SS_RPM =max(_n1,_n2)
    Z150 =int(W150+0.5)
    X150 =int(W150/2+0.5)
    _AxisDist_min =IF(S_Units,ROUND((_D1+_D2)*0.7,0),ROUND((_D1+_D2)*0.7,1))
    _AxisDist_max= 160 * _Pitch
    P122 =IF(S_Units,_P2*9550/_n2,_P2*63000/_n2)
    X137 =IF(_C_req<_AxisDist_min,1,0)
    Y143 =32-2.5*_i
    Y182 =2.5-(_SS_Z-4)*((2.5-0.62)/44)
    Z182 =12.5-(_SS_Z-4)*((12.5-3)/44)
    X182 =1-(_SS_Z-4)*(0.72/44)
    Y150 =X150*2
    Y137 =X137
    _LubrRecPt =IF(_v_m<X182,1,IF(_v_m<Y182,2,IF(_v_m<Z182,3,4)))
    _ChLinks_prop =IF(_LinksEven==1,Y150,Z150)
    #W184 =IF(AND(_Lubrication>2, _LubrRecPt>2),1,0)
    #Y2 =_Dg1
    N211=0.7*_Pitch
    _Dg2 =_D2-2*N211
    _Dg1 =_D1-2*N211
    Z143=CAprox("1;13;20;25",_v_m)
    X143 =IF(_TeethOdd_1==1,ODD((Y143+Z143)/2-1),ROUND((Y143+Z143)/2,0))
    _bf =W208*_Chain_b1#链轮宽度
    W204=0.505*_Chain_d3_mm*IF(S_Units,1,1/25.4)
    X204=0.505*_Chain_d3+0.069*_Chain_d3_mm**0.33*IF(S_Units,1,1/25.4)
    _R1=ROUND((W204+X204)/2,_RA)
    _df2 =ROUND(_D2-_R1*2,_RA)
    _df1 =ROUND(_D1-_R1*2,_RA)
    Y206=120-90/_z2
    Z206=140-90/_z2
    _alfa2 =ROUND((Y206+Z206)/2,2)
    Y205=0.12*_Chain_d3_mm*(_z2+2)*IF(S_Units,1,1/25.4)
    Z205=0.008*_Chain_d3_mm*(_z2**2+180)*IF(S_Units,1,1/25.4)
    _R2_2 =ROUND((Y205+Z205)/2,_RA)
    W206=120-90/_z1
    X206=140-90/_z1
    _alfa1 =ROUND((W206+X206)/2,2)
    W205=0.12*_Chain_d3_mm*(_z1+2)*IF(S_Units,1,1/25.4)
    X205=0.008*_Chain_d3_mm*(_z1**2+180)*IF(S_Units,1,1/25.4)
    _R2_1 =ROUND((W205+X205)/2,_RA)
    _R1 =ROUND((W204+X204)/2,_RA)
    W202=_D2+0.5*_Chain_d3
    X202=_D2+1.25*_Pitch-_Chain_d3
    _da2 =ROUND((W202+X202)/2,_RA)
    W201=_D1+0.5*_Chain_d3
    X201=_D1+1.25*_Pitch-_Chain_d3
    _da1 =ROUND((W201+X201)/2,_RA)
    _v_max =round(IF(S_Units,W155/60*(_D1*pi)/1000,W155*(_D1*pi)*0.0833333)*X155,2)
    X167 =IF(S_Units,_df2/1000,_df2*25.4/1000)
    W167 =IF(S_Units,_df1/1000,_df1*25.4/1000)
    X140 =IF(IF(S_Units,pi*_D1*_n1/60000,_D1*_n1/3.82)<_v_max,1,0)
    X167 =IF(S_Units,_df2/1000,_df2*25.4/1000)
    W167 =IF(S_Units,_df1/1000,_df1*25.4/1000)
    W167=IF(S_Units,_df1/1000,_df1*25.4/1000)
    W168=PulleyMass(W167,W166,W165,W165/4,_Density)
    X168=PulleyMass(X167,X166,W165,W165/4,_Density)
    _SumMass =(W168+X168)*IF(S_Units,1,2.2406)+P157#总功率
    _K4_prop =CAprox('20;1.2;40;1;60;0.9;80;0.85;160;0.7;1000;0.7',_C_Pitch)
    _K1_prop =CAprox('1;2.5;7;2.3;9;2;11;1.7;13;1.45;15;1.3;17;1.1;19;1;21;0.9;23;0.85;25;0.75;30;0.7;100;0.6',_SS_Z)
    Z143 =CAprox('1;13;20;25',_v_m)
    _K5_prop =CAprox('1;1;2;1.5;3;2.5;4;5',_Lubrication)
    _K2_prop =CAprox('1;1.25;2;1.1;3;1;5;0.9;7;0.85;12;0.8;100;0.75',_i_1)
    _K6_prop =CAprox('0;1;90;1;170;1.1;260;1.2;500;1.5',_TemperatureC)
    #profile=1
    x155_prop=min(0.6,0.3+_Pitch_i/2)
    w208_prop=IF(_Pitch_mm < 12.7, CAprox("1;0.93;2;0.91;3;0.88;4;0.85;10;0.85", _rows),
        CAprox("1;0.95;2;0.93;3;0.93;4;0.9;10;0.9", _rows))
    import pandas as pd
    #链数据 = pd.read_excel(r'D:\程序文件\24-1-20程序\mechanical-calculation-4\程序文件\链传动\链型.xlsx')
    G9=G9#需要选择
    K9=1.06
    L9=0.9
    M9=3.25
    N9=0.11
    I9=I9#需要选择
    O9=1.6
    P9=0.38
    Q9=0.4
    h7_prop=G9 * _SS_Z ** K9 * _SS_RPM ** L9 * (_Pitch_i ** (M9 - N9 * _Pitch_i)) * 0.7457
    j9_prop=1000 * (I9 * (_SS_Z / _SS_RPM) **O9 * _Pitch_i **P9 * (15000 / _Life) ** Q9) * 0.7457
    _MultipleStrand = CAprox('1;1;2;1.7;3;2.5;4;3.3;5;3.9;6;4.6;8;6', _rows)
    _PpTable=min(h7_prop,j9_prop** _MultipleStrand)
    _OddChLinksCoeff_prop=IF(int(_ChLinks / 2) !=_ChLinks / 2, 0.8, 1)
    #_v_m=3.25
    轴承压力 = yuce( _SS_Z, _v_m)
    print(_SS_Z,_v_m,轴承压力)
    k8_prop=monik8(_i_1,_C_Pitch)
    #k4_prop=CAprox("20;1.2;40;1;60;0.9;80;0.85;160;0.7;1000;0.7", _C_Pitch)
    _Safety_Smin=nihejingtai(_Pitch_mm,_v_m)
    _Safety_Dmin=nihedongtai(_Pitch_mm, _SS_RPM)
    结果字典 = {
            'TeethOdd_1链轮1齿数奇数标志': (_TeethOdd_1, ''),
            'TeethOdd_2链轮2齿数奇数标志': (_TeethOdd_2, ''),
            'Lubrication润滑类型': (_Lubrication, ''),
            'LinksEven链节奇数偶数标志': (_LinksEven, ''),
            'P1传递功率': (_P1, ''),
            'n1小链轮速度': (_n1, ''),
            'z1链齿轮齿数': (_z1, ''),
            'z2链齿轮齿数': (_z2, ''),
            'K1': (_K1_prop, ''),
            '_SS_Z': (_SS_Z, ''),
            'Y144': (Y144, ''),
            'Z144': (Z144, ''),
            'C_req需求轴向距离': (_C_req, ''),
            'ChLinks链节数': (_ChLinks, ''),
            'K1齿数系数': (_K1, ''),
            'K2传动比系数': (_K2, ''),
            'K3冲击系数 (保险系数)': (_K3, ''),
            'K4轴距系数': (_K4, ''),
            'K5润滑系数': (_K5, ''),
            'K6温度系数': (_K6, ''),
            'K7寿命系数': (_K7, ''),
        'K8摩擦系数': (_K8, ''),
            'n2_req链轮转速2': (_n2_req, ''),
            'S_Units单位标志': (S_Units, ''),
            'Temperature温度': (_Temperature, ''),
            'Density密度': (_Density, ''),
            'Life工作时间或寿命': (_Life, ''),
            'K9摩擦条件系数': (_K9, ''),
            'X155最大转速条件': (X155, ''),
            'Efficiency链的效率': (_Efficiency, ''),
            'W165特定工作负载': (W165, ''),
            'Chain_ex': (_Chain_ex, ''),
            'Chain_e': (_Chain_e, ''),
            'Chain_s2': (_Chain_s2, ''),
            'Chain_s1': (_Chain_s1, ''),
            'Chain_g': (_Chain_g, ''),
            'Chain_L': (_Chain_L, ''),
            'Chain_d3滚子直径': (_Chain_d3, ''),
            'Chain_d3_mm滚子直径（毫米）': (_Chain_d3_mm, ''),
            'Chain_d1销轴直径': (_Chain_d1, ''),
            'Chain_d1_mm销轴直径（毫米）': (_Chain_d1_mm, ''),
            'Chain_b2': (_Chain_b2, ''),
            'Chain_b1': (_Chain_b1, ''),
            'RA小数点位数设置': (_RA, ''),
            'Pitch链距': (_Pitch, ''),
            'rows链数': (_rows, ''),
            'PiMPa轴承压力': (_PiMPa, ''),
            'OddChLinksCoeff奇数链节系数': (_OddChLinksCoeff, ''),
            'W208特定工作负载': (W208, ''),
            'K8链类型/摩擦系数': (_K8, ''),
            'BArrea链承载面积': (_BArrea, ''),
            'Massm链轮质量': (_Massm, ''),
            'Power capacity (link plate)': (h7_prop, ''),
            'Power capacity (Bushing)': (j9_prop, ''),
            'G9': (G9, ''),
            'I9': (I9, ''),
            '_SS_RPM': (_SS_RPM, ''),
            '_Pitch_i': (_Pitch_i, ''),
            '_Pitch_mm': (_Pitch_mm, ''),
            ' _Life': ( _Life, ''),
            '_bf': (_bf, ''),
        '_K9': (_K9, ''),
            '_P1': (_P1, ''),
        '_C_optimal': (_C_optimal, ''),
            '_C_Pitch': (_C_Pitch, ''),
        '_K5': (_K5, ''),
        '链速_v': (_v, ''),
        '最大链速': (_v_max, ''),
        '设计功率_Pp': (_Pp, ''),
        '许用功率': (_PpTable, ''),
    '静态安全_Safety_S': (_Safety_S, ''),
        '_Safety_Smin': (_Safety_Smin, ''),
    '动态安全_Safety_D': (_Safety_D, ''),
        '_Safety_Dmin': (_Safety_Dmin, ''),
    '设计压力_Sigma': (_Sigma, ''),
        '许用压力': (_sigma_tbl, ''),
    '安全等级_Safety_P>1': (_Safety_P, ''),
    '_FB': (_FB, ''),
    '链力_FR': (_Fr, ''),
    '链节距_D1': (_D1, ''),
    '_l链长': (_L, ''),}

    return _Sigma,_Pp,_Fu,_Fc,结果字典,轴承压力,w208_prop,\
           _OddChLinksCoeff_prop,k8_prop,_K1_prop,_K2_prop,_K4_prop,_K5_prop,\
           _K6_prop,_K8,_ChLinks_prop,_C_optimal
if __name__ == '__main__':
    链轮计算()

