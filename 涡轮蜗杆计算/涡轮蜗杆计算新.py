from excel公式python版本涡轮蜗杆 import IF
from excel公式python版本涡轮蜗杆 import INDEX,CHOOSE,OR,LOG,LN,ROUND,AND,CellTransmitVal,T_Lubrication,INDEX2
from math import *
import pandas as pd
def 计算涡轮(_PoweredWoWh=1,_Pw2_Input=3.7,_n1=900,_iin=50,F122=1,_MatP=32,_MatW=7,
_ToothType=1,_LoadTypeA=1,_LoadTypeB=1,_DesignCooling=3,_OilType=1,
_Lubricant=2,_ny100=9,_ny40=46,_rooil15_Input=1.035,_Ra_Input=0.5,_KA=1.85,
_Lh=25000,_Sd_Proposal=1,_SH_proposal=1,_SF_Proposal=1.1,_SW_proposal=1.1,
_haXP=1,_caXP=0.25,_rf1=0.379950841145184,_z1_from=1,_z1_to=3,
_SortTbl=13,_z1=1,_Alfa0ID=1,_d1_Input=50,_alfa_temp=20,
_gama=5.7106,_gamaProp=3,_q=10,P163=45102,_calc_q=1,
_TeethOrientation=1,_m_Input=5,_Module=5,_l1_proc=50,_l2_proc=50,
_x2=0,_a_req1_Input=150,_FitAxis=3,_l1_input=123.373216981801,_l2_input=123.373216981801,
_L_Input=45,_b2H_Input=45,_de2Input=45,涡轮外径判断值=False,_BearingType=2,_deltaWlimn_Input=0.599999999999999
,判断齿侧允许磨损=False,_SKInput=4.05,轮缘厚度输入判断值=False,_YNL=1,_AG=1,_theta0_Input=20,_thetaSlimInput=90,齿轮箱的极端温度油判断=False,
_Cooling1=1,_thetaReqInput=81.8181818181818,目标最大齿轮箱温度油判断值=False,_GboxAreaType=4,_AgesInput=0.51695678054951,齿轮箱表面判断值=False,
_k_Input=43.266417139886,热传导效率判断值=False,_PK1_Input=0,油冷却能量如果使用判断值=False,_Cooling2=2,_dthetaS_Input=3,_coil_Input=1900,
_Qoil=0.028188110386212,_CastType=3,S_Units=True,_Diam_q_from=1,_Diam_q_to=18):



        #附加部分
        _z1_req=1#蜗杆/蜗轮 齿数z1, z2
        _z2_req=50#蜗杆/蜗轮 齿数z1, z2
        _a_req=180#目标圆心距a[mm]
        _XX_z1=2#用齿数来进行传动率计算z1,z2  i
        _XX_Mk2=300#用小齿轮速度和扭矩进行功率计算Mk2,n2Pw2
        _XX_n1=1600#用速度来进行传动比计算n1,n2  i
        _Shaft_th=0.5#轴肩(直径,宽度)ds, t[mm]
        _Shaft_ds=33#轴肩(直径,宽度)ds, t[mm]#选择输入
        _DXF_Beta=10#蜗轮收缩角b[ ° ]
        _XX_n2=3.75#用小齿轮速度和扭矩进行功率计算Mk2,n2Pw2
        _AxisDist=7#辅助计算选择蜗杆

        #其他意义
        S_HRA00=0#展开和不展开
        S_HRB00=0#展开和不展开
        S_HRC00=0#展开和不展开
        B149=True
        B325=True
        B327=True
        B419=True
        B423=True
        _coilFlag=True
        _YNLFlag=True
        _l1l2_flag=True
        X141=True
        X142=True
        X143=True
        X144=True#方框选项
        P409=80#用速度来进行传动比计算n1,n2  i
        _DIN_Version=1#DIN标准对应计算方法
        _UnitPT=2#单位选择
        _GboxDensity=7250#铁的密度
        #H414=1#图纸输出选项
        #H427=1#图纸输出选项
        AA336=0.5
        AA337=1#循环值
        AA338=2
        AA339=5#要注意
        AA340=10
        AA341=20
        AA342=50
        AA343=100
        AA344=200
        AI309=0.2
        AI310=0.5
        AI311=1#缺失值

        #未解析部分
        T379=-2#关注这个值的变化
        _x1=0#蜗轮齿顶修正系数x [modul]
        #_ZeroValue=0
        P271=0#抬高系数/每小时开始数WNS
        #U316=0#单位表示
        X173=5#要注意
        X350=0.15#常数值
        P408=41#用齿数来进行传动率计算z1,z2  i
        AA298=50#缺失值
        AE309=50#缺失值
        _IDTblMax=54
        AC298=100#缺失值
        #D403=1
        moveval=13#函数名
        #Y309=1#常数值
        #F395=15
        #F396=15
        #F402=15


        #AG152=1
        #W421 =1#XM_Material & ": " &INDEX(材料!E7:E57,_MatP)

        #H413 =S_DXFOutPt
        #X418 =S_BOMInfo
        #P148 =P147#动力头间隙c*      [modul]
        #P150 =P147#齿根半径系数rf*      [modul]
        #计算过程
        #_x_srollbar =X173/10-0.5
        #T_Results='T_Results'#涡轮型号#这是一个数据表
        #_SafetySumBool =OR(X141,X144)
        _WNS =min(1+0.015*P271,4)#抬高系数/每小时开始数WNS
        _Zh =min((25000/_Lh)**(1/6),1.6)#寿命因数Zh
        _z2 =int(_iin*_z1+0.5)
        #_q_Results =INDEX(T_Results,_Results,6)
        #_i_Results =INDEX(T_Results,_Results,4)
        #_alfa_Results =INDEX(T_Results,_Results,21)
        #_x2_Results =INDEX(T_Results,_Results,20)
        #_z1_Results =INDEX(T_Results,_Results,2)
        T_OilType='T_OilType'#这是一个数据表
        _kp =INDEX(T_OilType,_OilType,4)
        _calfa =INDEX(T_OilType,_OilType,3)#恒量的,用于代替粘度指数ca  [m**2/N]
        _Zoil =INDEX(T_OilType,_OilType,2)#润滑因数Zoil
        T_Module='T_Module'#这是一个数据表
        _mn_fromtable =INDEX(T_Module,_Module,1)
        T_MatTblWorm='T_MatTblWorm'#这是一个数据表
        _Poison1 =INDEX(T_MatTblWorm,_MatP,69)#损坏率
        _E1 =INDEX(T_MatTblWorm,_MatP,67)#杨氏模量(弹性模数)E[GPa]
        _qF1 =INDEX(T_MatTblWorm,_MatP,66)#弯曲疲劳说明线图qF
        _qH1 =INDEX(T_MatTblWorm,_MatP,65)#接触疲劳说明线图qH
        _NFLim1 =INDEX(T_MatTblWorm,_MatP,64)*1000000#弯曲负荷循环基数NFlim
        _NHLim1 =INDEX(T_MatTblWorm,_MatP,63)*1000000#接触负荷循环基数NHlim
        _BendingLimit1 =INDEX(T_MatTblWorm,_MatP,61)#弯曲疲劳极限SFlim[MPa]
        _ContactLimit1 =INDEX(T_MatTblWorm,_MatP,59)#接触疲劳极限SHlim[MPa]
        _VHV1 =INDEX(T_MatTblWorm,_MatP,58)#齿的边缘硬度VHV[HV]
        O388 =INDEX(T_MatTblWorm,_MatP,57)#齿的中心硬度JHV[HV]
        O383 =INDEX(T_MatTblWorm,_MatP,55)#抗张强度-收缩率Rp0.2[MPa]
        O382 =INDEX(T_MatTblWorm,_MatP,53)#抗张强度-极限Rm[MPa]
        _Ro1 =INDEX(T_MatTblWorm,_MatP,49)#密度Ro[kg/m**3]
        T_MatTblWheel='T_MatTblWheel'#这是一个数据表
        _YNL_Proposal =INDEX(T_MatTblWheel,_MatW,75+_AG)
        #_YNL=_YNL_Proposal
        _TauFlimT =INDEX(T_MatTblWheel,_MatW,75)
        _sigmaHlimT =INDEX(T_MatTblWheel,_MatW,74)
        _YW =INDEX(T_MatTblWheel,_MatW,73)#材料因数YW
        _WML =INDEX(T_MatTblWheel,_MatW,69+_OilType)#材料/润滑剂因数 - 磨损WML
        _Poison2 =INDEX(T_MatTblWheel,_MatW,69)#损坏率
        _E2 =INDEX(T_MatTblWheel,_MatW,67)#杨氏模量(弹性模数)E[GPa]
        _qF2 =INDEX(T_MatTblWheel,_MatW,66)#弯曲疲劳说明线图qF
        _qH2 =INDEX(T_MatTblWheel,_MatW,65)#接触疲劳说明线图qH
        _NFLim2 =INDEX(T_MatTblWheel,_MatW,64)*1000000#弯曲负荷循环基数NFlim
        _NHLim2 =INDEX(T_MatTblWheel,_MatW,63)*1000000#接触负荷循环基数NHlim
        _BendingLimit2 =INDEX(T_MatTblWheel,_MatW,61)#弯曲疲劳极限SFlim[MPa]
        _ContactLimit2 =INDEX(T_MatTblWheel,_MatW,59)#接触疲劳极限SHlim[MPa]
        _VHV2 =INDEX(T_MatTblWheel,_MatW,58)#齿的边缘硬度VHV[HV]
        P388 =INDEX(T_MatTblWheel,_MatW,57)#齿的中心硬度JHV[HV]
        P383 =INDEX(T_MatTblWheel,_MatW,55)#抗张强度-收缩率Rp0.2[MPa]
        P382 =INDEX(T_MatTblWheel,_MatW,53)#抗张强度-极限Rm[MPa]
        _MatTypeW =INDEX(T_MatTblWheel,_MatW,51)
        _Ro2 =INDEX(T_MatTblWheel,_MatW,49)#密度Ro[kg/m**3]
        T_DesignCooling='T_DesignCooling'#这是一个数据表
        位置1=int(float(INDEX(T_DesignCooling,_DesignCooling,2)))
        _LubricationIndex =int(float(位置1+_OilType))
        #_LubricationIndex
        print(_LubricationIndex)
        #T_Lubricant='T_Lubricant'#这是一个数据表
        #T_Lubrication='T_Lubrication'#这是一个数据表

        #_ny100_tbl =INDEX(T_Lubricant,_Lubricant,4)
        #_ny40_tbl =INDEX(T_Lubricant,_Lubricant,3)
        #_rooil15_tbl =INDEX(T_Lubricant,_Lubricant,2)
        T_KAcoef='T_KAcoef'#这是一个数据表
        #_KA_Prop =INDEX(T_KAcoef,_LoadTypeA,_LoadTypeB)#运用因素KA
        T_i='T_i'
        _iin_fromtable =INDEX(T_i,F122,2)
        T_gamaProp='T_gamaProp'#这是一个数据表
        _gamaFromTbl =INDEX(T_gamaProp,_gamaProp,1)
        T_DXFTablesList='T_DXFTablesList'#这是一个数据表
        #_DXF_TblOutName =INDEX(T_DXFTablesList,H427,2)
        T_DXFScale='T_DXFScale'#这是一个数据表
        #S_DXFScale =INDEX(T_DXFScale,H414,2)
        T_CastType='T_CastType'#这是一个数据表
        Y351 =INDEX(T_CastType,_CastType,2)
        T_AxisDist='T_AxisDist'#这是一个数据表
        _x2_axis2 =INDEX(T_AxisDist,_AxisDist,7)
        _q_axis2 =INDEX(T_AxisDist,_AxisDist,6)
        _DP_axis2 =INDEX(T_AxisDist,_AxisDist,5)
        _m_axis2 =INDEX(T_AxisDist,_AxisDist,4)
        _i_axis2 =INDEX(T_AxisDist,_AxisDist,3)/INDEX(T_AxisDist,_AxisDist,2)
        _z1_axis2 =INDEX(T_AxisDist,_AxisDist,2)
        T_Alfa0='T_Alfa0'#这是一个数据表
        _Alfa0fromTbl =INDEX(T_Alfa0,_Alfa0ID,1)
        #L168 =IF(S_Units,XM_2031,XM_2032)
        #L167 =IF(S_Units,XM_0032,XM_0020)
        #_m_Results =IF(S_Units,INDEX(T_Results,_Results,7),25.4/INDEX(T_Results,_Results,7))
        M167 =IF(S_Units,IF(_ToothType==1,"mx","mn"),"DP")
        _dthetaS_prop =IF(S_Units,IF(_Cooling2==1,15,3),IF(_Cooling2==1,27,5.4))
        _thetaSlimProp =IF(S_Units,CHOOSE(_OilType,90,100,110),CHOOSE(_OilType,194,212,230))
        _thetaSlimInput=CellTransmitVal(_thetaSlimProp,_thetaSlimInput,齿轮箱的极端温度油判断)
        _thetaSlim =IF(S_Units,_thetaSlimInput,(_thetaSlimInput-32)/9*5)
        _thetaReqProposal =IF(S_Units,(_thetaSlim/1.1),((_thetaSlim/1.1))/5*9+32)
        _thetaReqInput=CellTransmitVal(_thetaReqProposal,_thetaReqInput,目标最大齿轮箱温度油判断值)
        _thetaReq =IF(S_Units,_thetaReqInput,(_thetaReqInput-32)/9*5)
        _coilProp =IF(S_Units,1900,1900*0.000238844709019669)
        _theta0 =IF(S_Units,_theta0_Input,(_theta0_Input-32)/9*5)
        _rooil15 =IF(S_Units,_rooil15_Input,_rooil15_Input/62.4278178356276)
        _Ra =IF(S_Units,_Ra_Input,_Ra_Input/25.4)
        _Pw2 =IF(S_Units,_Pw2_Input,_Pw2_Input* 0.745701033541632)
        _m_temp =IF(S_Units,_m_Input,25.4/_m_Input)
        _L =IF(S_Units,_L_Input,_L_Input*25.4)
        _dthetaS =IF(S_Units,_dthetaS_Input,(_dthetaS_Input)/9*5)

        _d1 =IF(S_Units,_d1_Input,_d1_Input*25.4)
        _coil =IF(S_Units,_coil_Input,_coil_Input/0.000238844709019669)
        _b2H =IF(S_Units,_b2H_Input,_b2H_Input*25.4)


        B422 =IF(B423,1,0)
        B418 =IF(B419,1,0)
        C149 =IF(B149,1,0)
        C327 =IF(_DesignCooling==3 and B327==False,1,0)
        C325 =IF(_DesignCooling==3 and B325==False,1,0)
        C326 =IF(_DesignCooling==3 and _coilFlag==False,1,0)
        G2 =IF(_z1==1,0.001,360)
        F2 =IF(_z1<2,2,_z1)
        print(F2)
        Z255 =0.94+0.25*_z2/_z1+6.7/tan(_gama*pi/180)
        Y255 =0.78+0.21*_z2/_z1+5.6/tan(_gama*pi/180)
        _s_x =IF(_ToothType==5,Z255,Y255)
        #L162 =IF(_ToothType==1,XM_2006,XM_2005)
        Y176 =_a_req1_Input*2/(_q+_z2+2*_x2)
        O176 =_a_req1_Input#所需圆心距 / 当前的a [mm]
        Z176 =2*_a_req1_Input/(_z1/sin(_gama*pi/180)+_z2/cos(_gama*pi/180)+_x2)
        _m_for_a =IF(_ToothType==1,IF(S_Units,Y176,1/Y176),IF(S_Units,Z176,1/Z176))
        if _ToothType == 1:
                _mx =_m_temp
                _mn =_mx*cos(_gama*pi/180)
        else:
                _mn =_m_temp
                _mx=_mn/cos(_gama*pi/180)
        #_mx =IF(_ToothType==1,_m_temp,_mn/cos(_gama*pi/180))
        #_mn =IF(_ToothType==1,_mx*cos(_gama*pi/180),_m_temp)
        _L_Proposal =IF(_ToothType==1,IF(_z1<4,(11+0.06*_z2)*_mx,(12.5+0.09*_z2)*_mx),IF(_z1<4,(11+0.06*_z2)*_mn,(12.5+0.09*_z2)*_mn))/IF(S_Units,1,25.4)#蜗杆表面宽度L[mm]
        #_alfan=1#
        if _ToothType == 1:
                _alfax =_alfa_temp
                _alfan =atan(tan(_alfax*pi/180)*cos(_gama*pi/180))*180/pi
        else:
                _alfan =_alfa_temp
                _alfax =atan(tan(_alfan*pi/180)/cos(_gama*pi/180))*180/pi
        #_alfax =IF(_ToothType==1,_alfa_temp,atan(tan(_alfan*pi/180)/cos(_gama*pi/180))*180/pi)#压力角: 法向/横向/轴向  alfan,alfat,alfax20[°]
        #_alfan =IF(_ToothType==1,atan(tan(_alfax*pi/180)*cos(_gama*pi/180))*180/pi,_alfa_temp)
        #_gama_calc =IF(_ToothType==1,atan(_z1/_q)*180/pi,asin(_z1/_q)*180/pi)
        if _ToothType == 1:
                _ex2 = 0.5 * pi * _mx - 2 * _x2 * _mx * tan(_alfax * pi / 180)
                _en2=_ex2 * cos(_gama * pi / 180)
        else:
                _en2=0.5 * pi * _mn - 2 * _x2 * _mn * tan(_alfan * pi / 180)
                _ex2=_en2 / cos(_gama * pi / 180)
        #_en2 =IF(_ToothType==1,_ex2*cos(_gama*pi/180),0.5*pi*_mn-2*_x2*_mn*tan(_alfan*pi/180))
        #_ex2 =IF(_ToothType==1,0.5*pi*_mx-2*_x2*_mx*tan(_alfax*pi/180),_en2/cos(_gama*pi/180))
        if _ToothType==1:
                _sx2=0.5*pi*_mx+2*_x2*_mx*tan(_alfax*pi/180)
                _sn2 = _sx2 * cos(_gama * pi / 180)
        else:
                _sn2 = 0.5 * pi * _mn + 2 * _x2 * _mn * tan(_alfan * pi / 180)
                _sx2=_sn2/cos(_gama*pi/180)
        #_sn2 =IF(_ToothType==1,_sx2*cos(_gama*pi/180),0.5*pi*_mn+2*_x2*_mn*tan(_alfan*pi/180))
        #_sx2 =IF(_ToothType==1,0.5*pi*_mx+2*_x2*_mx*tan(_alfax*pi/180),_sn2/cos(_gama*pi/180))
        _ex1 =IF(_ToothType==1,0.5*pi*_mx,0.5*pi*_mn/cos(_gama*pi/180))
        _sx1 =IF(_ToothType==1,0.5*pi*_mx,0.5*pi*_mn/cos(_gama*pi/180))
        _en1 =IF(_ToothType==1,0.5*pi*_mx*cos(_gama*pi/180),0.5*pi*_mn)
        _sn1 =IF(_ToothType==1,0.5*pi*_mx*cos(_gama*pi/180),0.5*pi*_mn)
        X183 =atan(_z1/6)*180/pi
        X184 =atan(_z1/25)*180/pi
        Y184 =_mn/cos(X184*pi/180)
        Y183 =_mn/cos(X183*pi/180)
        Z183 =0.5*(Y183*6+_mn*_z2/cos(X183*pi/180)+2*_x2*_mn)
        Z184 =0.5*(Y184*25+_mn*_z2/cos(X184*pi/180)+2*_x2*_mn)
        _amin_q =IF(_ToothType==1,0.5*_mx*(6+_z2+2*_x2),Z183)/IF(S_Units,1,25.4)
        _amax_q =IF(_ToothType==1,0.5*_mx*(25+_z2+2*_x2),Z184)/IF(S_Units,1,25.4)
        _d2 =IF(_ToothType==1,_mx*_z2,_mn*_z2/cos(_gama*pi/180))
        _a =IF(_ToothType==1,0.5*(_d1+_d2)+_x2*_mx,0.5*(_d1+_d2)+_x2*_mn)
        _amax_dx =IF(_ToothType==1,0.5*(_d1+_d2)+(1)*_mx,0.5*(_d1+_d2)+(1)*_mn)
        _amin_dx =IF(_ToothType==1,0.5*(_d1+_d2)+(-0.5)*_mx,0.5*(_d1+_d2)+(-0.5)*_mn)
        _d1_calc =IF(_ToothType==1,_mx*_z1/tan(_gama*pi/180),_mn*_z1/sin(_gama*pi/180))/IF(S_Units,1,25.4)
        _haXG =_haXP
        _caXG =_caXP
        _df2 =IF(_ToothType==1,_d2-2*_mx*(_haXG+_caXG-_x2),_d2-2*_mn*(_haXG+_caXG-_x2))
        _dw2 =IF(_ToothType==1,_d2+2*_mx*_x1,_d2+2*_mn*_x1)
        _da2 =IF(_ToothType==1,_d2+2*_mx*(_haXG+_x2),_d2+2*_mn*(_haXG+_x2))
        _df1 =IF(_ToothType==1,_d1-2*_mx*(_haXP+_caXP),_d1-2*_mn*(_haXP+_caXP))
        _dw1 =IF(_ToothType==1,_d1+2*_mx*_x2,_d1-2*_mn*_x2)
        _da1 =IF(_ToothType==1,_d1+2*_mx*(_haXP+_x1),_d1+2*_mn*(_haXP+_x1))
        _a_req1 =_a_req1_Input*IF(S_Units,1,25.4)
        _x_for_a =IF(_ToothType==1,_a_req1/_mx-0.5*_q-0.5*_z2,_a_req1/_mn-0.5*_z1/sin(_gama*pi/180)-0.5*_z2/cos(_gama*pi/180))
        _q_for_a =IF(_ToothType==1,(_a_req1_Input*IF(S_Units,1,25.4)-0.5*_mx*_z2-_mx*_x2)/(0.5*_mx),(_a_req1_Input*IF(S_Units,1,25.4)-0.5*_mn*_z2/cos(_gama*pi/180)-_x2*_mn)/(0.5*_mx))
        _Coeff_Kn =IF(_n1<150,(_z2/_z1*72.5/150)**0.35,(_z2/_z1*72.5/_n1)**0.35)

        R2 =IF(_DXF_Beta<0.001,0.001,_DXF_Beta)
        _Zu =IF(_DIN_Version==1,1,IF(_z2/_z1<20.5,((_z2/_z1)/20.5)**(1/6),1))#传动比因数Zu
        _ck =IF(_DesignCooling==2,0.8,1)
        B164 =IF(_calc_q==3,True,False)
        B165 =IF(_calc_q==3,True,False)
        B162 =IF(_calc_q==2,True,False)
        B163 =IF(_calc_q==2,True,False)
        B160 =IF(_calc_q==1,True,False)
        B161 =IF(_calc_q==1,True,False)
        Y170 =IF(_alfa_temp<=15,0.2,IF(_alfa_temp>=20,0.3,(_alfa_temp-15)/5*0.1+0.2))
        X398 =1#GetZoom2(_AxisDist)#当前窗口缩放比例
        _Zoom =1#GetZoom1(_Results)#当前窗口缩放比例

        Z185 =CHOOSE(_MatTypeW,0.13,0.18,0.15)
        B424 =B423
        B425 =B423
        B420 =B419
        B421 =B419
        #M169 =b2h
        _alfat =atan(tan(_alfan*pi/180)/sin(_gama*pi/180))*180/pi#压力角: 法向/横向/轴向  alfan,alfat,alfax20[°]

        _gamaw =atan(_d1/_dw1*tan(_gama*pi/180))*180/pi#螺旋角 : 中心直径/节径g, gw[°]
        AI312 =AI311+1
        AJ311 =AI311**0.85
        AJ310 =AI310**0.85
        AJ309 =AI309**0.85
        AE310 =AE309+50
        X234 =acos(cos(_gama*pi/180)*cos(_alfan*pi/180))*180/pi
        AC299 =AC298+50
        AB344 =AA344**0.75/100*60
        AB343 =AA343**0.75/100*60
        AB342 =AA342**0.75/100*60
        AB341 =AA341**0.75/100*60
        AB340 =AA340**0.75/100*60
        AB339 =AA339**0.75/100*60
        AB338 =AA338**0.75/100*60
        AB337 =AA337**0.75/100*60
        AB336 =AA336**0.75/100*60
        AA299 =AA298+50
        Y314 =8.1/100*(_n1/60-0.23)**0.7*(_ny40/100)**0.41*(_a+32)**0.63#热量分析
        Z314 =5.23/100*(_n1/60+0.28)**0.68*(abs(_ny40/100-2.203))**0.0237*(_a+22.36)**0.915#热量分析
        AB174 =5*_mn**0.5

        _Mk2 =30/pi*_Pw2/_n1*_z2/_z1*1000#扭矩
        Y315 =3.9/100*(_n1/60+2)**0.34*(_ny40/100)**-0.17*(_z2/_z1)**-0.22*(max(_a,49)-48)**0.34
        Z315 =3.4/100*(_n1/60+0.22)**0.43*(10.8-_ny40/100)**-0.0636*(_z2/_z1)**-0.18*(_a-20.4)**0.26
        _DP_Units =25.4/_m_temp
        _Ered =2/((1-_Poison1**2)/_E1/1000+(1-_Poison2**2)/_E2/1000)
        #S_ExtraCopy_FlagOUT =2*S_ExtraCopy_FlagIN
        _z2minTh =2*_haXP/(sin(_alfa_temp*pi/180))**2
        X160 =2*(1.4+2*(_z1**0.5))
        AE2 =2*(_a-_df2/2)/IF(S_Units,1,25.4)
        AC2 =2*(_a-_da2/2)/IF(S_Units,1,25.4)
        AD2 =2*(_a-_d2/2)/IF(S_Units,1,25.4)
        Z316 =1-9/((0.012*_z2/_z1+0.092)*_n1**0.5-0.745*_z2/_z1+82.877)
        Y316 =1-5/((0.012*_z2/_z1+0.092)*_n1**0.5-0.745*_z2/_z1+82.877)
        AD321 =14*(_n1/200)**0.5
        AC331 =-13.129*LOG((LOG(_ny40+0.7))/(LOG(_ny100+0.7)))
        X264 =-13.129*LOG((LOG(_ny40+0.7))/(LOG(_ny100+0.7)))
        _Ygama =1/cos(_gama*pi/180)#主要因数Yg
        AB254 =1.03*(0.4+_x2/(_z2/_z1)+0.01*_z2-0.083*_b2H/_mx+(2*_q-1)**0.5/6.9+(_q+50*(_z2/_z1+1)/(_z2/_z1))/(15.9+37.5*_q))
        _Yepsilon =0.5#齿轮齿数比因数Ye
        _deltalim =0.04*_mx**0.5
        _h_x_1998 =0.018+_q/(7.86*(_q+_z2))+1/_z2+_x2/110-(_z2/_z1)/36300+_b2H/(370.4*_mx)-(2*_q-1)**0.5/213.9
        Z321 =0.0066*(1+0.42*(_n1/60)**0.75)
        AA321 =0.0066*(1+0.23*(_n1/60)**0.75)
        _PV0 =0.000089*_a*_n1**(4/3)
        O282 =_Zu#传动比因数Zu
        X158 =_Zoom
        O283 =_Zoil#润滑因数Zoil
        O279 =_Zh#寿命因数Zh
        #C322 =_ZeroValue
        X169 =_z2minTh
        P397 =_z2_req#蜗杆/蜗轮 齿数z1, z2
        _i =_z2/_z1#实际传动比i
        _NG =_z2#蜗杆/蜗轮 齿数NW, NG
        P223 =_z2#蜗杆/蜗轮 齿数z1,z2
        S2 =_z2
        T161 =_z2
        P155 =_z1_to#z1范围 从-到
        #Y159 =_z1_Results
        O397 =_z1_req#蜗杆/蜗轮 齿数z1, z2
        O155 =_z1_from#z1范围 从-到
        X400 =_z1_axis2
        _NW =_z1#蜗杆/蜗轮 齿数NW, NG
        E2 =_z1
        O223 =_z1#蜗杆/蜗轮 齿数z1,z2
        O161 =_z1#蜗杆/蜗轮 齿数z1,z2
        O244 =_YW#材料因数YW
        B303 =_YNLFlag
        T303 =_YNL_Proposal
        O303 =_YNL#寿命因数/精度等级YNL
        O300 =_Ygama#主要因数Yg
        O298 =_Yepsilon#齿轮齿数比因数Ye
        O408 =_XX_z1#用齿数来进行传动率计算z1,z2 = i
        P410 =_XX_n2#用小齿轮速度和扭矩进行功率计算Mk2,n2=Pw2
        _XX_i =_XX_n1/P409
        O409 =_XX_n1#用速度来进行传动比计算n1,n2 = i
        _XX_Pw2 =_XX_Mk2*_XX_n2/9550
        O410 =_XX_Mk2#用小齿轮速度和扭矩进行功率计算Mk2,n2=Pw2
        R409 =_XX_i
        #AB159 =_x2_Results
        AC400 =_x2_axis2
        O173 =_x2#蜗轮齿顶修正系数x [modul]
        X172 =_x1
        #Y173 =_x_srollbar
        X174 =_x_for_a
        O271 =_WNS#抬高系数/每小时开始数WNS
        O272 =_WML#材料/润滑剂因数 - 磨损WML
        P387 =_VHV2#齿的边缘硬度VHV[HV]
        O387 =_VHV1#齿的边缘硬度VHV[HV]
        #G117 =_UnitPT_BCKP
        F117 =_UnitPT
        F129 =_ToothType
        X311 =_thetaSlimProp
        O311 =_thetaSlimInput#齿轮箱的极端温度(油)JSlim       [°C]
        #B311 =_thetaSlimFlag
        T311 =_thetaSlim
        X318 =_thetaReqProposal
        O318 =_thetaReqInput#目标最大齿轮箱温度(油)JSmax       [°C]
        #B318 =_thetaReqFlag
        T318 =_thetaReq
        O310 =_theta0_Input#环境温度J0       [°C]
        T310 =_theta0
        F166 =_TeethOrientation
        O304 =_TauFlimT*IF(S_Units,1,0.145037)#剪切抵抗极限tFlimT  [MPa]
        _TauFG =_TauFlimT*_YNL
        T304 =_TauFlimT
        O305 =_TauFG*IF(S_Units,1,0.145037)#齿根剪切应力极限值tFG  [MPa]
        T305 =_TauFG
        P236 =_sx2/IF(S_Units,1,25.4)#中心面齿厚sx1,sx2[mm]
        Z2 =_sx2/2/IF(S_Units,1,25.4)
        U236 =_sx2
        O236 =_sx1/IF(S_Units,1,25.4)#中心面齿厚sx1,sx2[mm]
        M2 =_sx1/2/IF(S_Units,1,25.4)
        T236 =_sx1
        O141 =_SW_proposal#磨损安全SW
        F157 =_SortTbl
        P235 =_sn2/IF(S_Units,1,25.4)#法向面齿厚sn1,sn2[mm]
        Y2 =_sn2/2/IF(S_Units,1,25.4)
        U235 =_sn2
        O235 =_sn1/IF(S_Units,1,25.4)#法向面齿厚sn1,sn2[mm]
        L2 =_sn1/2/IF(S_Units,1,25.4)
        T235 =_sn1

        _SK_Proposal =ROUND(_mx*2/IF(S_Units,1,25.4)*1.001,3)#轮缘厚度SK[mm]
        _SKInput=CellTransmitVal(_SK_Proposal, _SKInput,轮缘厚度输入判断值)
        _SK =_SKInput*IF(S_Units,1,25.4)
        O301 =_SKInput#轮缘厚度SK[mm]
        #B301 =_SKFlag
        T301 =_SK
        O284 =_sigmaHlimT*IF(S_Units,1,0.145037)#蚀损阻抗sHlimT  [MPa]
        U284 =_sigmaHlimT
        Q2 =_Shaft_th
        P416 =_Shaft_th#轴肩(直径,宽度)ds, t[mm]
        P2 =_Shaft_ds
        O416 =_Shaft_ds#轴肩(直径,宽度)ds, t[mm]
        O142 =_SH_proposal#蚀损安全SH
        O144 =_SF_Proposal#齿强度安全SF
        O143 =_Sd_Proposal#蜗杆挠度安全Sd
        #X140 =_SafetySumBool
        #Y140 =_SafetySum
        X255 =_s_x
        # =_S_QCalc_beta
        #X134 =_rooil15_tbl
        O136 =_rooil15_Input#15°C下润滑油密度roil15     [kg/dm**3]
        T136 =_rooil15
        P380 =_Ro2#密度Ro[kg/m**3]
        O380 =_Ro1#密度Ro[kg/m**3]
        _rf2 =_rf1
        O150 =_rf1#齿根半径系数rf*      [modul]
        #F159 =_Results
        O137 =_Ra_Input#蜗杆的平均粗造度系数Ra1     [microm]
        T137 =_Ra
        T327 =_Qoil*60
        O327 =_Qoil#油喷体积Qoil       [litre/s]
        P390 =_qH2#接触疲劳说明线图qH
        O390 =_qH1#接触疲劳说明线图qH
        P392 =_qF2#弯曲疲劳说明线图qF
        O392 =_qF1#弯曲疲劳说明线图qF
        #Z159 =_q_Results
        X177 =_q_for_a
        AB400 =_q_axis2
        _dm1 =_q*_mx
        O163 =_q#直径率(q =d1/m)q
        P119 =_Pw2_Input#传动功率Pw [kW][kW]
        U119 =_Pw2
        O250 =_PV0*IF(S_Units,0.001,0.00134102)#无负载损失PV0  [kW]
        U250 =_PV0
        F118 =_PoweredWoWh
        P384 =_Poison2#损坏率
        O384 =_Poison1#损坏率
        #B322 =_PK1Flag

        F133 =_OilType
        #Y134 =_ny40_tbl
        O135 =_ny40#40°C 和 100°C下运动粘度n40,n100[mm**2/s]
        #Z134 =_ny100_tbl
        P135 =_ny100#40°C 和 100°C下运动粘度n40,n100[mm**2/s]
        O334 =_NW#蜗杆/蜗轮 齿数NW, NG
        P389 =_NHLim2#接触负荷循环基数NHlim
        O389 =_NHLim1#接触负荷循环基数NHlim
        P334 =_NG#蜗杆/蜗轮 齿数NW, NG
        P391 =_NFLim2#弯曲负荷循环基数NFlim
        O391 =_NFLim1#弯曲负荷循环基数NFlim
        _n2 =_n1/_i#速度(蜗杆/蜗轮)n [/min][/min]
        O120 =_n1#速度(蜗杆/蜗轮)n [/min][/min]
        P220 =_mx/IF(S_Units,1,25.4)#模数: 法向/横向/轴向 mn,mt,mx2[mm]
        _dm2 =_mx*_z2+2*_x2*_mx
        V220 =_mx
        F167 =_Module
        X167 =_mn_fromtable
        _mt =_mn/sin(_gama*pi/180)#模数
        M220 =_mn/IF(S_Units,1,25.4)
        Z306 =_mn
        T220 =_mn
        _T2 =_Mk2*_KA
        U121 =_Mk2
        F128 =_MatW
        X128 =_MatTypeW
        F127 =_MatP
        _CP =_m_temp*pi/25.4#圆周齿距 / 径节CP/DP
        T167 =_m_temp
        #AA159 =_m_Results
        O167 =_m_Input#模数/ 额定值mn[mm]
        X176 =_m_for_a
        Z400 =_m_axis2
        X132 =_LubricationIndex
        F134 =_Lubricant
        F131 =_LoadTypeB
        F130 =_LoadTypeA
        _NL =_Lh*_n1*60/(_z2/_z1)#负载周期NL
        O139 =_Lh#期望使用寿命Lh     [h]
        P169 =_l2_proc#左/右轴承距离(直径百分比)l1%,l2%[% da2]
        _l2 =_l2_input*IF(S_Units,1,25.4)
        O290 =_l2_input#右轴承间距l2  [mm]
        P170 =_l2_input#左/右轴承距离l1,l2[mm]
        U170 =_l2
        B169 =_l1l2_flag
        #B170 =_l1l2_flag
        O169 =_l1_proc#左/右轴承距离(直径百分比)l1%,l2%[% da2]
        _l1 =_l1_input*IF(S_Units,1,25.4)
        O289 =_l1_input#左轴承间距l1  [mm]
        O170 =_l1_input#左/右轴承距离l1,l2[mm]
        T170 =_l1
        P171 =_L_Proposal#蜗杆表面宽度L[mm]
        O171 =_L_Input#蜗杆表面宽度L[mm]
        H2 =_L/IF(S_Units,1,25.4)
        O233 =_L/IF(S_Units,1,25.4)#蜗杆表面宽度/蜗轮表面宽度L/b2H[mm]
        T171 =_L
        X261 =_kp
        #B321 =_kFlag
        #P138 =_KA_Prop#运用因素KA
        #B138 =_KA_Flag
        O138 =_KA#运用因素KA



        X122 =_iin_fromtable
        O122 =_iin#传动比i
        X159 =_IDTblMax
        #AC159 =_i_Results
        Y400 =_i_axis2
        _mG =_i#传动比mG
        O123 =_i#实际传动比i

        O147 =_haXP#齿根高系数ha*      [modul]
        X147 =_haXG
        X244 =_h_x_1998
        Z181 =_GboxDensity
        H319 =_GboxAreaType
        P234 =_gamaw#螺旋角 : 中心直径/节径g, gw[°]
        F165 =_gamaProp
        X166 =_gamaFromTbl
        #X165 =_gama_calc
        O234 =_gama#螺旋角 : 中心直径/节径g, gw[°]
        O165 =_gama#螺旋角g[°]

        #B171 =_FlagL
        #B172 =_Flagb2H
        F177 =_FitAxis
        #Y130 =_FH_proposal
        P238 =_ex2/IF(S_Units,1,25.4)#中心面齿间隙厚度ex1,ex2[mm]
        AB2 =_ex2/2/IF(S_Units,1,25.4)
        U238 =_ex2
        O238 =_ex1/IF(S_Units,1,25.4)#中心面齿间隙厚度ex1,ex2[mm]
        O2 =_ex1/2/IF(S_Units,1,25.4)
        T238 =_ex1

        #E329 =_Err5
        O258 =_Ered*IF(S_Units,1,0.145037)#相等的弹性模量EEred  [MPa]
        U258 =_Ered
        P237 =_en2/IF(S_Units,1,25.4)#法向面齿间隙厚度en1,en2[mm]
        AA2 =_en2/2/IF(S_Units,1,25.4)
        U237 =_en2
        O237 =_en1/IF(S_Units,1,25.4)#法向面齿间隙厚度en1,en2[mm]
        N2 =_en1/2/IF(S_Units,1,25.4)
        T237 =_en1
        P381 =_E2#杨氏模量(弹性模数)E[GPa]
        O381 =_E1#杨氏模量(弹性模数)E[GPa]
        #H415 =_DXFWheelNo
        #X427 =_DXF_TblOutName
        O417 =_DXF_Beta#蜗轮收缩角b[ ° ]
        P227 =_dw2/IF(S_Units,1,25.4)#节圆柱直径dw1,dw2[mm]
        U227 =_dw2
        O227 =_dw1/IF(S_Units,1,25.4)#节圆柱直径dw1,dw2[mm]
        T227 =_dw1
        X325 =_dthetaS_prop
        O325 =_dthetaS_Input#润滑油的温度差异DJ       [°C]
        T325 =_dthetaS
        #B417 =_dstFlag
        #B416 =_dstFlag
        T168 =_DP_Units
        AA400 =_DP_axis2
        P228 =_dm2/IF(S_Units,1,25.4)#中心直径dm1,dm2[mm]
        U228 =_dm2
        O228 =_dm1/IF(S_Units,1,25.4)#中心直径dm1,dm2[mm]
        _vgm =_dm1*_n1/(19098*cos(_gama*pi/180))

        T228 =_dm1
        P156 =_Diam_q_to#q范围 从-到
        O156 =_Diam_q_from#q范围 从-到
        P226 =_df2/IF(S_Units,1,25.4)#齿根圆直径df1,df2[mm]
        W2 =_df2/IF(S_Units,1,25.4)
        U226 =_df2
        K2 =_df1/IF(S_Units,1,25.4)
        O226 =_df1/IF(S_Units,1,25.4)#齿根圆直径df1,df2[mm]
        T226 =_df1
        F132 =_DesignCooling
        #B275 =_deltaWlimnFlag
        _deltaWlimn30 = (0.3 * _mx * cos(_gama * pi / 180)) / IF(S_Units, 1, 25.4)
        _deltaWlimn_Input=CellTransmitVal(_deltaWlimn30,_deltaWlimn_Input,判断齿侧允许磨损)
        _deltaWlimn =_deltaWlimn_Input*IF(S_Units,1,25.4)
        O275 =_deltaWlimn_Input#齿侧允许磨损dWlimn[mm]
        U275 =_deltaWlimn
        O294 =_deltalim/IF(S_Units,1,25.4)#允许蜗杆轴变形dlim  [mm]
        U294 =_deltalim
        O229 =_de2Input#蜗轮外径de2[mm]
        #B229 =_de2Flag
        P224 =_da2/IF(S_Units,1,25.4)#齿顶圆直径da1,da2[mm]
        U2 =_da2/IF(S_Units,1,25.4)
        _l2_Units =_da2*_l2_proc/100/IF(S_Units,1,25.4)
        _l1_Units =_da2*_l1_proc/100/IF(S_Units,1,25.4)
        U224 =_da2
        I2 =_da1/IF(S_Units,1,25.4)
        O224 =_da1/IF(S_Units,1,25.4)#齿顶圆直径da1,da2[mm]
        T224 =_da1
        _d2_Units =_d2/IF(S_Units,1,25.4)#参考直径 蜗杆/蜗轮d1, d2[mm]
        P225 =_d2/IF(S_Units,1,25.4)#参考直径d1,d2[mm]
        V2 =_d2/IF(S_Units,1,25.4)
        U225 =_d2
        O164 =_d1_Input#蜗杆中心直径d1[mm]
        X164 =_d1_calc
        _d1_Units =_d1/IF(S_Units,1,25.4)#参考直径 蜗杆/蜗轮d1, d2[mm]
        J2 =_d1/IF(S_Units,1,25.4)
        O225 =_d1/IF(S_Units,1,25.4)#参考直径d1,d2[mm]
        _d_LC =_d1/25.4#蜗杆节径,蜗轮节径d,D[in]

        T164 =_d1
        O338 =_d_LC#蜗杆节径,蜗轮节径d,D[in]
        O168 =_CP#圆周齿距 / 径节CP/DP
        H324 =_Cooling2
        H312 =_Cooling1
        P385 =_ContactLimit2#接触疲劳极限SHlim[MPa]
        O385 =_ContactLimit1#接触疲劳极限SHlim[MPa]
        X326 =_coilProp
        B326 =_coilFlag
        O326 =_coil_Input#油比热coil       [Ws/Kg/°K]
        T326 =_coil
        X331 =_Coeff_Kn
        Z330 =_ck

        O148 =_caXP#动力头间隙c*      [modul]
        X148 =_caXG
        F351 =_CastType
        O260 =_calfa#恒量的,用于代替粘度指数ca  [m**2/N]
        F163 =_calc_q
        P386 =_BendingLimit2#弯曲疲劳极限SFlim[MPa]
        O386 =_BendingLimit1#弯曲疲劳极限SFlim[MPa]
        F251 =_BearingType
        #M425 =_BBOM03
        #M424 =_BBOM02
        #M423 =_BBOM01
        O172 =_b2H_Input#蜗轮表面宽度b2H[mm]
        P233 =_b2H/IF(S_Units,1,25.4)#蜗杆表面宽度/蜗轮表面宽度L/b2H[mm]
        T2 =_b2H/IF(S_Units,1,25.4)
        _AR =_b2H*_dm2*0.000001
        T172 =_b2H
        F400 =_AxisDist
        X330 =_AR
        Y177 =_amin_q
        X175 =_amin_dx
        Z177 =_amax_q
        Y175 =_amax_dx
        D2 =_alfax
        P222 =_alfax#压力角: 法向/横向/轴向  alfan,alfat,alfax20[°]
        O222 =_alfat#压力角: 法向/横向/轴向  alfan,alfat,alfax20[°]
        M222 =_alfan
        F162 =_Alfa0ID
        X161 =_Alfa0fromTbl
        _alfa0 =_alfa_temp
        O162 =_alfa_temp#法向压力角a[°]
        #AD159 =_alfa_Results
        O320 =_AgesInput#齿轮箱表面A       [m**2]
        #B320 =_AgesFlag

        H303 =_AG
        #M421 =_ABOM03
        #M420 =_ABOM02
        #M419 =_ABOM01
        AA229 =IF(S_Units,_da2+_mx,(_da2+_mx)/25.4)
        AA231 =(_b2H/2)*(_a-_da2/2)/(_a-_df2/2)
        AB231 =((_a-_da2/2)**2-(AA231)**2)**0.5
        AC231 = _a - _df2 / 2 - AB231
        X231 =((_a-_df2/2)**2-(_b2H/2)**2)**0.5
        Y231 =_a-_df2/2-X231
        _de2min = (_df2 + 2 * Y231 + 0.02 * _mn) / IF(S_Units, 1, 25.4)
        Z232 = (_df2 + 2 * Y231) / IF(S_Units, 1, 25.4)
        _de2max = (_df2 + 2 * AC231 - 0.02 * _mn) / IF(S_Units, 1, 25.4)
        _de2Prop = ROUND(min(max(_de2min, AA229), _de2max), IF(S_Units, 2, 3))
        _de2Input = CellTransmitVal(_de2Prop, _de2Input, 涡轮外径判断值)
        _de2 = IF(S_Units, _de2Input, _de2Input * 25.4)
        X2 = _de2 / IF(S_Units, 1, 25.4)
        U229 = _de2

        T177 =_a_req1
        O398 =_a_req#目标圆心距a[mm]
        _WaTh =_a**0.5
        _a_Units =_a/IF(S_Units,1,25.4)#所需圆心距 / 当前的a [mm]
        A2 =_a/IF(S_Units,1,25.4)
        O232 =_a/IF(S_Units,1,25.4)#圆心距a[mm]
        _C =_a/25.4#圆心距,蜗杆轴距C, px[in]
        T336 =_a/25.4
        _DXF_AutoScale =_a/100
        AB173 =_a
        Z307 =_a
        T232 =_a
        _mass1 =(pi*_df1*_df1/4*(_l1-_L/2)+pi*_d1*_d1/4*_L+pi*_df1*_df1/4*(_l2-_L/2))*_Ro1/1000000000
        _B =(6*_mx*_dm1-9*_mx*_mx+_mx)**0.5
        _Zv =(5/(4+_vgm))**0.5#速度因数Zv
        _Zs =(3000/(2900+_a))**0.5#尺寸因数Zs
        T245 =(3.2/0.5)**0.25
        _Coeff_Ks =(160/_a)**0.6
        _YS =(100/min(max(65,_a),250))**0.5#比例系数YS
        _z2minPr =(1+Y170/_haXP)*X169
        _ShaftDA2 =(1.77*10000000*_Pw2/_n2)**0.333#     主要动力传送轴DA[mm]
        _ShaftDB2 =(0.83*10000000*_Pw2/_n2)**0.333#     小的,短轴DB[mm]

        AG310 =(0.3*(AE310/25.4)**1.7)/10.7639104167097
        AG309 =(0.3*(AE309/25.4)**1.7)/10.7639104167097
        AD320 =(0.3*(_a/25.4)**1.7)/10.7639104167097
        _YR =(_Ra/0.5)**0.25#表面耐久性粗糙因素YR

        P123 =(_i-_iin)/_i#实际传动比i
        _ha2 =(_da2-_d2)/2
        _ha1 =(_da1-_d1)/2
        _hf2 =(_d2-_df2)/2
        _hf1 =(_d1-_df1)/2

        AF310 =((400/AE310)**0.3-1)*15
        AF309 =((400/AE309)**0.3-1)*15
        AD299 =((200/AC299)**0.5-1)*10
        AD298 =((200/AC298)**0.5-1)*10
        AB299 =((200/AA299)**0.4-1)*10
        AB298 =((200/AA298)**0.4-1)*10
        _kTempFactor =((_thetaReq-_theta0)-40)*IF(_Cooling1==1,0.1,0.05)
        Y320 =((_da1+_da2+4*_mx+_WaTh)*(_da2+4*_mx+_WaTh)*2+(_da1+_da2+4*_mx+_WaTh)*2*(_da1+2*_mx+_WaTh)+(_da2+4*_mx+_WaTh)*2*(_da1+2*_mx+_WaTh))/1000000

        Q408 =1
        Q409 =1
        Q410 =1
        _etaStatic =Z185*_YS**0.5*_YW*_YR
        AB320 =Y320*2.2
        AA320 =Y320*1.7
        Z320 =Y320*1.3
        #Y398 =VLOOKUP(X398,T_HeaderStrings2,2)
        #Y158 =VLOOKUP(_Zoom,T_HeaderStrings,2)#显示值
        #AA106 =S_ExtraCopy_FlagOUT
        #X414 =S_DXFScale
        Y160 =ROUND(X160*_m_temp/IF(S_Units,1,25.4),2)
        _xmin =ROUND(max(_haXP*(_z2minPr-_z2)/_z2minTh,-1),3)
        _b2H_Proposal =ROUND(IF(_z1<4,0.75*(1+2/_q)*_d1,0.67*(1+2/_q)*_d1)/IF(S_Units,1,25.4),2)#蜗轮表面宽度b2H[mm]
        _gama_SelfLock =ROUND(atan(_etaStatic)*180/pi,2)

        Y229 =ROUND((_da2+_mx*1.5)/IF(S_Units,1,25.4),IF(S_Units,2,3))
        X229 =ROUND((_da2+_mx*0)/IF(S_Units,1,25.4),IF(S_Units,2,3))
        _v =pi*_n1*_dm1/25.4/(12*cos(_gama*pi/180))#滑动速度v   [ft/min]
        _pn =pi*_mn
        _v2 =pi*_d2/1000*_n2/60
        _v1 =pi*_d1/1000*_n1/60
        _mass2 =pi*_b2H*((_da2-_ha2)**2/4-(_da2-2*(_ha2+_hf2)-2*_SK)**2/4)*_Ro2/1000000000+(pi*_b2H*0.25*((_da2-2*(_ha2+_hf2)-_SK)**2/4-_ShaftDB2**2/4)+pi*_b2H*((_ShaftDB2+3*_SK)**2/4-_ShaftDB2**2/4))*_Ro1/1000000000+pi*_b2H*2.5*(_ShaftDB2**2/4)*_Ro1/1000000000
        _GboxArea =pi*(_da2+4*_mn)**2/2+(_da2+_mn*4)**2+(pi*(_da2+_mn*4)/2+_da2)*(_b2H+_mn*4)+(_l1+_l2)*(_da1+_mn*4)*3+(_da1+_mn*4)**2*2
        _XXX_i =P408/O408
        _Fe =min(0.67*_dm1/25.4,_b2H/25.4)#有效表面宽度Fe   [in]
        _kSizeFactor =min(((400/_a)**0.3-1)*15-2,10)
        AA243 =-0.511+0.0000037904*(_z2**-0.0847)*(_alfa0**0.0595)*(0.0000007947*_x2+0.00005927)*((1-0.038*_q)*_q+65.576)*((108.8547*_z1/_q-1)*_z1/_q-3294.921)*((0.003291*_B+1)*_B-13064.58)
        Z243 =-0.393+0.0000029157*(_z2**-0.0847)*(_alfa0**0.0595)*(0.0000007947*_x2+0.00005927)*((1-0.038*_q)*_q+65.576)*((108.8547*_z1/_q-1)*_z1/_q-3294.921)*((0.003291*_B+1)*_B-13064.58)
        _h_x =max(IF(_DIN_Version==1,_h_x_1998,IF(_ToothType==5,AA243,Z243)),0.000000001)
        _pm_x_1998 =max(1.03*(0.4+_x2/(_z2/_z1)+0.01*_z2-0.083*_b2H/_mx+((2*_q-1)**0.5)/6.9+(_q+50*(_z2/_z1+1)/(_z2/_z1))/(15.9+37.5*_q)),0.01)
        Y264 =LOG(LOG(_ny40+0.7))-2.496*X264
        AD331 =LOG(LOG(_ny40+0.7))-2.496*AC331
        _Shaft_th_prop =IF(S_Units,ROUND(_mn/4,1),ROUND((_mn/4)/25.4,2))
        _Shaft_ds_prop =IF(S_Units,ROUND(_df1-_mn,1),ROUND((_df1-_mn)/25.4,2))
        _DP =IF(S_Units,25.4/_m_temp,_m_temp/25.4)#圆周齿距 / 径节CP/DP
        P121 =IF(S_Units,1,8.850732)*_Mk2#扭矩(蜗杆/蜗轮)Mk [Nm][Nm]

        B168 =IF(B169,1,0)
        _Flag_z2min =IF(AND(_z2<_z2minPr,_x2<_xmin),1,0)
        _YK =IF(_SK<_mx*2,1.043*LN(5.281*_mx/_SK),1)#轮缘厚度系数YK
        _c2 =IF(_OilType==1,Z316,IF(_OilType==2,Y316,1))
        _alfaL =IF(_n1<150,_ck*4190,_ck*(1940+15*_n1))
        Y254 =0.1794+0.2389*_a/_dm1+0.0761*_x2*(abs(_x2))**3.18+0.0536*_q-0.00369*_z2-0.01136*_alfa0+44.9814*(_x2+0.005657)/_z2*(_z1/_q)**2.6872
        Z254 =0.1401+0.1866*_a/_dm1+0.0595*_x2*(abs(_x2))**3.18+0.0419*_q-0.00288*_z2-0.0089*_alfa0+35.1417*(_x2+0.005657)/_z2*(_z1/_q)**2.6872
        _pm_x =IF(_DIN_Version==1,_pm_x_1998,IF(_ToothType==5,Z254,Y254))
        Y321 =IF(_Cooling1==1,Z321,AA321)
        _c1 =IF(_Cooling1==1,Y315,Z315)
        _c0 =IF(_Cooling1==1,Y314,Z314)
        _AgesProp =CHOOSE(_GboxAreaType,Y320,Z320,AA320,AB320)*IF(S_Units,1,10.7639104167097)
        _AgesInput = CellTransmitVal(_AgesProp, _AgesInput, 齿轮箱表面判断值)
        _Ages =IF(S_Units,_AgesInput,_AgesInput/10.7639104167097)
        T320 =_Ages
        AI314 =AI312+1
        AJ312 =AI312**0.85
        AE311 =AE310+50
        AC300 =AC299+50
        AA300 =AA299+50
        X351 =720+10.37*_C**3
        Z349 =65.52*_v**(-0.774)
        _sigmaHm =4/pi*(_pm_x*_T2*1000*_Ered/_a**3)**0.5
        _Ftm2 =2000*_T2/_dm2
        _D_UC =2*_C-_d_LC#蜗杆节径,蜗轮节径d,D[in]
        Y349 =13.31*_v**(-0.571)
        Z348 =1.1483-0.00658*_mG
        X349 =0.659*exp(-0.0011*_v)

        Y350 =0.124*exp(-0.074*_v**0.645)
        Z350 =0.103*exp(-0.11*_v**0.45)+0.012
        X251 =0.03*_Pw2*1000*_a**0.44*(_z2/_z1)/_dm2
        X348 =0.02*(-(_mG**2)+40*_mG-76)**0.5+0.46
        Y251 =0.013*_Pw2*1000*_a**0.44*(_z2/_z1)/_dm2
        Y348 =0.0107*(-(_mG**2)+56*_mG+5145)**0.5
        _PVD =0.00001178*_dm1**2*_n1*2
        O280 =_Zv#速度因数Zv
        O281 =_Zs#尺寸因数Zs
        X170 =_z2minPr
        O242 =_YS#比例系数YS
        O245 =_YR#表面耐久性粗糙因素YR
        O302 =_YK#轮缘厚度系数YK
        R408 =_XXX_i
        R410 =_XX_Pw2
        X171 =_xmin
        X319 =_WaTh
        O241 =_vgm*IF(S_Units,1,3.28083989501312)#滑动速度vgm  [m/s]
        T241 =_vgm
        P372 =_v2*IF(S_Units,1,3.28083989501312)#圆周速度v1,v2[m/s]
        U372 =_v2
        O372 =_v1*IF(S_Units,1,3.28083989501312)#圆周速度v1,v2[m/s]
        T372 =_v1
        O347 =_v#滑动速度v   [ft/min]
        _thetaS_B =_theta0+(_c1*_Mk2/(_a/63)**3+_c0)*_c2
        Y259 =_T2
        P301 =_SK_Proposal#轮缘厚度SK[mm]
        O259 =_sigmaHm*IF(S_Units,1,0.145037)#平均接触面应力sHm  [MPa]
        U259 =_sigmaHm
        _sigmaHG =_sigmaHlimT*_Zh*_Zv*_Zs*_Zu*_Zoil
        O285 =_sigmaHG*IF(S_Units,1,0.145037)#接触面应力极限值sHG  [MPa]
        U285 =_sigmaHG
        P405 =_ShaftDB2#     小的,短轴DB[mm]
        P404 =_ShaftDA2#     主要动力传送轴DA[mm]
        X417 =_Shaft_th_prop
        X416 =_Shaft_ds_prop
        _sWm =_s_x*_sigmaHm*_a/_Ered*_NL
        X150 =_rf2
        #X163 =_q_calc
        O252 =_PVD*IF(S_Units,0.001,0.00134102)#密封损失PVD  [kW]
        U252 =_PVD
        _pt =_pn/sin(_gama*pi/180)
        M221 =_pn/IF(S_Units,1,25.4)
        T221 =_pn
        X253 =_pm_x_1998
        X254 =_pm_x
        O266 =_NL#负载周期NL
        P120 =_n2#速度(蜗杆/蜗轮)n [/min][/min]
        _deltaWlimnMax =_mx*cos(_gama*pi/180)*(pi/2-2*tan(_alfa0*pi/180))/IF(S_Units,1,25.4)
        O220 =_mt/IF(S_Units,1,25.4)#模数: 法向/横向/轴向 mn,mt,mx2[mm]
        U220 =_mt
        O335 =_mG#传动比mG
        X180 =_mass2
        X179 =_mass1
        U169 =_l2_Units
        T169 =_l1_Units
        AC321 =_kTempFactor
        AB321 =_kSizeFactor

        P231 =_hf2/IF(S_Units,1,25.4)#齿根高hf1,hf2[mm]
        U231 =_hf2
        O231 =_hf1/IF(S_Units,1,25.4)#齿根高hf1,hf2[mm]
        T231 =_hf1
        P230 =_ha2/IF(S_Units,1,25.4)#齿顶高ha1,ha2[mm]
        U230 =_ha2
        O230 =_ha1/IF(S_Units,1,25.4)#齿顶高ha1,ha2[mm]
        T230 =_ha1
        X243 =_h_x
        Y181 =_GboxArea
        X185 =_gama_SelfLock
        P373 =_Ftm2*IF(S_Units,1,0.224809)#切向力Ftm1,Ftm2[N]
        U373 =_Ftm2
        U161 =_Flag_z2min
        O352 =_Fe#有效表面宽度Fe   [in]
        Y185 =_etaStatic
        X415 =_DXF_AutoScale
        P168 =_DP#圆周齿距 / 径节CP/DP

        X275 =_deltaWlimnMax
        X278 =_deltaWlimn30/(_deltaWlimnMax/100)
        Y275 =_deltaWlimn30
        P174 =_d2_Units#参考直径 蜗杆/蜗轮d1, d2[mm]
        O174 =_d1_Units#参考直径 蜗杆/蜗轮d1, d2[mm]
        P338 =_D_UC#蜗杆节径,蜗轮节径d,D[in]
        Z331 =_Coeff_Ks
        X149 =_caXP/(1-sin(_alfa0*pi/180))
        O149 =_caXG/(1-sin(_alfa0*pi/180))#被推荐齿根半径系数
        X316 =_c2
        X315 =_c1
        X314 =_c0
        O336 =_C#圆心距,蜗杆轴距C, px[in]
        P172 =_b2H_Proposal#蜗轮表面宽度b2H[mm]
        Y243 =_B
        Y330 =_alfaL
        X222 =_alfa0
        X320 =_AgesProp
        P176 =_a_Units#所需圆心距 / 当前的a [mm]
        _kProp =(IF(_DesignCooling==2,0.8*Y321,1*Y321)*1000+_kSizeFactor+_kTempFactor)/IF(S_Units,1,5.6778)
        _k_Input = CellTransmitVal(_kProp, _k_Input, 热传导效率判断值)
        _k = _k_Input * IF(S_Units, 1, 5.6778)
        O321 = _k_Input  # 热传导效率k       [W/m2*K]
        T319 =_k/5.6778*778/60
        T321 =_k
        AG311 =(0.3*(AE311/25.4)**1.7)/10.7639104167097
        P178 =(_mass1+_mass2)*IF(S_Units,1,2.204624)#齿轮箱/齿轮 近似重量m[kg]
        T323 =(_k*(_thetaReqInput-_theta0_Input))/1000
        _mass3 =(_GboxArea*(_mn)**0.5*5)/1000000000*_GboxDensity


        AD232 =(_df2+2*AC231)/IF(S_Units,1,25.4)
        AF311 =((400/AE311)**0.3-1)*15
        AD300 =((200/AC300)**0.5-1)*10
        AB300 =((200/AA300)**0.4-1)*10
        #L399 =Y398
        #L158 =Y158

        _WH = IF(_MatTypeW == 2, (300 / _sigmaHm) ** 1.4, IF(_sigmaHm < 450, 1, (450 / _sigmaHm) ** 4.5))
        _YG =min((0.07/_h_x)**0.5,2)#几何因数YG
        #_KW=1#查找y246不需要kw
        Y246 = T_Lubrication(_vgm=_vgm, 行号=_LubricationIndex, 列号=5)
        X246 = T_Lubrication(_vgm=_vgm,  行号=_LubricationIndex, 列号=4)
        _eta0T =IF(_MatTypeW==2,Y246,X246)#摩擦基本系数m0T
        _etazm =_eta0T*_YS*_YG*_YW*_YR#摩擦中心系数mzm
        _etaz = max(0.0001,IF(_PoweredWoWh == 1, tan(_gama * pi / 180) / tan((_gama + atan(_etazm) * 180 / pi) * pi / 180),tan((_gama - atan(_etazm) * 180 / pi) * pi / 180) / tan(_gama * pi / 180)))  # 齿轮功率hz
        _PVz = 0.1 * _Mk2 * _n1 / (_z2 / _z1) * (1 / _etaz - 1)
        _dtheta = 1 / (_alfaL * _AR) * _PVz
        AH251 =(0.83*10000000*_Pw2/_etaz/_n1)**0.333
        _pitchx =pi*_D_UC/_NG#圆心距,蜗杆轴距C, px[in]
        _Cs =min(X351,Y351)#材料因数Cs
        AG251 = _Mk2 / _i / _etaz * _KA
        AF251 = 2000 * AG251 / _dm1
        _roz = atan(_etazm) * 180 / pi  # 摩擦角rz  [°]
        AE251 = AF251 * tan(_alfan * pi / 180) / sin(_gama * pi / 180 + _roz * pi / 180)
        AD251 =(AE251**2+AF251**2)**0.5
        AC251 =(AE251**2+_Ftm2**2)**0.5
        AA251 =AD251*0.01*(AH251/1000)/2*_n1/9550*1000*2
        AB251 =AC251*0.01*(_ShaftDB2/1000)/2*_n2/9550*1000*2
        Z251 =AA251+AB251
        _PVLP =IF(_BearingType==1,X251,IF(_BearingType==2,Y251,Z251))
        _PV =_PVz+_PV0+_PVLP+_PVD
        _thetaMax = _theta0 + _PV / (_k * _Ages)
        _dthetaForRequest = _thetaMax - _thetaReq
        _PK1_Prop = IF(_DesignCooling != 3, max(_dthetaForRequest * _Ages * _k * IF(S_Units, 0.001, 1 / 3412.1), 0), 0)
        _PK1_Input = CellTransmitVal(_PK1_Prop, _PK1_Input, 油冷却能量如果使用判断值)
        _PK1 = _PK1_Input * IF(S_Units, 1000, 3412.1)
        _PK2 = IF(_DesignCooling != 3, 0, max(min(_coil * _rooil15 * _Qoil * _dthetaS, _PV - _PK1), 0))
        _thetaS =_theta0+max((_PV-_PK1-_PK2)/(_k*_Ages),0)
        _thetaE =_thetaS-_dthetaS
        AE331 = 10 ** (AC331 * LOG(_thetaE + 273) + AD331)
        _nyE =10**AE331-0.7
        _Coeff_Kv =(_nyE/55)**0.35
        _thetaMcalc =IF(_DesignCooling==3,_thetaE+16*_Coeff_Kn*_Coeff_Kv*_Coeff_Ks*_PVz/1000,_thetaS+_dtheta)
        _thetaM = _thetaMcalc

        _rooilM = _rooil15 / (1 + _kp * (_thetaM - 15))
        Z264 = 10 ** (X264 * LOG(_thetaM + 273) + Y264)
        _nyM = 10 ** Z264 - 0.7
        _eta0M = _nyM * _rooilM / 1000
        _WS = IF(OR(AND(_MatTypeW == 2, _OilType == 2), _OilType == 1), 1, 1 / _eta0M ** 0.35)  # 润滑剂结构因数WS  [ - ]
        print(_WS)
        _hminm = 21 * _h_x * _calfa ** 0.6 * _eta0M ** 0.7 * _n1 ** 0.7 * _a ** 1.39 * _Ered ** 0.03 / _T2 ** 0.13
        print(_hminm,_h_x,_calfa,_eta0M,_n1,_a,_Ered,_T2)
        _KW = _hminm * _WS * _WH  # 参数-润滑剂结构/膜厚度KW  [ - ]

        U263 = _nyM
        U264 = _eta0M
        O263 = IF(S_Units, _nyM, _nyM * 0.001550003)  # 高温下运动粘度nM  [mm**2/s]
        O264 = IF(S_Units, _eta0M, _eta0M * 0.671968975)  # 高温下动力粘度h0M  [Ns/m**2]
        O268 = _WS  # 润滑剂结构因数WS  [ - ]
        Y271 = T_Lubrication(_vgm, _KW, _LubricationIndex, 8)
        Z271 = T_Lubrication(_vgm, _KW, _LubricationIndex, 7)
        X271 = T_Lubrication(_vgm, _KW, _LubricationIndex, 6)
        _J0T = CHOOSE(_MatTypeW, X271, Y271, Z271)  # 磨损相对强度J0T  [ - ]
        _JW = _J0T * _WNS * _WML  # 材料的磨损强度JW
        O270 = _J0T  # 磨损相对强度J0T  [ - ]
        _deltaWn = _JW * _sWm
        _ds = min(_deltaWlimn, _deltaWn) / cos(_gama * pi / 180)

        _ST1 =max(min(_thetaSlim/_thetaS_B,99),0)#热量安全ST
        _SH =max(min(_sigmaHG/_sigmaHm,99),0)#蚀损安全SH
        _SW =max(min(_deltaWlimn/_deltaWn,99),0)#磨损安全SW
        Y142 =IF(X142,IF(_SH>=_SH_proposal,1,0),1)
        Y141 =IF(X141,IF(_SW>=_SW_proposal,1,0),1)
        O315 =IF(S_Units,_thetaS_B,(_thetaS_B*9/5+32))#齿轮温度JS       [°C]
        O267 =IF(S_Units,_sWm,_sWm/25.4)#滑动路径sWm  [mm]
        _Cv =IF(_v<700,X349,IF(_v<3000,Y349,Z349))#速度因数Cv
        _ny =IF(_v<10,Y350,Z350)#摩擦系数m
        _Fxm1 =IF(_PoweredWoWh==1,-_Ftm2,-_Ftm2)
        _dedendum =IF(_pitchx>0.16,1.157*_pitchx/pi,1.2*_pitchx/pi+0.002)#蜗杆蜗轮齿根高a,b[in]
        _Cm =IF(_mG<20,X348,IF(_mG<76,Y348,Z348))#传动比因数Cm

        '''A149 =CellTransmitVal(O149 & O150)
        A321 =CellTransmitVal(_kProp & _k_Input)'''
        AI315 =AI314+1
        AJ314 =AI314**0.85
        AE312 =AE311+50
        AC301 =AC300+50
        AA301 =AA300+50
        _sf2 =1.06*(_mx*pi/2-(_ds-(_dm2-_df2)*tan(_alfa0*pi/180)/cos(_gama*pi/180)))
        O243 =_YG#几何因数YG



        O274 =_deltaWn/IF(S_Units,1,25.4)#法向截面磨料磨损dWn  [mm]
        U274 =_deltaWn
        O273 =_JW#材料的磨损强度JW
        X157 =atan(_eta0T)*180/pi
        O246 = _eta0T  # 摩擦基本系数m0T
        Y157 =45-X157/2
        X269 =_WH
        T315 =_thetaS_B
        U267 =_sWm
        O180 =_SW#安全系数(磨损,蚀损)SW, SHArea[mm]
        O276 =_SW#磨损安全SW
        O316 =_ST1#热量安全ST
        P180 =_SH#安全系数(磨损,蚀损)SW, SHArea[mm]
        O286 =_SH#蚀损安全SH
        X300 =_sf2
        O221 =_pt/IF(S_Units,1,25.4)#间距: 法向/横向/轴向 pn,pt,px6.28318530717958[mm]
        _px =_pt*tan(_gama*pi/180)
        U221 =_pt
        _addendum =_pitchx/pi#蜗杆蜗轮齿根高a,b[in]
        P336 =_pitchx#圆心距,蜗杆轴距C, px[in]
        O350 =_ny#摩擦系数m
        _Lead =_NW*_pitchx#蜗杆驱动,驱动角L,l[in],[°]
        X181 =_mass3
        O339 =_Lead#蜗杆驱动,驱动角L,l[in],[°]
        X321 =_kProp
        O374 =_Fxm1*IF(S_Units,1,0.224809)#轴向力Fxm1,Fxm2[N]
        T374 =_Fxm1



        X299 =_ds
        _clearance =_dedendum-_addendum#间隙c[in]
        P340 =_dedendum#蜗杆蜗轮齿根高a,b[in]
        Z229 =_de2Prop
        Z231 =_de2min
        AD231 =_de2max
        _Dt =_D_UC+2*_addendum#蜗杆齿根径,蜗轮临界截面直径dr,Dt[in]
        _dr =_d_LC-2*_dedendum#蜗杆齿根径,蜗轮临界截面直径dr,Dt[in]
        _do1 =_d_LC+2*_addendum#蜗杆蜗轮外径do,Do[in]
        O349 =_Cv#速度因数Cv
        _Wt =_Cs*(_dm2/25.4)**0.8*_Fe*_Cm*_Cv#允许切向载荷Wt   [lbf]
        X353 =_Cs*(_dm2)**0.8*(_b2H)*_Cm*_Cv/75.948
        O351 =_Cs#材料因数Cs
        O348 =_Cm#传动比因数Cm
        O343 =_clearance#间隙c[in]
        O340 =_addendum#蜗杆蜗轮齿根高a,b[in]
        AG312 =(0.3*(AE312/25.4)**1.7)/10.7639104167097
        _deltam =(0.006592/_E1)*_l1**2*_l2**2*_Ftm2*(tan(_gama*pi/180+atan(_etazm))**2+tan(_alfa0*pi/180)**2/cos(_gama*pi/180)**2)**0.5/((1.1*_df1)**4*(_l1+_l2))
        _mass =(_mass1+_mass2+_mass3)*IF(S_Units,1,2.204624)#齿轮箱/齿轮 近似重量m[kg]
        AF312 =((400/AE312)**0.3-1)*15
        AD301 =((200/AC301)**0.5-1)*10
        AB301 =((200/AA301)**0.4-1)*10
        _Sd =max(min(_deltalim/_deltam,99),0)#蜗杆挠度安全Sd

        Y143 =IF(X143,IF(_Sd>=_Sd_Proposal,1,0),1)
        P339 =atan(_Lead/(pi*_d_LC))*180/pi#蜗杆驱动,驱动角L,l[in],[°]

        AI316 =AI315+1
        AJ315 =AI315**0.85
        AE314 =AE312+50
        AC289 =AC301+50
        AC290 =AC289+50
        AA302 =AA301+50
        _YF =2.9*_mx/_sf2#齿形因数YFZahndickenabnahme ds [mm]
        O344 =2*((_Dt/2)**2-(_D_UC/2-_addendum)**2)**0.5#蜗杆表面宽度,蜗轮表面宽度FWmax,FG[in]
        P344 =1.125*((_do1+2*_clearance)**2-(_do1-4*_addendum)**2)**0.5#蜗杆表面宽度,蜗轮表面宽度FWmax,FG[in]

        X360 =0.025*_px**0.5
        O360 =0.005*(_px/25.4)**0.5#允许蜗杆轴变形Dwmax   [in]
        O299 =_YF#齿形因数YFZahndickenabnahme ds [mm]
        _TG =_Wt*(_dm2/25.4)/2#蜗轮扭力TG   [lb*in]
        O353 =_Wt#允许切向载荷Wt   [lbf]
        X355 =_TG*0.112985005082066
        O355 =_TG#蜗轮扭力TG   [lb*in]
        O181 =_Sd#安全系数(变形,疲劳衰坏)Sd, SF
        O295 =_Sd#蜗杆挠度安全Sd
        O248 =_roz#摩擦角rz  [°]
        B2 =_px/IF(S_Units,1,25.4)
        P221 =_px/IF(S_Units,1,25.4)#间距: 法向/横向/轴向 pn,pt,px6.28318530717958[mm]
        C2 =_px*_z1/IF(S_Units,1,25.4)
        AF2 =_px*_z1/2/IF(S_Units,1,25.4)
        V221 =_px
        O253 =_PVz*IF(S_Units,0.001,0.00134102)#齿轮损失PVz  [kW]
        U253 =_PVz
        _Wf =_ny*_Wt/(cos(_gama*pi/180)*cos(_alfan*pi/180))#摩擦力Wf   [lbf]
        _Pi =_n1*_Wt*(_dm2/25.4)/(126000*_mG)+_v*_Wf/33000#额定输入功率Pi   [HP]
        _Po =_n1*_Wt*(_dm2/25.4)/(126000*_mG)#额定输出功率Po   [HP]

        O178 =_mass#齿轮箱/齿轮 近似重量m[kg]
        _TauF =_Ftm2/(_b2H*_mx)*_Yepsilon*_YF*_Ygama*_YK
        Y372 =_Ftm2*tan(_gama*pi/180+_roz*pi/180)
        O247 =_etazm#摩擦中心系数mzm
        O249 =_etaz#齿轮功率hz
        _Do2 =_Dt+_addendum#蜗杆蜗轮外径do,Do[in]
        P342 =_Dt#蜗杆齿根径,蜗轮临界截面直径dr,Dt[in]
        O342 =_dr#蜗杆齿根径,蜗轮临界截面直径dr,Dt[in]
        P341 =_Do2#蜗杆蜗轮外径do,Do[in]
        O341 =_do1#蜗杆蜗轮外径do,Do[in]
        O293 =_deltam/IF(S_Units,1,25.4)#蜗杆轴变形dm  [mm]
        O359 =_deltam/25.4#蜗杆轴变形Dw   [in]
        U293 =_deltam

        AG314 =(0.3*(AE314/25.4)**1.7)/10.7639104167097
        AF314 =((400/AE314)**0.3-1)*15
        AD290 =((200/AC290)**0.5-1)*10
        AD289 =((200/AC289)**0.5-1)*10
        AB302 =((200/AA302)**0.4-1)*10
        U344 =P344*25.4
        T344 =O344*25.4
        _SF =max(min(_TauFG/_TauF,99),0)#齿强度安全SF
        Y144 =IF(X144,IF(_SF>=_SF_Proposal,1,0),1)
        AI317 =AI316+1
        AJ316 =AI316**0.85
        AE315 =AE314+50
        AC291 =AC290+50
        AA303 =AA302+50


        X354 =_Wf*4.44822048939322
        O354 =_Wf#摩擦力Wf   [lbf]
        O306 =_TauF*IF(S_Units,1,0.145037)#齿根剪切应力tF  [MPa]
        T306 =_TauF
        P181 =_SF#安全系数(变形,疲劳衰坏)Sd, SF
        O307 =_SF#齿强度安全SF
        O358 =_Po/_Pi*100#效率h   [%]
        O357 =_Po#额定输出功率Po   [HP]
        O356 =_Pi#额定输入功率Pi   [HP]
        AA330 =_dtheta
        AG315 =(0.3*(AE315/25.4)**1.7)/10.7639104167097
        AF315 =((400/AE315)**0.3-1)*15
        AD291 =((200/AC291)**0.5-1)*10
        AB303 =((200/AA303)**0.4-1)*10
        AI318 =AI317+1
        AJ317 =AI317**0.85

        AE316 =AE315+50
        AC292 =AC291+50
        AA304 =AA303+50

        AG316 =(0.3*(AE316/25.4)**1.7)/10.7639104167097
        AF316 =((400/AE316)**0.3-1)*15
        AD292 =((200/AC292)**0.5-1)*10
        AB304 =((200/AA304)**0.4-1)*10
        AI319 =AI318+1
        AJ318 =AI318**0.85
        AE317 =AE316+50

        AC293 =AC292+50


        AA305 =AA304+50

        AG317 =(0.3*(AE317/25.4)**1.7)/10.7639104167097
        AF317 =((400/AE317)**0.3-1)*15
        AD293 =((200/AC293)**0.5-1)*10
        AB305 =((200/AA305)**0.4-1)*10

        AI320 =AI319+1
        AJ319 =AI319**0.85
        AE318 =AE317+50
        AC294 =AC293+50
        AA306 =AA305+50

        O251 =_PVLP*IF(S_Units,0.001,0.00134102)#轴承损失PVLP  [kW]
        U251 =_PVLP
        O254 =_PV*IF(S_Units,0.001,0.00134102)#总功率损耗PV  [kW]
        T334 =_PV
        U254 =_PV
        AG318 =(0.3*(AE318/25.4)**1.7)/10.7639104167097

        O322 = _PK1_Input  # 油冷却能量(内/外) 如果使用PK1       [kW]
        T322 = _PK1
        _Qoil_min_calc =(_PV-_PK1-(_Ages*_k*(_thetaReq-_theta0)))/(_coil*_rooil15*_dthetaS)
        T316 =(_PV/(_thetaS_B-_theta0))/_Ages
        AF318 =((400/AE318)**0.3-1)*15
        AD294 =((200/AC294)**0.5-1)*10
        AB306 =((200/AA306)**0.4-1)*10
        O313 =O254#总功率损耗       [kW]
        _etages =IF(_PoweredWoWh==1,_Pw2/(_Pw2+_PV/1000),(_Pw2-_PV/1000)/_Pw2)#总功率hges
        _Mk1 =IF(_PoweredWoWh==1,_Mk2/(_i*_etages),_Mk2/(_i/_etages))

        AI321 =AI320+1
        AJ320 =AI320**0.85
        AE319 =AE318+50
        AC295 =AC294+50
        AA307 =AA306+50


        Y327 =_Qoil_min_calc
        O328 =_PK2*IF(S_Units,0.001,1/3412.1)#油冷却能量PK2       [kW]
        T328 =_PK2
        _T1 =_Mk1*_KA
        _Ftm1 =2000*_T1/_dm1
        _Frm2=1#这里可能有问题
        _Frm1 =IF(_PoweredWoWh==1,_Ftm1*tan(_alfan*pi/180)/sin(_gama*pi/180+_roz*pi/180),-_Frm2)
        _Frm2=IF(_PoweredWoWh==1, -_Frm1, _Ftm2 * tan(_alfan * pi / 180) / cos(_gama * pi / 180 - _roz * pi / 180))
        _Fr2 =(_Ftm2**2+_Frm2**2)**0.5
        P376 =_Fr2*IF(S_Units,1,0.224809)#总径向力Fr1,Fr2[N]
        U376 =_Fr2
        P375 =_Frm2*IF(S_Units,1,0.224809)#径向力Frm1,Frm2[N]
        U375 =_Frm2
        T121 =_Mk1
        O179 =_etages*100#总功率 / 最大理论值mges, mmax[%]
        O255 =_etages#总功率hges
        P179 =(tan((45-_roz/2)*pi/180)/tan((45+_roz/2)*pi/180)-(_etaz-_etages))*100#总功率 / 最大理论值mges, mmax[%]
        AG319 =(0.3*(AE319/25.4)**1.7)/10.7639104167097
        AF319 =((400/AE319)**0.3-1)*15
        AD295 =((200/AC295)**0.5-1)*10
        AB307 =((200/AA307)**0.4-1)*10
        _ST =max(min(_thetaSlim/_thetaS,99),0)#热量安全ST[°C]
        O121 =IF(S_Units,1,8.850732)*_Mk1#扭矩(蜗杆/蜗轮)Mk [Nm][Nm]
        O329 =IF(S_Units,_thetaS,(_thetaS*9/5+32))#齿轮温度JS       [°C]
        _Pw1 =IF(_PoweredWoWh==1,_Pw2/_etages,_Pw2*_etages)
        _GamaErrFlag =IF(_calc_q==3,IF(_Pw1>0,2,3),IF(_Pw1>0,0,1))
        AI322 =AI321+1
        AJ321 =AI321**0.85
        AE320 =AE319+50
        AC296 =AC295+50


        T329 =_thetaS

        X322 =_thetaMax
        T330 =_thetaE
        X259 =_T1
        O330 =_ST#热量安全ST[°C]
        T119 =_Pw1
        G165 =_GamaErrFlag
        X372 =_Ftm1/tan(_gama*pi/180+_roz*pi/180)
        T394 =_Ftm1*tan(_alfan*pi/180)/sin(_gama*pi/180+T379*pi/180)
        X373 =_Ftm1*tan(_alfan*pi/180)/(sin(_gama*pi/180)+cos(_gama*pi/180)*tan(_roz*pi/180))
        O373 =_Ftm1*IF(S_Units,1,0.224809)#切向力Ftm1,Ftm2[N]
        T373 =_Ftm1
        Y322 =_dthetaForRequest
        _ShaftDA1 =(1.77*10000000*_Pw1/_n1)**0.333#     主要动力传送轴DA[mm]
        _ShaftDB1 =(0.83*10000000*_Pw1/_n1)**0.333#     小的,短轴DB[mm]
        AG320 =(0.3*(AE320/25.4)**1.7)/10.7639104167097
        _Qoil_min =(_Pw1**0.75)/100
        U364 =(_Ftm1**2+_Ftm2**2)**0.5
        AF320 =((400/AE320)**0.3-1)*15
        AD296 =((200/AC296)**0.5-1)*10
        X394 =T394/sin(_alfan*pi/180)
        _Qoil_prop =max(_Qoil_min_calc,_Qoil_min)
        O119 =IF(S_Units,_Pw1,_Pw1/ 0.745701033541632)#传动功率Pw [kW][kW]#显示值
        U377 =IF(_PoweredWoWh==1,_Ftm1/(cos(_alfan*pi/180)*(sin(_gama*pi/180)+_etaz*cos(_gama*pi/180))),_Ftm1/(cos(_alfan*pi/180)*(sin(_gama*pi/180)-_etaz*cos(_gama*pi/180))))
        _Fxm2 =IF(_PoweredWoWh==1,-_Ftm1,-_Ftm1)

        _Flag_d1min =IF(_df1<_ShaftDB1,1,0)

        #A327 =CellTransmitVal(_Qoil_prop & _Qoil)
        #A322 =CellTransmitVal(_PK1_Prop & _PK1_Input)
        AI323 =AI322+1
        AJ322 =AI322**0.85
        AE321 =AE320+50

        O405 =_ShaftDB1#     小的,短轴DB[mm]
        O404 =_ShaftDA1#     主要动力传送轴DA[mm]
        X327 =_Qoil_prop
        Z327 =_Qoil_min
        Z322 =_PK1_Prop
        P374 =_Fxm2*IF(S_Units,1,0.224809)#轴向力Fxm1,Fxm2[N]
        U374 =_Fxm2
        _F_N =_Frm1/sin(_alfan*pi/180)
        _Fn =_Frm1/sin(_alfan*pi/180)
        O375 =_Frm1*IF(S_Units,1,0.224809)#径向力Frm1,Frm2[N]
        T375 =_Frm1
        O377 =_Fn*IF(S_Units,1,0.224809)#法向力Fn[N]
        T377 =_Fn
        U164 =_Flag_d1min
        X377 =_F_N*cos(_alfan*pi/180)
        X374 =_F_N
        AG321 =(0.3*(AE321/25.4)**1.7)/10.7639104167097
        U365 =(_Ftm1**2+_Ftm2**2+_Frm1**2)**0.5
        _Fr1 =(_Ftm1**2+_Frm1**2)**0.5
        _GearF =(_Frm1**2+_Ftm2**2)**0.5
        _WormF =(_Frm1**2+_Ftm1**2)**0.5
        AF321 =((400/AE321)**0.3-1)*15
        X375 =X377*tan(_roz*pi/180)
        V365 =U365*cos(_alfan*pi/180)
        AI325 =AI323+1
        AJ323 =AI323**0.85
        AE322 =AE321+50

        X291 =_WormF
        AB331 =_nyE
        _ForceRA =_l2*_WormF/(_l1+_l2)
        _ForceRB =_l1*_WormF/(_l1+_l2)
        X292 =_GearF
        O376 =_Fr1*IF(S_Units,1,0.224809)#总径向力Fr1,Fr2[N]
        T376 =_Fr1
        O292 =_ForceRB*IF(S_Units,1,0.224809)#右轴承反作用力RB  [N]
        U292 =_ForceRB
        O291 =_ForceRA*IF(S_Units,1,0.224809)#左轴承反作用力RA  [N]
        U291 =_ForceRA
        AG322 =(0.3*(AE322/25.4)**1.7)/10.7639104167097

        AF322 =((400/AE322)**0.3-1)*15

        AI326 =AI325+1
        AJ325 =AI325**0.85
        AE323 =AE322+50

        T331 =_thetaMcalc
        U261 =_thetaM

        Y331 =_Coeff_Kv
        AG323 =(0.3*(AE323/25.4)**1.7)/10.7639104167097
        AF323 =((400/AE323)**0.3-1)*15
        O331 =IF(S_Units,_thetaMcalc,(_thetaMcalc*9/5+32))#轮温度JM       [°C]
        O262 =IF(S_Units,_rooilM,_rooilM/62.4278178356276)#高温下润滑剂密度roilM  [kg/dm**3]
        AI327 =AI326+1
        AJ326 =AI326**0.85
        AE325 =AE323+50
        AE326 = AE325 + 50
        AE327 = AE326 + 50

        U262 =_rooilM
        AG325 =(0.3*(AE325/25.4)**1.7)/10.7639104167097
        AF325 =((400/AE325)**0.3-1)*15
        O261 =O331#轮温度JM  [°C]
        AJ327 =AI327**0.85
        AG326 = (0.3 * (AE326 / 25.4) ** 1.7) / 10.7639104167097
        AF326 = ((400 / AE326) ** 0.3 - 1) * 15
        U265 =_hminm
        AG327 =(0.3*(AE327/25.4)**1.7)/10.7639104167097
        AF327 =((400/AE327)**0.3-1)*15
        O265 =IF(S_Units,_hminm,_hminm*39.37007874)#润滑剂平均膜厚度hminm  [micrometer]
        O269 =_KW#参数-润滑剂结构/膜厚度KW  [ - ]
        print('齿根强度安全_SF',_SF)
        print('蚀损安全',_Sd)
        print('涡轮蜗杆外径_do1',_do1)
        print('蜗杆轴变形O293',O293)
        print('齿根剪切应力O306',O306)
        print('总径向力O376',O376)
        print('平均接触面应力O259',O259)
        涡轮类型值 = ['ZA (A)蜗轮', 'ZN (N) 蜗轮', 'ZI (I) 蜗轮', 'ZK (K) 蜗轮', 'ZH (C) 蜗轮']
        负载类型值 = ['A…连续的', 'B…轻的震动', 'C…中等的震动', 'D….重的震动']
        润滑油类型值 = ['矿物油', '聚 α 稀烴油润滑 (PAO)', '聚乙二醇油润滑 (PEG)']
        润滑方式值 = ['蜗杆油浸没润滑', '蜗轮油浸没润滑', '油喷润滑']
        齿轮箱的加强肋值 = ['无加强筋接合', '晶格结构无加强筋', '部分加强筋', '最佳加强筋']
        if _TeethOrientation==1:
                倾斜类型='右'
        else:
                倾斜类型 = '左'
        安全返回值 = {'输入参数：': ('',''),
                 '传动功率': (_Pw2_Input, 'kw'), '蜗杆转速': (_n1, 'r/min'), '传动比': (_iin, ''),
                 '输入材料,加载条件,生产参数：': ('----------------', '------------------'),
                 '涡杆材料': (INDEX2(T_MatTblWorm,_MatP,'材料名称(GB)'), ''),
                 '涡轮材料': (INDEX2(T_MatTblWheel, _MatW, '材料名称(GB)'), ''),'涡轮类型': (涡轮类型值[_ToothType-1], ''), '涡杆负载类型': (负载类型值[_LoadTypeA-1], ''), '涡轮负载类型': (负载类型值[_LoadTypeB-1], ''),
                 '润滑油类型': (润滑油类型值[_DesignCooling-1], ''), '润滑方式': (润滑方式值[_OilType-1], ''), '润滑油': (1, ''),
                 '蜗杆的平均粗糙度': (_Ra_Input, 'microm'),'运用因数': (_KA, ''),'期望寿命': (_Lh, 'h'),
                 '目标磨损安全': (_Sd_Proposal, ''), '目标蚀损安全': (_SH_proposal, ''), '目标蜗杆挠度安全': (_SF_Proposal, ''),'目标齿强度安全': (_SW_proposal, ''),
                 '输入齿形设计：': ('--------------------', '--------------------------'),
                 '齿根高系数': (_haXP, ''), '动力头间隙': (_caXP, ''),'齿根半径系数': (_rf1, ''),
                 '输入几何设计：': ('--------------------', '--------------------------'),
                 '蜗杆齿数输入': (_z1, ''),
                 '蜗杆中心直径输入': (_d1_Input, 'mm'), '轴向压力角': (_alfa_temp, ''), '螺旋角输入': (_gama, '°'), '直径率': (_q, ''),
                 '倾斜角': (倾斜类型, ''), '模数额定值': (_m_Input, ''), '左轴承距离百分比': (_l1_proc, ''), '右轴承距离百分比': (_l2_proc, ''),
                 '蜗轮齿顶修正系数': (_x2, ''), '所需圆心距当前的': ( _a_req1_Input, 'mm'), '左右轴承距离左': (_l1_input, 'mm'),
                 '左右轴承距离右': ( _l2_input, 'mm'),
                 '蜗杆表面宽度输入': (_L_Input, 'mm'), '蜗轮表面宽度输入': (_b2H_Input, 'mm'),
                 '输出参数输入参考：': ('------', '-----'),
                 '100度润滑油粘度值': (_ny100, '[mm^2/s]'), '40度润滑油粘度值': (_ny40, '[mm^2/s]'),'15度润滑油粘度值': (_rooil15_Input, '[mm^2/s]'),
                 '蜗杆圆周齿距': (_CP, 'mm'), '涡轮圆周齿距': (_DP, 'MM'),'齿侧允许磨损': (_deltaWlimn30, 'mm'),
                '安全系数磨损': (O180,''), '安全系数蚀损': (P180,''), '安全系数变形': (O181,''), '安全系数疲劳': (P181,''),
                 '输出参数基本尺寸：': ('--------------------', '--------------------------'),
                 '模数法向': (M220, 'mm'), '模数横向': (O220, 'mm'), '模数轴向': (P220, 'mm'),
                 '间距法向': (M221, 'mm'), '间距横向': (O221, 'mm'), '间距轴向': (P221, 'mm'),
                 '压力角法向': (_alfan, '°'), '压力角横向': (_alfat, '°'), '压力角轴向': (_alfax, '°'),
                 '蜗杆齿数': (O223, ''), '涡轮齿数': (P223, ''),
                 '蜗杆齿顶圆直径': (O224, 'mm'), '蜗轮齿顶圆直径': (P224, 'mm'),
                 '蜗杆参考直径': (O225, 'mm'), '涡轮参考直径': (P225, 'mm'),
                 '蜗杆齿根圆直径': (O226, 'mm'), '涡轮齿根圆直径': (P226, 'mm'),
                 '蜗杆节圆柱直径': (O227, 'mm'), '涡轮节圆柱直径': (P227, 'mm'),
                 '蜗杆中心直径': (O228, 'mm'), '涡轮中心直径': (P228, 'mm'),
                 '蜗轮外径': (_de2Input, 'mm'),
                 '蜗杆齿轮顶高': (O230, 'mm'), '涡轮顶高': (P230, 'mm'),
                 '蜗杆齿根高': (O231, 'mm'), '涡轮齿根高': (P231, 'mm'),
                 '圆心距': (O232, 'mm'),
                 '蜗杆表面宽度': (O233, 'mm'), '涡轮表面宽度': (P233, 'mm'),
                 '螺旋角': (O234, '°'), '中心直径': (P234, 'mm'),
                 '蜗杆法向面齿厚': (O235, 'mm'), '蜗轮法向面齿厚': (P235, 'mm'),
                 '蜗杆中心面齿厚': (O236, 'mm'), '涡轮中心面齿厚': (P236, 'mm'),
                 '蜗杆法向面齿间隙厚度': (O237, 'mm'), '涡轮法向面齿间隙厚度': (P237, 'mm'),
                 '蜗杆中心面齿间隙厚度': (O238, 'mm'), '涡轮中心面齿间隙厚度': (P238, 'mm'),
                 '效率和损失(DIN 3996)输出': ('------------', '-----------'),
                 '滑动速度': (O241, 'm/s'), '比例系数': (_YS, ''),
                 '几何因数': (_YG, ''), '材料因数': (_YW, ''),
                 '表面耐久性粗糙因素': (_YR, ''), '摩擦基本系数': (_eta0T, ''),
                 '摩擦中心系数': (_etazm, ''), '摩擦角': (_roz, '°'),
                 '齿轮功率': (_etaz, ''), ' 无负载损失': (O250, 'KW'),
                 '轴承损失': (O251, 'KW'), '密封损失': (O252, 'KW'),
                 '齿轮损失': (O253, 'KW'), '总功率损耗': (O254, 'KW'),
                 '总功率': (_etages, ''),
                 '磨损负载能力(DIN 3996)输出': ('------------', '-----------'),
                 '相等的弹性模量E': (O258, 'Mpa'), '平均接触面应力': (O259, 'Mpa'),
                 '恒量的, 用于代替粘度指数': (_calfa, '[m^2/N]'), '轮温度输入': (O261, '°'),
                 '高温下润滑剂密度': (O262, 'kg/dm^3'),
                 '高温下运动粘度': (O263, '[mm^2/s]'), '高温下动力粘度': (O264, 'Ns/m^2'),
                 '润滑剂平均膜厚度': (O265, 'micrometer'),'负载周期': (_NL, ''),
                  '滑动路径': (O267, 'mm'),
                 '润滑剂结构因数': (_WS, ''), '参数 - 润滑剂结构 / 膜厚度': (_KW, ''),
                 '磨损相对强度': (_J0T, ''), '抬高系数 / 每小时开始数': (_WNS, ''),
                 '材料 / 润滑剂因数 - 磨损': (_WML, ''), '材料的磨损强度': (_JW, ''),
                 '法向截面磨料磨损': (O274, 'mm'), '齿侧允许磨损输出': (_deltaWlimn_Input, 'mm'),
                 '磨损安全': (_SW, ''),
                 '蚀损阻抗(DIN 3996)输出': ('------------', '-----------'),
                 '寿命因数': (_Zh, ''), '速度因数': (_Zv, ''),
                 '尺寸因数': (_Zs, ''), '传动比因数': (_Zu, ''),
                 '润滑因数': (_Zoil, ''), '蚀损阻抗': (O284, 'Mpa'),
                 '接触面应力极限值': (O285, 'Mpa'), '蚀损安全': (_SH, ''),
                 '蜗杆挠度输出': ('-----------', '-------------'),
                 '左轴承间距': (O289, 'mm'), '右轴承间距': (O290, 'mm'),
                 '左轴承反作用力': (O291, 'N'), '右轴承反作用力': (O292, 'N'),
                 '蜗杆轴变形': (O293, 'mm'), '允许蜗杆轴变形': (O294, 'mm'),
                 '蜗杆挠度安全': (_Sd, ''),
                 '齿根强度(DIN 3996)输出': ('-------------', '---------------'),
                 '齿轮齿数比因数': (_Yepsilon, ''), '齿形因数': (_YF, ''),
                 '主要因数': (_Ygama, ''), '轮缘厚度': (_SKInput, 'mm'),
                 '轮缘厚度系数': (_YK, ''), '寿命因数 / 精度等级': (_YNL, ''),
                 '剪切抵抗极限': (O304, 'MPa'), '齿根剪切应力极限值': (O305, 'MPa'),
                 '齿根剪切应力': (O306, 'MPa'), '齿强度安全': (_SF, ''),
                 '热量安全(DIN 3996)输出': ('-------------', '---------------'),
                 '齿轮温度': (_Ygama, '°'), '热量安全': (_SKInput, ''),
                 '轮温度': (_YK, '°'), '齿轮箱的加强肋': (齿轮箱的加强肋值[_GboxAreaType-1], ''),
                 '圆柱蜗轮尺寸(AGMA 6022-C93)输出': ('-------------', '---------------'),
                 '蜗杆齿数输出': (_NW, ''), '蜗轮 齿数': (_NG, ''),
                 '传动比输出': (_mG, ''), '圆心距输出': (_C, ''),
                 '蜗杆轴距输出': (_pitchx, 'in'),
                 '蜗杆节径(推荐)': ('o337', ''), '蜗杆节径': (_d_LC, 'in'),
                 '蜗轮节径': (_D_UC, 'in'), '蜗杆驱动': (_Lead, 'in'),
                 '驱动角': (P339, ''),
                 '蜗杆齿根高输出': (_addendum, 'in'), '蜗轮齿根高输出': (_dedendum, 'in'),
                 '蜗杆外径输出2a': (_do1, 'in'), '蜗杆外径输出2a': (_Do2, 'in'),
                 '蜗杆齿根径': (_dr, 'in'), '蜗轮临界截面直径': (_Dt, 'in'),
                 '间隙': (_clearance, 'in'), '蜗杆表面宽度输出': (O344, 'in'),
                 '蜗轮表面宽度': (P344, 'in'),
                 '安全(ANSI/AGMA 6034-B92)输出': ('-------------', '---------------'),
                 '滑动速度AGMA': (_v, 'ft/min'), '传动比因数AGMA': (_Cm, ''),
                 '速度因数AGMA': (_Cv, ''), '摩擦系数': (_ny, ''),
                 '材料因数AGMA': (_Cs, ''),
                 '有效表面宽度': (_Fe, ''), '允许切向载荷': (_Wt, 'lbf'),
                 '摩擦力': (_Wf, 'lbf'), '蜗轮扭力': (_TG, ''),
                 '额定输入功率': (_Pi, 'HP'),
                 '额定输出功率': (_Po, 'HP'), '效率': (O358, ''),
                 '蜗杆轴变形AGMA': (O359, ''), '允许蜗杆轴变形AGMA': (O360, ''),
                 '力作用条件(压力作用在齿轮上)输出': ('-------------', '---------------'),
                 '蜗杆圆周速度': (O372, 'm/s'), '蜗轮圆周速度': (P372, 'm/s'),
                 '蜗杆切向力': (O373, 'N'), '蜗轮切向力': (P373, 'N'),
                 '蜗杆轴向力': (O374, 'N'), '蜗轮轴向力': (P374, 'N'),
                 '蜗杆径向力': (O375, 'N'), '蜗轮径向力': (P375, 'N'),
                 '蜗杆总径向力': (O376, 'N'), '蜗轮总径向力': (P376, 'N'),
                 '法向力': (O377, 'N'),
                 '选择材料的参数输出': ('-------------', '---------------'),
                 '蜗杆密度': (_Ro1, 'kg/m^3'), '蜗轮密度': (_Ro2, 'kg/m^3'),
                 '蜗杆杨氏模量(弹性模数)': (_E1, 'GPa'), '蜗轮杨氏模量(弹性模数)': (_E2, 'GPa'),
                 '蜗杆抗张强度-极限': (O382, 'MPa'), '蜗轮抗张强度-极限': (P382, 'MPa'),
                 '蜗杆抗张强度-收缩率': (O383, 'MPa'), '蜗轮抗张强度-收缩率': (P383, 'MPa'),
                 '蜗杆损坏率': (_Poison1, ''), '蜗轮损坏率': (_Poison2, ''),
                 '蜗杆接触疲劳极限': (_ContactLimit1, 'MPa'), '蜗轮接触疲劳极限': (_ContactLimit2, 'MPa'),
                 '蜗杆弯曲疲劳极限': (_BendingLimit1, 'MPa'), '蜗轮弯曲疲劳极限': (_BendingLimit2, 'MPa'),
                 '蜗杆齿的边缘硬度': (_VHV1, 'HV'), '蜗轮齿的边缘硬度': (_VHV2, 'HV'),
                 '蜗杆齿的中心硬度': (O388, 'HV'), '蜗轮齿的中心硬度': (P388, 'HV'),
                 '蜗杆接触负荷循环基数': (_NHLim1, ''), '蜗轮接触负荷循环基数': (_NHLim2, ''),
                 '蜗杆接触疲劳说明线图': (_qH1, ''), '蜗轮接触疲劳说明线图': (_qH2, ''),
                 '蜗杆弯曲负荷循环基数': (_NFLim1, ''), '蜗轮弯曲负荷循环基数': (_NFLim2, ''),
                 '蜗杆弯曲疲劳说明线图': (_qF1, ''), '蜗轮弯曲疲劳说明线图': (_qF2, ''),
                 }

        return 安全返回值
if __name__=="__main__":
     计算涡轮()