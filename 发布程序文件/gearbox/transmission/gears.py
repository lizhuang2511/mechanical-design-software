from math import pi, atan, tan, radians, cos, sin, degrees, sqrt, floor, ceil
import sys
#sys.path.append("../gearbox/libs")
from maths import involute, arcinvolute


class Tool(object):
    """

    :param ha_p:
    :param hf_p:
    :param rho_fp:
    :param x:
    :param rho_ao:
    :param delta_ao:
    :param nc:
    """

    def __init__(self, ha_p, hf_p, rho_fp, x, rho_ao, delta_ao, nc, c=0.25):
        self.ha_p = ha_p
        self.hf_p = hf_p
        self.rho_fp = rho_fp
        self.c = c
        self.nc = nc
        self.x = x
        self.rho_ao = rho_ao
        self.delta_ao = delta_ao


class Material(object):
    """

    :param sh_limit:
    :param sf_limit:
    :param brinell:
    :param classification:
    :param name:
    :param e:
    :param poisson:
    :param density:
    """

    def __init__(self, sh_limit, sf_limit, brinell, classification, name='', e=206000., poisson=0.3, density=7.83e-6):
        self.sh_limit = sh_limit
        self.sf_limit = sf_limit
        self.classification = classification
        self.name = name
        self.e = e
        self.poisson = poisson
        self.density = density
        self.brinell = brinell


class Lubricant(object):
    """

    :param v40:
    :param name:
    """

    def __init__(self, v40, name=''):
        self.name = name
        self.v40 = v40


class Gear(object):
    """

    :param profile:
    :param material:
    :param z:
    :param beta:
    :param b:
    :param bs:
    :param alpha:
    :param m:
    :param x:
    :param sr:
    :param rz:
    :param precision_grade:
    :param shaft_diameter:
    :param schema:
    :param l:
    :param s:
    :param backlash:
    :param gear_crown:
    :param gear_condition:
    :param helix_modification:
    :param favorable_contact:
    """

    def __init__(self, **kw):
        if 'gear' in kw:
            self.profile = kw['gear'].profile
            self.material = kw['gear'].material
            self.z = kw['gear'].z
            self.beta = kw['gear'].beta
            self.alpha = kw['gear'].alpha
            self.m = kw['gear'].m
            self.x = kw['gear'].x
            self.b = kw['gear'].b
            self.bs = kw['gear'].bs
            self.sr = kw['gear'].sr
            self.rz = kw['gear'].rz
            self.precision_grade = kw['gear'].precision_grade
            self.shaft_diameter = kw['gear'].shaft_diameter
            self.schema = kw['gear'].schema
            self.l = kw['gear'].l
            self.s = kw['gear'].s
            self.backlash = kw['gear'].backlash

            self.gear_crown = kw['gear'].gear_crown
            self.helix_modification = kw['gear'].helix_modification

            if kw['gear'].favorable_contact:
                self.favorable_contact = 1
            else:
                self.favorable_contact = 0

            self.gear_condition = kw['gear'].gear_condition

        else:
            self.profile = kw['profile']
            self.material = kw['material']
            self.z = kw['z']
            self.beta = kw['beta']
            self.alpha = kw['alpha']
            self.m = kw['m']
            self.x = kw['x']
            self.b = kw['b']
            self.bs = kw['bs']
            self.sr = kw['sr']
            self.rz = kw['rz']
            self.precision_grade = kw['precision_grade']
            self.shaft_diameter = kw['shaft_diameter']
            self.schema = kw['schema']
            self.l = kw['l']
            self.s = kw['s']
            self.backlash = kw['backlash']

            self.gear_crown = kw['gear_crown']
            self.helix_modification = kw['helix_modification']

            if kw['favorable_contact']:
                self.favorable_contact = 1
            else:
                self.favorable_contact = 0

            self.gear_condition = kw['gear_condition']

        self.xmin = (1 - sqrt(self.z * sin(radians(self.alpha)))) / 2
        self.alpha_t = degrees(atan(tan(radians(self.alpha)) / cos(radians(self.beta))))
        self.d = self.m * self.z / cos(radians(self.beta))
        self.da = self.m * (self.z / cos(radians(self.beta)) + 2 * (self.profile.ha_p + self.x))
        self.df = self.d - 2 * self.m * (self.profile.ha_p + self.profile.c - self.x)
        self.db = self.d * cos(radians(self.alpha_t))
        self.addendum = self.m * (self.profile.ha_p + self.x)
        self.dedendum = self.m * (self.profile.hf_p - self.x)
        self.h = self.dedendum + self.addendum
        self.rho_f = self.profile.rho_fp * self.m
        self.mt = self.m / cos(radians(self.beta))
        self.p_b = self.m * cos(radians(self.alpha)) * pi
        self.p_n = pi * cos(radians(self.alpha))

        # FIXME self.sn = ((pi/2) + 2 * 0 *self.m*self.x*tan(self.Alpha))
        self.beta_b = degrees(atan(self.db * tan(radians(self.beta)) / self.d))

        self.zn = self.z / (cos(radians(self.beta)) * cos(radians(self.beta_b)) ** 2)

        mc = self.__interval_calc([0, 0.5, 2.0, 3.5, 6.0, 25, 40, 70], self.m)
        dc = self.__interval_calc([0, 5, 20, 50, 125, 280, 560, 1000, 1600, 2500, 4000, 6000, 8000, 10000], self.d)
        bc = self.__interval_calc([0, 4, 10, 20, 40, 80, 160, 250, 400, 650, 1000], self.b)

        f_pt = 0.3 * (mc + 0.4 * sqrt(dc)) + 4.
        f_p = 0.3 * mc + 1.25 * sqrt(dc) + 7.
        f_a = 3.2 * sqrt(mc) + 0.22 * sqrt(dc) + 0.27
        f_beta = 0.1 * sqrt(dc) + 0.63 * sqrt(bc) + 4.2
        f_f_alpha = 2.5 * sqrt(mc) + 0.17 * sqrt(dc) + 0.5
        f_h_alpha = 2 * sqrt(mc) + 0.14 * sqrt(dc) + 0.5
        f_h_beta = 0.07 * sqrt(dc) + 0.45 * sqrt(bc) + 3.

        self.f_pt = self.__q(f_pt, self.precision_grade)
        self.f_p = self.__q(f_p, self.precision_grade)
        self.f_alpha = self.__q(f_a, self.precision_grade)
        self.f_beta = self.__q(f_beta, self.precision_grade)
        self.f_f_alpha = self.__q(f_f_alpha, self.precision_grade)
        self.f_h_alpha = self.__q(f_h_alpha, self.precision_grade)
        self.f_h_beta = self.__q(f_h_beta, self.precision_grade)
        self.f_f_beta = self.__q(f_h_beta, self.precision_grade)
        self.f_h_beta5 = self.__q(f_h_beta, 5)

     
    @staticmethod
    def __interval_calc(intervals, attr):
        for i in range(1, intervals.__len__()):
            if intervals[i - 1] <= attr < intervals[i]:
                return sqrt(intervals[i] * intervals[i - 1])

    @staticmethod
    def __q(x, qiso):
        x *= 2 ** (0.5 * (qiso - 5))
        if x >= 10:
            x = round(x)
        elif 5 <= x < 10:
            if x % 1 <= 0.25 or (0.5 <= x % 1 % 1 <= 0.75):
                x = floor(x * 2) * 0.5
            else:
                x = ceil(x * 2) * 0.5
        else:
            x = round(x, 1)
        return x
