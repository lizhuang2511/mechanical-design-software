class CustomObject:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

# 创建一个示例对象
obj = CustomObject(10, 'hello', 3.14)

# 获取对象的所有属性名称及对应的属性值
attributes = obj.__dict__.items()

# 创建包含对象名和每个属性与其完整的对象名和原始属性名称的字典
result_dict = {f"{obj.__class__.__name__}.{key}": (f"{obj.__class__.__name__}.{key}", '') for key, value in attributes}

print(result_dict)
original_dict2 = {
    'sigmafone': 418.73812752180146,
    'sigmaftwo': 511.3977173055086,
    'sigmafpone': 835.8615596870329,
    'sigmafptwo': 806.4764007972391,
    'yst': 2,
    'yxone': 1.0,
    'yxtwo': 1.0,
    'yfone': 0.9752418688852466,
    'yftwo': 1.7175981987947102,
    'ysone': 2.500451811579183,
    'ystwo': 1.7339059217696875,
    'ybeta': 1.0,
    'ybone': 1,
    'ybtwo': 1,
    'ydeltaone': 1.0070294343690813,
    'ydeltatwo': 0.9600583453346874,
    'ydt': 1,
    'yntone': 0.8926181581863151,
    'ynttwo': 0.9033739551836921,
    'yrelone': 1.0107381158996591,
    'yreltwo': 1.0107381158996591,
    'kv': 1.032205908934822,
    'kfa': 1,
    'kfb': 1.1355080947897715
}
original_dict={'sigmaH': 1457.2053560138731, 'sigmaHTwo': 1457.103208966315, 'sigmaHPOne': 1280.0740671861715, 'sigmaHPTwo': 1294.7601105154292, 'zh': 2.416943479068675, 'zb': 1.0000701028224561, 'zd': 1, 'ze': 189.8117004375665, 'z_epsilon': 0.9020275942428247, 'z_beta': 1.0, 'znt_one': 0.8905416859975352, 'znt_two': 0.9007586993113188, 'zl': 0.9967176032217998, 'zv': 0.978123363949461, 'zr': 0.972620472849807, 'zw_one': 1.010602617345763, 'zw_two': 1.010602617345763, 'zx': 1, 'kv': 1.032205908934822, 'khb': 1.1636746453329694, 'kha': 1}

# 使用原始字典中的值创建格式化后的字典
formatted_dict = {key: (f"接触应力[{key}]", '') for key in original_dict}
formatted_dict2 = {key: (f"弯曲应力[{key}]", '') for key in original_dict2}
result={}
#print(formatted_dict)


