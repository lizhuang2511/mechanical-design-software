from traits.api import HasTraits, Float, Int, Enum, observe, List, Str
from traitsui.api import View, Item, VGrid, Handler, EnumEditor

cities = {
    'Square': ['1x1', '2x2'],
    'Triangle': ['3x5', '6x3']
}

class ThreadInfoHandler(Handler):
    cities = List(Str)

    def object_thread_type_changed(self, info):
        self.cities = cities[info.object.thread_type]
        info.object.thread_size = self.cities[0] if self.cities else ''

class ThreadInfo(HasTraits):
    thread_type = Enum(list(cities.keys())[0], list(cities.keys()))
    thread_size = Enum(values='handler.cities')

    thread_outer_diameter = Float
    nut_inner_diameter = Float
    pitch_diameter = Float
    thread_inner_diameter = Float
    nut_thread_outer_diameter = Float
    bolt_spacing = Float
    thread_number = Int
    thread_angle_1 = Float
    thread_angle_2 = Float

    data = {
        ('Square', '1x1'): {
            'thread_outer_diameter': 10.0,
            'nut_inner_diameter': 5.0,
            'pitch_diameter': 2.0,
            'thread_inner_diameter': 7.0,
            'nut_thread_outer_diameter': 12.0,
            'bolt_spacing': 15.0,
            'thread_number': 3,
            'thread_angle_1': 30.0,
            'thread_angle_2': 60.0
        },
        ('Square', '2x2'): {
            'thread_outer_diameter': 12.0,
            'nut_inner_diameter': 6.0,
            'pitch_diameter': 2.5,
            'thread_inner_diameter': 8.0,
            'nut_thread_outer_diameter': 14.0,
            'bolt_spacing': 16.0,
            'thread_number': 4,
            'thread_angle_1': 35.0,
            'thread_angle_2': 65.0
        },
        ('Triangle', '3x5'): {
            'thread_outer_diameter': 8.0,
            'nut_inner_diameter': 4.0,
            'pitch_diameter': 1.5,
            'thread_inner_diameter': 6.0,
            'nut_thread_outer_diameter': 10.0,
            'bolt_spacing': 12.0,
            'thread_number': 2,
            'thread_angle_1': 25.0,
            'thread_angle_2': 55.0
        },
        ('Triangle', '6x3'): {
            'thread_outer_diameter': 9.0,
            'nut_inner_diameter': 4.5,
            'pitch_diameter': 1.8,
            'thread_inner_diameter': 6.5,
            'nut_thread_outer_diameter': 11.0,
            'bolt_spacing': 13.0,
            'thread_number': 3,
            'thread_angle_1': 27.0,
            'thread_angle_2': 57.0
        },
    }

    @observe('thread_type')
    def thread_type_changed(self, change):
        self.thread_size = self.handler.cities[0] if self.handler.cities else ''

        data = self._read_thread_data(self.thread_type, self.thread_size)
        if data:
            self._update_values(data)

    @observe('thread_size')
    def thread_size_changed(self, change):
        data = self._read_thread_data(self.thread_type, self.thread_size)
        if data:
            self._update_values(data)

    def _update_values(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def _read_thread_data(self, thread_type, thread_size):
        return self.data.get((thread_type, thread_size), {})

    traits_view = View(
        Item('thread_type', label='螺纹类型'),
        Item('thread_size', label='螺纹尺寸', editor=EnumEditor(name='handler.cities')),
        VGrid(
            Item('thread_outer_diameter', label='螺纹外径（标称）'),
            Item('nut_inner_diameter', label='螺母螺纹的内径'),
            Item('pitch_diameter', label='节圆直径'),
            Item('thread_inner_diameter', label='螺纹内径'),
            Item('nut_thread_outer_diameter', label='螺母螺纹外径'),
            Item('bolt_spacing', label='螺栓间距'),
            Item('thread_number', label='螺纹序号'),
            Item('thread_angle_1', label='螺纹角度1'),
            Item('thread_angle_2', label='螺纹角度2'),
            columns=2,
            show_border=True,
        ),
        title='螺纹信息',
        resizable=True,
        handler=ThreadInfoHandler(),
    )

# 创建对象并显示界面
thread_info = ThreadInfo()
thread_info.configure_traits()
