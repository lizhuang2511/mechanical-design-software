from excel公式python版本螺纹传动 import IF
from excel公式python版本螺纹传动 import INDEX,CHOOSE,OR,LOG,LN,ROUND,AND,CellTransmitVal,T_Lubrication,Atan,Pmax_SecFormula,Smax_SecFormula,vlookup4
from math import *
def 传动螺栓计算(_Q_input=10000,
    _n_req=200,
    _f=0.08,
    _d_input=26,
    _d1_input=23,
    _d2_input=24.5,
    _d3_input=22.5,
    _d4_input=26.5,
    _P_input=3,
    _ns=1,
    _alfa1_input=15,
    _alfa2_input=15,_MatID_Screw=4,_MatID_Nut=8,
    _JournalBT=1,_KFactor=2,_EccRatioID=3,
    _fj = 0.1,
    _dj_input = 32,
    _dx_input = 250,
    _rev_input = 83.3333333333333,
    _Ls_input = 1000,
    _ro_input = 7850,
    _E_input = 206000,
    _Rp02_input = 320,
    _pD_input = 18.75,
    _SRcs = 17.9,
    _SRc = 112.7,
    _Lef_coef = 0.8,
    _ecc = 0.1,
    _h_nut_input = 24,
    _nzmax = 8,
    _nts = 333,
    _ntn = 8,
    _DN = 52,
    _SFA = 2,
    _SFC_prop = 1.5,
    _SFB_1 = 1.75,
    _nzmax_prop = 8,
    _SFC = 1.25,
    S_ExtraCopy_FlagIN = 1,
):
    FALSE=False
    TRUE=True
    S_HRA00=0
    S_HRA01=1
    _dx_Flag=1
    S_HRA02=1
    #XM_ErrMsg1=计算无误。
    _UnitsPT_BCKP=1
    #XM_ErrMsg2=检查行：
    _UnitsPT=2
    _MatID_Screw=_MatID_Screw
    _MatID_Nut=_MatID_Nut
    #_ScrewA_ID=_ScrewA_ID
    _JournalBT=_JournalBT
    _KFactor=_KFactor
    _EccRatioID=_EccRatioID
    S_DXFOutPt=1
    S_DXFScaleID=1


    _Q_input=_Q_input
    #_v_input=_v_input
    _f=_f
    _d_input=_d_input
    _d1_input=_d1_input
    _d2_input=_d2_input
    _d3_input=_d3_input
    _d4_input=_d4_input
    _P_input=_P_input
    _ns=_ns
    _alfa1_input=_alfa1_input
    _alfa2_input=_alfa2_input
    _fj=_fj
    _dj_input=_dj_input
    _dx_input=_dx_input
    _rev_input=_rev_input
    _Ls_input=_Ls_input
    _ro_input=_ro_input
    _E_input=_E_input
    _Rp02_input=_Rp02_input
    _pD_input=_pD_input
    _SRcs=_SRcs
    _SRc=_SRc
    _Lef_coef=_Lef_coef
    _ecc=_ecc
    _h_nut_input=_h_nut_input
    _nzmax=_nzmax
    _nts=_nts
    _ntn=_ntn
    _DN=_DN
    _SFA=_SFA
    _SFC_prop=_SFC_prop
    _SFB_1=_SFB_1
    _nzmax_prop=_nzmax_prop
    _SFC=_SFC
    S_ExtraCopy_FlagIN=S_ExtraCopy_FlagIN
    S_Units=True

    B148 =IF(_dx_Flag==1,FALSE,TRUE)
    B149 =IF(_dx_Flag==1,TRUE,FALSE)

    #C104 =IF(H104,1,0)
    #C105 =IF(H105,1,0)
    #C106 =IF(H106,1,0)
    #C107 =IF(H107,1,0)
    #C108 =IF(H108,1,0)
    #C109 =IF(H109,1,0)
    R168 =_Ls_input*_Lef_coef
    T_KFactor='T_KFactor'
    T_MaterialA='T_MaterialA'
    T_ScrewA='T_ScrewA'
    _SrewATblName='_SrewATblName'
    T_Friction1='T_Friction1'
    T_Friction2='T_Friction2'
    T_Pressure3='T_Pressure3'
    R181 =INDEX(T_KFactor,_KFactor,8)
    R182 =(INDEX(T_KFactor,_KFactor,7)*1000)*IF(S_Units,1,1/25.4)
    _ro_Screw_Tbl =INDEX(T_MaterialA,_MatID_Screw,11)
    _E_Screw_Tbl =INDEX(T_MaterialA,_MatID_Screw,10)
    _Rp02_Screw_Tbl =INDEX(T_MaterialA,_MatID_Screw,9)
    #S161 ="< "+str(ROUND(_Rp02_input*0.6,2))
    #S162 ="< "&ROUND(_Rp02_input,2)
    #S163 ="< "&ROUND(_Rp02_input,2)
    _Lef_coef_Tbl =INDEX(T_KFactor,_KFactor,4)
    #S187 ="< "&ROUND(_pD_input,2)
    #AD105 =INDEX(T_ScrewA,_ScrewA,3)
    #AD106 =INDEX((_SrewATblName),_ScrewA_ID,1)#INDIRECT
    AD119 =INDEX(T_Friction1,_MatID_Screw,_MatID_Nut)
    _Q =_Q_input/IF(S_Units,1,0.224809)
    #_v =_v_input/IF(S_Units,1000,39.37007874)

    _f_Tbl =INDEX(T_Friction2,_MatID_Screw,_MatID_Nut)#这里检查输入数据
    _pD_prop =INDEX(T_Pressure3,_MatID_Screw,_MatID_Nut)
    #_SrewATblName =INDEX(T_ScrewA,_ScrewA,4)
    _SrewATblName =_SrewATblName
    _d =_d_input/IF(S_Units,1,1/25.4)
    _d1 =_d1_input/IF(S_Units,1,1/25.4)
    _d2 =_d2_input/IF(S_Units,1,1/25.4)
    _d3 =_d3_input/IF(S_Units,1,1/25.4)
    _d4 =_d4_input/IF(S_Units,1,1/25.4)
    _P =_P_input/IF(S_Units,1,1/25.4)
    _L =_P*_ns

    AD134 =Atan(_f)*180/pi
    _alfa1 =IF(_alfa1_input<0.0001,0.0001,_alfa1_input)
    AD137 =IF(_alfa1==0,0.0001,tan(_alfa1*pi/180))
    _dj =_dj_input/IF(S_Units,1,1/25.4)
    _Mkj =IF(_JournalBT==1,0,_Q*_fj*(_dj/1000)/2)
    _Mkup =_Q*_d2/2*((_L*cos(_alfa1*pi/180)+pi*_f*_d2)/(pi*_d2*cos(_alfa1*pi/180)-_f*_L))/1000+_Mkj#起重扭矩
    _Mkdw =_Q*_d2/2*((pi*_f*_d2-_L*cos(_alfa1*pi/180))/(pi*_d2*cos(_alfa1*pi/180)+_f*_L))/1000+_Mkj
    _rev =(_dx_input/IF(S_Units,1,1/25.4))/_L
    _dx =_rev_input*_L*IF(S_Units,1,1/25.4)
    _Ls =_Ls_input/IF(S_Units,1,1/25.4)
    _ro =_ro_input/IF(S_Units,1,0.0624278178356276)
    _E =_E_input/IF(S_Units,1,0.145037)
    _Rp02 =_Rp02_input/IF(S_Units,1,0.145037)
    _pD =_pD_input/IF(S_Units,1,0.145037)
    _SigmaT =16*_Mkup/(pi*(_d3/1000)**3)/1000000#16/3.14大约是5*扭矩见清华书机械设计教程第100页
    _Sigma =4*_Q/(pi*(_d3/1000)**2)/1000000#d3为齿根直径清华书第100页
    _SigmaRed =(_Sigma**2+3*_SigmaT**2)**0.5
    _A =pi*_d3**2/4
    _Ix =pi*_d3**4/64
    _rx =(_Ix/_A)**0.5
    _y =_d3/2
    T_ScrewA='T_ScrewA'
    T_EccRatio='T_EccRatio'
    #T_DXFScale=''
    _mass =pi*(_d2/1000)**2/4*(_Ls/1000)*_ro
    _ecc_ratio =INDEX(T_EccRatio,_EccRatioID,1)
    _excentricity =_ecc*_rx**2/_y
    _SigmaScrew =_Q/_A*(1+_ecc*(1/cos((_Ls*_Lef_coef)/(2*_rx)*(_Q/(_E*_A))**0.5)))
    _h_nut =_h_nut_input/IF(S_Units,1,1/25.4)
    _nz_calc =ROUND(_h_nut/_P,2)
    #S_DXFScale =INDEX(T_DXFScale,S_DXFScaleID,2)
    #_DXF_AutoScale =IF(S_Units,1,25.4)*_d/100
    S_ExtraCopy_FlagOUT =2*S_ExtraCopy_FlagIN
    #S_TUnits =INDEX(T_ScrewA,_ScrewA,5)
    S_TUnits =True
    #_d_tbl =INDEX(T_ScrewA,_ScrewA,14)*IF(S_TUnits,1,25.4)*IF(S_Units,1,1/25.4)
    #_d_tbl =_d_tbl
    #_d1_tbl =INDEX(T_ScrewA,_ScrewA,16)*IF(S_TUnits,1,25.4)*IF(S_Units,1,1/25.4)
    #_d1_tbl =_d1_tbl
    #_d2_tbl =INDEX(T_ScrewA,_ScrewA,17)*IF(S_TUnits,1,25.4)*IF(S_Units,1,1/25.4)
    #_d2_tbl =_d2_tbl
    #_d3_tbl =INDEX(T_ScrewA,_ScrewA,19)*IF(S_TUnits,1,25.4)*IF(S_Units,1,1/25.4)
    #_d3_tbl =_d3_tbl
    #_d4_tbl =INDEX(T_ScrewA,_ScrewA,20)*IF(S_TUnits,1,25.4)*IF(S_Units,1,1/25.4)
    #_d4_tbl =_d4_tbl
    #_P_tbl =INDEX(T_ScrewA,_ScrewA,9)*IF(S_TUnits,1,25.4)*IF(S_Units,1,1/25.4)
    #_P_tbl =_P_tbl
    _alfa2 =IF(_alfa2_input<0.0001,0.0001,_alfa2_input)
    AE137 =IF(_alfa2==0,0.0001,tan(_alfa2*pi/180))
    _dj_prop =ROUND((_d+2*_P)*IF(S_Units,1,1/25.4),IF(S_Units,1,2))
    T_Coeff_pD='T_Coeff_pD'
    _gama = Atan(_L / (_d2 * pi)) * 180 / pi
    _v_req = (_n_req / (60 / (pi * (_d2 / 1000) * tan(_gama * pi / 180)))) * IF(S_Units, 1000, 39.37007874)
    _v=_v_req
    _pD_coeff =vlookup4(_v,T_Coeff_pD,2)
    T_Pressure1='T_Pressure1'
    T_Pressure2='T_Pressure2'
    print(_MatID_Nut,_MatID_Screw,INDEX(T_Pressure1,_MatID_Screw,_MatID_Nut+1))
    _PressMin=ROUND(INDEX(T_Pressure1,_MatID_Screw,_MatID_Nut+1)*_pD_coeff*IF(S_Units,1,0.145037),2)
    _PressMax=ROUND(INDEX(T_Pressure2,_MatID_Screw,_MatID_Nut+1)*_pD_coeff*IF(S_Units,1,0.145037),2)
    _pD_Tbl=ROUND((_PressMin+_PressMax)/2,2)
    d2_prop =(_Q/(pi*0.5*2*((_pD_Tbl/IF(S_Units,1,0.145037))/_SFC_prop)))**0.5
    AF123=d2_prop
    AE152 =10*AF123
    AE166 =ROUND(0.5*(_E/(_Rp02*0.5))**0.5,1)
    AE167 =ROUND((_E*pi**2/(_Rp02*0.5))**0.5,1)
    _qm =_mass*9.81/(_Ls/1000)
    _excentricity_input=0.15
    _ecc_req =_excentricity_input/IF(S_Units,1,1/25.4)
    _h_nut_prop =ROUND(_P*8*IF(S_Units,1,1/25.4),IF(S_Units,1,2))
    S_ItoM =IF(S_Units,25.4,1)
    #_alfa1_tbl =INDEX(T_ScrewA,_ScrewA,7)
    #_alfa1_tbl =_alfa1_tbl
    AF137 =AD137+AE137
    T_Pressure1='T_Pressure1'
    _Pressmin =ROUND(INDEX(T_Pressure1,_MatID_Screw,_MatID_Nut+1)*_pD_coeff*IF(S_Units,1,0.145037),2)
    _ecc_ratio_req =_ecc_req/_rx**2*_y
    _nz_input=8
    _h_nut_calc =_P*_nz_input*IF(S_Units,1,1/25.4)
    S_MtoI =IF(S_Units,1,1/25.4)
    #_alfa2_tbl =INDEX(T_ScrewA,_ScrewA,8)
    #_alfa2_tbl =_alfa2_tbl
    #AG127 =INDEX((_SrewATblName),_ScrewA_ID,1)#INDIRECT
    AG137 =_P/AF137*AD137
    T_Pressure2='T_Pressure2'
    _PressMax =ROUND(INDEX(T_Pressure2,_MatID_Screw,_MatID_Nut)*_pD_coeff*IF(S_Units,1,0.145037),2)
    AG169 =pi*_d3**2/4*(0.4+0.6*_d/_d3)
    _Ix_prec =pi*_d3**4/64*(0.4+0.6*_d/_d3)
    _SFB_3 =3.5
    AG187 =1/4*pi*((_d/1000)**2-(_d1/1000)**2)
    AH137 =_P/AF137*AE137

    AH169 =pi*_d**2/4
    _H =AG137/AD137
    AI137=_H
    _Hup =0.5*AI137
    _Hdw =0.5*AI137
    _d0 =_d2-2*_Hdw
    _d5 =_d2+2*_Hup
    _pD_Tbl =ROUND((_Pressmin+_PressMax)/2,2)
    _SRcs_rec = ROUND(0.5*(_E / (_Rp02 * 0.5))**0.5,1)
    _SRc_rec = ROUND((_E * pi**2 / (_Rp02 * 0.5))**0.5,1)
    _DN_Prop =ROUND(_d*2*IF(S_Units,1,1/25.4),2)
    _Pressmin =ROUND(INDEX(T_Pressure1,_MatID_Screw,_MatID_Nut+1)*_pD_coeff*IF(S_Units,1,0.145037),2)
    _nz =ROUND(_h_nut/_P,2)
    AH187 =AG187*min(_nz,_nzmax)
    _Hdw =0.5*AI137
    _Hup =0.5*AI137
    #A126 =CellTransmitVal(_d_tbl , _d_input,True)
    #A127 =CellTransmitVal(_d1_tbl , _d1_input,True)
    #A128 =CellTransmitVal(_d2_tbl , _d2_input,True)
    #A129 =CellTransmitVal(_d3_tbl , _d3_input,True)
    #A130 =CellTransmitVal(_d4_tbl , _d4_input,True)
    #A131 =CellTransmitVal(_P_tbl , _P_input,True)
    #A135 =CellTransmitVal(_alfa1_tbl , _alfa1_input,True)
    #A136 =CellTransmitVal(_alfa2_tbl , _alfa2_input,True)
    A148 =CellTransmitVal(_dx , _dx_input,True)
    A149 =CellTransmitVal(_rev , _rev_input,True)
    A154 =CellTransmitVal(_ro_Screw_Tbl , _ro_input,True)
    A155 =CellTransmitVal(_E_Screw_Tbl , _E_input,True)
    A156 =CellTransmitVal(_Rp02_Screw_Tbl , _Rp02_input,True)
    A157 =CellTransmitVal(_pD_Tbl , _pD_input,True)
    A158 =CellTransmitVal(_SRcs_rec , _SRcs,True)
    A159 =CellTransmitVal(_SRc_rec , _SRc,True)
    A195 =CellTransmitVal(_DN_Prop , _DN,True)
    R133 =_L*IF(S_Units,1,1/25.4)
    R140 =_Mkj*IF(S_Units,1,0.737651)
    R141 =_Mkup*IF(S_Units,1,0.737651)#起重力
    R142 =_Mkdw*IF(S_Units,1,0.737651)#下降力
    _eta =_Q*(_L/1000)/(2*pi*_Mkup)#效率
    _n =_v*60/(pi*(_d2/1000)*tan(_gama*pi/180))#
    R161 =_SigmaT*IF(S_Units,1,0.145037)
    R162 =_Sigma*IF(S_Units,1,0.145037)
    R163 =_SigmaRed*IF(S_Units,1,0.145037)#等效应力
    _SFAcalc =_Rp02/_SigmaRed
    R169 =_A*IF(S_Units,1,(1/25.4)**2)
    R170 =_Ix*IF(S_Units,1,(1/25.4)**4)
    R171 =_rx*IF(S_Units,1,1/25.4)
    R172 =_y*IF(S_Units,1,1/25.4)
    R173 =_mass*IF(S_Units,1,2.204624)
    _SR =_Ls*_Lef_coef/_rx
    R176 =_excentricity*IF(S_Units,1,1/25.4)
    R177 =_SigmaScrew*IF(S_Units,1,0.145037)
    S122 =AD119
    #S157 =_Pressmin&" - "&_PressMax
    #S184 ="> "&_h_nut_prop
    _nts_prop =int(_Ls/_P)
    _ntn_prop =int(_h_nut/_P)
    _Pw =_Q*_v/1000/_eta
    _v=pi*_d/1000*_n/60
    _SigmaCr =Smax_SecFormula(_SR, _ecc, _Rp02, _A, _E)
    _Q_Crit =_SigmaCr*_A
    _p_thread =4*_Q/(pi*(_d**2-_d1**2)*min(_nz,_nzmax))
    AE178 =Pmax_SecFormula(_SR, _ecc, _Rp02, _A, _E)
    AE187 =4*_Q/(pi*(_d**2-_d1**2)*min(_nz,_nzmax))
    _d2_prop =(_Q/(pi*0.5*2*((_pD_Tbl/IF(S_Units,1,0.145037))/_SFC_prop)))**0.5
    _SFB_2 =ROUND(1.75*(1+(_SR-_SRcs)/(_SRc-_SRcs)),2)
    AF187 =2*_Q/(pi*(_d2/1000)*min(_nz,_nzmax)*_P)/1000
    AI187 =_Q/AH187/1000000
    _SFBcalc =_Q_Crit/_Q
    _SFCcalc =_pD/_p_thread
    _SigmaCr =Smax_SecFormula(_SR, _ecc, _Rp02, _A, _E)
    _Q_Crit =_SigmaCr*_A
    _p_thread =4*_Q/(pi*(_d**2-_d1**2)*min(_nz,_nzmax))#未找到公式
    _SFB_2 =ROUND(1.75*(1+(_SR-_SRcs)/(_SRc-_SRcs)),2)
    A193 =CellTransmitVal(_nts_prop ,_nts,True)
    A194 =CellTransmitVal(_ntn_prop , _ntn,True)
    R123 =ROUND(_d2_prop*IF(S_Units,1,1/25.4),IF(S_Units,1,2))
    R144 =_Pw*IF(S_Units,1,1.34102)#驱动功率
    R146 =_v*IF(S_Units,1,39.37007874)
    R178 =_SigmaCr*IF(S_Units,1,0.145037)
    R179 =_Q_Crit*IF(S_Units,1,0.224809)
    R187 =_p_thread*IF(S_Units,1,0.145037)
    _SFB =IF(_SR<_SRcs,_SFB_1,IF(_SR>_SRc,_SFB_3,_SFB_2))
    结果字典 = {'输入力': (_Q_input, ''),
            '螺纹转速': (_n_req, ''),
            '螺纹摩擦系数': (_f, ''),
            '螺纹外径（标称）': (_d_input, ''),
            '螺母螺纹的内径': (_d1_input, ''),
            '节圆直径': (_d2_input, ''),
            '螺纹内径': (_d3_input, ''),
            '螺母螺纹外径': (_d4_input, ''),
            '螺栓间距': (_P_input, ''),
            '螺纹头数': (_ns, ''),
            '螺纹角度1': (_alfa1_input, ''),
            '螺纹角度2': (_alfa2_input, ''),
            '摩擦系数': (_fj, ''),
            '销钉直径': (_dj_input, ''),
            '螺母螺钉位移': (_dx_input , ''),
            '旋转圈速输入': (_rev_input, ''),
            '螺栓长度': (_Ls_input, ''),
            '密度': (_ro_input, ''),
            '拉伸弹性模量': (_E_input, ''),
            '屈服强度': (_Rp02_input, ''),
            '允许平均螺纹压力': (_pD_input, ''),
            '极限纤度比（短/中）': (_SRcs, ''),
            '极限纤度比（中/长）': (_SRc, ''),
            '有效长度系数': (_Lef_coef, ''),
            '偏心率': (_ecc, ''),
            '螺母高度': (_h_nut_input, ''),
            '最大活动螺纹数': (_nzmax, ''),
            '_nts': (_nts , ''),
            '_ntn': (_ntn, ''),
            '画图输入': (_DN, ''),
            '_SRc': (_SRc, ''),
            '_nzmax_prop': (_nzmax_prop, ''),
        '扭矩': (_Mkup, ''),
            '齿根直径': (_d3, ''),
            '螺纹压力': (_p_thread, 'mpa'),
            '螺纹剪切应力': (_SigmaT, 'mpa'),
            '螺纹弯曲应力': (_Sigma, 'mpa'),
            '螺纹合成应力': (_SigmaRed, 'mpa'),}
    return R163,R142,R141,_eta,R144,结果字典,R187
if __name__ == '__main__':
    传动螺栓计算()
    print('a')