#print(result)
pinion={'pinion.profile': ('pinion.profile', ''), 'pinion.material': ('pinion.material', ''), 'pinion.z': ('pinion.z', ''), 'pinion.beta': ('pinion.beta', ''), 'pinion.alpha': ('pinion.alpha', ''), 'pinion.m': ('pinion.m', ''), 'pinion.x': ('pinion.x', ''), 'pinion.b': ('pinion.b', ''), 'pinion.bs': ('pinion.bs', ''), 'pinion.sr': ('pinion.sr', ''), 'pinion.rz': ('pinion.rz', ''), 'pinion.precision_grade': ('pinion.precision_grade', ''), 'pinion.shaft_diameter': ('pinion.shaft_diameter', ''), 'pinion.schema': ('pinion.schema', ''), 'pinion.l': ('pinion.l', ''), 'pinion.s': ('pinion.s', ''), 'pinion.backlash': ('pinion.backlash', ''), 'pinion.pinion_crown': ('pinion.pinion_crown', ''), 'pinion.helix_modification': ('pinion.helix_modification', ''), 'pinion.favorable_contact': ('pinion.favorable_contact', ''), 'pinion.pinion_condition': ('pinion.pinion_condition', ''), 'pinion.xmin': ('pinion.xmin', ''), 'pinion.alpha_t': ('pinion.alpha_t', ''), 'pinion.d': ('pinion.d', ''), 'pinion.da': ('pinion.da', ''), 'pinion.df': ('pinion.df', ''), 'pinion.db': ('pinion.db', ''), 'pinion.addendum': ('pinion.addendum', ''), 'pinion.dedendum': ('pinion.dedendum', ''), 'pinion.h': ('pinion.h', ''), 'pinion.rho_f': ('pinion.rho_f', ''), 'pinion.mt': ('pinion.mt', ''), 'pinion.p_b': ('pinion.p_b', ''), 'pinion.p_n': ('pinion.p_n', ''), 'pinion.beta_b': ('pinion.beta_b', ''), 'pinion.zn': ('pinion.zn', ''), 'pinion.f_pt': ('pinion.f_pt', ''), 'pinion.f_p': ('pinion.f_p', ''), 'pinion.f_alpha': ('pinion.f_alpha', ''), 'pinion.f_beta': ('pinion.f_beta', ''), 'pinion.f_f_alpha': ('pinion.f_f_alpha', ''), 'pinion.f_h_alpha': ('pinion.f_h_alpha', ''), 'pinion.f_h_beta': ('pinion.f_h_beta', ''), 'pinion.f_f_beta': ('pinion.f_f_beta', ''), 'pinion.f_h_beta5': ('pinion.f_h_beta5', '')}
gear={'gear.profile': ('gear.profile', ''), 'gear.material': ('gear.material', ''), 'gear.z': ('gear.z', ''), 'gear.beta': ('gear.beta', ''), 'gear.alpha': ('gear.alpha', ''), 'gear.m': ('gear.m', ''), 'gear.x': ('gear.x', ''), 'gear.b': ('gear.b', ''), 'gear.bs': ('gear.bs', ''), 'gear.sr': ('gear.sr', ''), 'gear.rz': ('gear.rz', ''), 'gear.precision_grade': ('gear.precision_grade', ''), 'gear.shaft_diameter': ('gear.shaft_diameter', ''), 'gear.schema': ('gear.schema', ''), 'gear.l': ('gear.l', ''), 'gear.s': ('gear.s', ''), 'gear.backlash': ('gear.backlash', ''), 'gear.gear_crown': ('gear.gear_crown', ''), 'gear.helix_modification': ('gear.helix_modification', ''), 'gear.favorable_contact': ('gear.favorable_contact', ''), 'gear.gear_condition': ('gear.gear_condition', ''), 'gear.xmin': ('gear.xmin', ''), 'gear.alpha_t': ('gear.alpha_t', ''), 'gear.d': ('gear.d', ''), 'gear.da': ('gear.da', ''), 'gear.df': ('gear.df', ''), 'gear.db': ('gear.db', ''), 'gear.addendum': ('gear.addendum', ''), 'gear.dedendum': ('gear.dedendum', ''), 'gear.h': ('gear.h', ''), 'gear.rho_f': ('gear.rho_f', ''), 'gear.mt': ('gear.mt', ''), 'gear.p_b': ('gear.p_b', ''), 'gear.p_n': ('gear.p_n', ''), 'gear.beta_b': ('gear.beta_b', ''), 'gear.zn': ('gear.zn', ''), 'gear.f_pt': ('gear.f_pt', ''), 'gear.f_p': ('gear.f_p', ''), 'gear.f_alpha': ('gear.f_alpha', ''), 'gear.f_beta': ('gear.f_beta', ''), 'gear.f_f_alpha': ('gear.f_f_alpha', ''), 'gear.f_h_alpha': ('gear.f_h_alpha', ''), 'gear.f_h_beta': ('gear.f_h_beta', ''), 'gear.f_f_beta': ('gear.f_f_beta', ''), 'gear.f_h_beta5': ('gear.f_h_beta5', '')}
tool={'tool.ha_p': ('tool.ha_p', ''), 'tool.hf_p': ('tool.hf_p', ''), 'tool.rho_fp': ('tool.rho_fp', ''), 'tool.c': ('tool.c', ''), 'tool.nc': ('tool.nc', ''), 'tool.x': ('tool.x', ''), 'tool.rho_ao': ('tool.rho_ao', ''), 'tool.delta_ao': ('tool.delta_ao', '')}
transmission={'transmission.rpm_in': ('transmission.rpm_in', ''), 'transmission.rpm_out': ('transmission.rpm_out', ''), 'transmission.ka': ('transmission.ka', ''), 'transmission.sh_min': ('transmission.sh_min', ''), 'transmission.sf_min': ('transmission.sf_min', ''), 'transmission.v40': ('transmission.v40', ''), 'transmission.gear_box_type': ('transmission.gear_box_type', ''), 'transmission.u': ('transmission.u', ''), 'transmission.p': ('transmission.p', ''), 'transmission.l': ('transmission.l', ''), 'transmission.m': ('transmission.m', ''), 'transmission.alpha': ('transmission.alpha', ''), 'transmission.alpha_t': ('transmission.alpha_t', ''), 'transmission.u_real': ('transmission.u_real', ''), 'transmission.u_error': ('transmission.u_error', ''), 'transmission.alpha_wt': ('transmission.alpha_wt', ''), 'transmission.a': ('transmission.a', ''), 'transmission.aw': ('transmission.aw', ''), 'transmission.epsilon_alpha': ('transmission.epsilon_alpha', ''), 'transmission.epsilon_beta': ('transmission.epsilon_beta', ''), 'transmission.epsilon_gama': ('transmission.epsilon_gama', ''), 'transmission.v': ('transmission.v', ''), 'transmission.ft': ('transmission.ft', ''), 'transmission.fmt': ('transmission.fmt', ''), 'transmission.xsum': ('transmission.xsum', ''), 'transmission.gear_one': ('transmission.gear_one', ''), 'transmission.gear_two': ('transmission.gear_two', ''), 'transmission.pair': ('transmission.pair', '')}
lubricant={'lubricant.name': ('lubricant.name', ''), 'lubricant.v40': ('lubricant.v40', '')}
materialm1={'materialm1.sh_limit': ('materialm1.sh_limit', ''), 'materialm1.sf_limit': ('materialm1.sf_limit', ''), 'materialm1.classification': ('materialm1.classification', ''), 'materialm1.name': ('materialm1.name', ''), 'materialm1.e': ('materialm1.e', ''), 'materialm1.poisson': ('materialm1.poisson', ''), 'materialm1.density': ('materialm1.density', ''), 'materialm1.brinell': ('materialm1.brinell', '')}
materialm2={'materialm2.sh_limit': ('materialm2.sh_limit', ''), 'materialm2.sf_limit': ('materialm2.sf_limit', ''), 'materialm2.classification': ('materialm2.classification', ''), 'materialm2.name': ('materialm2.name', ''), 'materialm2.e': ('materialm2.e', ''), 'materialm2.poisson': ('materialm2.poisson', ''), 'materialm2.density': ('materialm2.density', ''), 'materialm2.brinell': ('materialm2.brinell', '')}
result.update(pinion)
result.update(gear)
result.update(tool)  
result.update(transmission)
result.update(lubricant)
result.update(materialm1)
result.update(materialm2)
result.update(formatted_dict2)
result.update(formatted_dict)

print(result)