class Transmission(object):
    """
    :param lubricant:
    :param rpm_in: the rotation speed of the first gear
    :param gear_box_type: used for AGMA calculation
    :param p: the transmitted power in kW
    :param l: the design life in hours
    :param gears: tuple of Gear objects
    :param ka: the application factor
    :param sf_min: the minimum safety factor for tooth bending
    :param sh_min: the minumum safety factor for flank pitting
    """

    def __init__(self, **kw):

        if 'transmission' in kw:
            gear_one = Gear(gear=kw['transmission'].gear_one)
            gear_two = Gear(gear=kw['transmission'].gear_two)
            gears = [gear_one, gear_two]
            self.rpm_in = kw['transmission'].rpm_in
            self.rpm_out = gear_one.z/gear_two.z*self.rpm_in
            self.ka = kw['transmission'].ka
            self.sh_min = kw['transmission'].sh_min
            self.sf_min = kw['transmission'].sf_min

            self.v40 = kw['transmission'].v40
            self.gear_box_type = kw['transmission'].gear_box_type

            self.u = kw['transmission'].rpm_out / kw['transmission'].rpm_in
            self.p = kw['transmission'].p
            self.l = kw['transmission'].l
        else:
            gears = kw['gears']
            self.rpm_in = kw['rpm_in']
            self.rpm_out = gears[0].z/gears[1].z*self.rpm_in
            self.ka = kw['ka']
            self.sh_min = kw['sh_min']
            self.sf_min = kw['sf_min']

            self.v40 = kw['lubricant'].v40
            self.gear_box_type = kw['gear_box_type']

            self.u = self.rpm_out / self.rpm_in
            self.p = kw['p']
            self.l = kw['l']
        self.pair = self.__calculate(gears[0], gears[1], self.rpm_in, self.rpm_out)
        self.计算齿厚(gears[0], gears[1])
        self.计算齿厚小齿轮(gears[0], gears[1])
    def __calculate(self, gear_one, gear_two, rpm_in, rpm_out):
        if gear_one.m is not gear_two.m:
            raise Exception("the modulus of the two gears most be equal")
        else:
            self.m = gear_one.m

        if gear_one.alpha is not gear_two.alpha:
            raise Exception("the pressure angle of the two gears most be equal")
        else:
            self.alpha = gear_one.alpha
            self.alpha_t = gear_one.alpha_t

        self.u_real = gear_two.z / gear_one.z
        self.u = rpm_in / rpm_out
        self.u_error = abs(1 - (self.u_real / self.u)) * 100
        inv = involute(gear_one.alpha_t) + 2 * (gear_one.x + gear_two.x) / (gear_one.z + gear_two.z) * tan(
            radians(gear_one.alpha))
        self.alpha_wt = arcinvolute(inv)
        print("alpha_wt",self.alpha_wt)
        self.a = ((gear_one.z + gear_two.z) * gear_one.m) / (2 * cos(radians(gear_one.beta)))
        print('a中心距',self.a)
        self.aw = self.a * cos(radians(gear_one.alpha)) / cos(radians(self.alpha_wt))
        print('aw中心距=',self.aw)
        分母=(pi * gear_one.m * cos(radians(gear_one.alpha_t)) / (cos(radians(gear_one.beta))))#pet
        print(分母,self.aw * sin(radians(self.alpha_wt)))
        print(gear_two.da**2-gear_two.b**2,gear_one.da**2-gear_one.b**2)
        galf=0.5*(sqrt(gear_one.da**2-gear_one.db**2)+((sqrt(gear_two.da**2-gear_two.db**2))- 2*self.aw * sin(radians(self.alpha_wt))))
        print(galf/分母)
        ga1=0.5*(sqrt(gear_one.da**2-gear_one.db**2)-gear_one.db*tan(radians(self.alpha_wt)))
        print(ga1)
        gf1=0.5*(sqrt(gear_two.da**2-gear_two.db**2)-gear_two.db*tan(radians(self.alpha_wt)))
        print(gf1)
        pt = gear_one.mt * pi
        print("pt", pt)
        pbt = gear_one.db / gear_one.d * pt
        print("pbt", pbt, gear_one.beta_b)
        pet = pbt
        print((ga1+gf1)/分母)
        self.epsilon_alpha=(ga1+gf1)/pet
        '''self.epsilon_alpha = (0.5 * (
        sqrt(gear_one.da ** 2 - gear_one.db ** 2) + sqrt(gear_two.da ** 2 - gear_two.db ** 2)) - self.aw * sin(
            radians(self.alpha_wt))) / (
                             pi * gear_one.m * cos(radians(gear_one.alpha_t)) / (cos(radians(gear_one.beta))))'''#源代码
        print('重合度=',self.epsilon_alpha )

        epsilon_beta=gear_one.b*tan(radians(gear_one.beta_b))/pet

        print(epsilon_beta)
        self.epsilon_beta = gear_one.b * sin(radians(gear_one.beta)) / (gear_one.m * pi)#齿宽是不是取小值
        print('重合度b=',self.epsilon_beta)
        self.epsilon_gama = self.epsilon_alpha + self.epsilon_beta
        self.v = rpm_in * gear_one.d * pi / 60000
        self.ft = 1000. * self.p * 60000 / (pi * gear_one.d * rpm_in)#名义切向力
        print('self.ft',self.ft)
        if self.ka * self.ft / gear_one.b < 100:
            self.fmt = 100
        else:
            self.fmt = self.ka * self.ft / gear_one.b

        # self.xsum = ((gear_one.z + gear_two.z) * (involute(radians(self.alpha_wt))-involute(radians(self.alpha_t))))/(2*tan(radians(self.alpha)))
        self.xsum = gear_one.x + gear_two.x
        self.gear_one = gear_one
        self.gear_two = gear_two

    def 计算齿厚(self, gear_one, gear_two):
        import math
        # 计算分度圆齿厚  
        # 齿厚与齿槽宽相等，因此分度圆齿厚 = (π * m) / 2  
        s = math.pi * gear_two.m / 2
        alpha_rad = math.pi * gear_two.alpha / 180
        # 计算齿顶厚和齿根厚需要更复杂的几何计算，但通常使用近似公式或图表  
        # 这里我们给出齿顶厚和齿根厚的基本计算公式（注意这些可能是近似值）  
        # 齿顶厚 sa（在齿顶圆上的弧长）  
        # 注意：这里使用了一个简化公式，实际计算可能需要根据具体情况调整  
        # gear_two.sa = gear_two.s + gear_two.m * (1.25 * math.tan(alpha_rad) - math.tan(math.radians(gear_two.alpha - 20)))

        # 齿根厚 sf（在齿根圆上的弧长）  
        # 注意：这里同样使用了近似公式
        _ha0X2 = 1.25
        x2 = 0
        _hf2 = gear_two.m * (_ha0X2 - x2)
        _d2 = gear_two.z * gear_two.mt
        df2 = _d2 - 2 * _hf2
        p = pi * gear_two.m
        pt = p / cos(gear_two.beta * pi / 180)
        alfa = 20
        alfat = 180 / pi * atan(tan(alfa * pi / 180) / cos(gear_two.beta * pi / 180))
        alfat = alfat / 180 * pi
        self.alfat = radians(gear_two.alpha_t)
        st2 = pt / 2 + 2 * x2 * gear_two.mt * tan(self.alfat)
        #sn2 = st2 * cos(gear_two.beta * pi / 180)
        self.sn22=gear_two.m*(pi/2+2*gear_two.x*tan(radians(self.alpha)))
        self.s = st2
        from maths import involute as inv
        sb2 = df2 * (st2 / _d2 + inv(degrees(self.alfat)))
        # mt=gear_two.m/cos(gear_two.beta*pi/180)
        _caXG = 0.25
        _d1 = gear_one.z * gear_two.mt
        _hf1=12.5
        _df1 =_d1 - 2 * _hf1
        da2 = 2 * (self.aw - _df1 / 2 - _caXG * gear_two.m)
        sta2 = da2 * (st2 / _d2 + inv(degrees(self.alfat)) - inv(degrees(math.acos(_d2 * cos(self.alfat) / da2))))
        # gear_two.sf = gear_two.s - (1.25 + gear_two.x) * gear_two.m * math.tan(alpha_rad)
        self.sf = sb2
        self.sa = sta2

    def 计算齿厚小齿轮(self, gear_one, gear_two):
        import math
        # 计算分度圆齿厚  
        # 齿厚与齿槽宽相等，因此分度圆齿厚 = (π * m) / 2  
        s = math.pi * gear_one.m / 2
        alpha_rad = math.pi * gear_one.alpha / 180
        # 计算齿顶厚和齿根厚需要更复杂的几何计算，但通常使用近似公式或图表  
        # 这里我们给出齿顶厚和齿根厚的基本计算公式（注意这些可能是近似值）  
        # 齿顶厚 sa（在齿顶圆上的弧长）  
        # 注意：这里使用了一个简化公式，实际计算可能需要根据具体情况调整  
        # gear_one.sa = gear_one.s + gear_one.m * (1.25 * math.tan(alpha_rad) - math.tan(math.radians(gear_one.alpha - 20)))

        # 齿根厚 sf（在齿根圆上的弧长）  
        # 注意：这里同样使用了近似公式
        _ha0X2 = 1.25
        x2 = 0
        _hf2 = gear_one.m * (_ha0X2 - x2)
        _d2 = gear_one.z * gear_one.mt
        df2 = _d2 - 2 * _hf2
        p = pi * gear_one.m
        pt = p / cos(gear_one.beta * pi / 180)
        alfa = 20
        alfat = 180 / pi * atan(tan(alfa * pi / 180) / cos(gear_one.beta * pi / 180))
        alfat = alfat / 180 * pi
        self.alfat = radians(gear_one.alpha_t)
        st2 = pt / 2 + 2 * x2 * gear_one.mt * tan(self.alfat)
        sn2 = st2 * cos(gear_one.beta * pi / 180)
        self.sn11 = gear_one.m * (pi / 2 + 2 * gear_one.x * tan(radians(self.alpha)))
        self.s1 = st2
        from maths import involute as inv
        sb2 = df2 * (st2 / _d2 + inv(degrees(self.alfat)))
        # mt=gear_one.m/cos(gear_one.beta*pi/180)
        _caXG = 0.25
        _d1 = gear_two.z * gear_two.mt
        _hf1 = 12.5
        _df1 = _d1 - 2 * _hf1
        da2 = 2 * (self.aw - _df1 / 2 - _caXG * gear_one.m)
        sta2 = da2 * (st2 / _d2 + inv(degrees(self.alfat)) - inv(degrees(math.acos(_d2 * cos(self.alfat) / da2))))
        # gear_one.sf = gear_one.s - (1.25 + gear_one.x) * gear_one.m * math.tan(alpha_rad)
        self.sf1 = sb2
        self.sa1 = sta2

