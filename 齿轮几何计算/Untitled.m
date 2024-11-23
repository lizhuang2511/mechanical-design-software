% 计算斜齿轮公法线长度及其偏差
% 输入齿轮基本参数
Mn=14;z=130;an=20;bat=15;
disp ' '
disp '           ========== 斜齿圆柱齿轮基本参数   =========='
fprintf('                      模数      Mn = %3.2f mm \n',Mn)
fprintf('                      齿数       z = %3.0f \n',z)
fprintf('                    压力角      an = %3.3f 度 \n',an)
fprintf('                    螺旋角     bat = %3.3f 度 \n',bat)
% 角度转换为弧度
hd=pi/180;
anh=an*hd;
bath=bat*hd;
invan=tan(anh)-anh;
% 计算跨齿数和公法线长度
ath=atan(tan(anh)/cos(bath));
invan=tan(anh)-anh;
invat=tan(ath)-ath;
zp=z*invat/invan;
k=round(zp/9+0.5);
Wkn=Mn*cos(anh)*(pi*(k-0.5)+zp*invan);
disp ' '
disp '    ========== 计算斜齿圆柱齿轮公法线长度及其偏差   =========='
fprintf('                 端面压力角     at = %3.3f 度 \n',ath/hd)
fprintf('                   相当齿数     zp = %3.3f \n',zp)
fprintf('                     跨齿数      k = %2.0f \n',k)
fprintf('                 公法线长度    Wkn = %3.3f mm \n',Wkn)
% 输入齿距极限偏差和齿圈径向跳动公差
fpt=0.028;Fr=0.071;
% 输入齿厚极限偏差代号
H=-8;L=-16;
% 计算齿厚极限偏差
Es=H*fpt;Ei=L*fpt;
fprintf('                 齿厚上偏差     Es = %3.3f mm \n',Es)
fprintf('                 齿厚下偏差     Ei = %3.3f mm \n',Ei)
% 计算公法线长度极限偏差
Ews=Es*cos(anh)-0.72*Fr*sin(anh);
Ewi=Ei*cos(anh)+0.72*Fr*sin(anh);
fprintf('           公法线长度上偏差    Ews = %3.3f mm \n',Ews)
fprintf('           公法线长度下偏差    Ewi = %3.3f mm \n',Ewi)

