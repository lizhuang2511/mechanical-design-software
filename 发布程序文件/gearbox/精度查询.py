# -*- coding = utf-8 -*-
# @time:2024/8/21 16:34
# Author:lizhuang
# @File:精度查询.py
# @Software:PyCharm
from traits.api import HasTraits, Str, Bool, TraitError
from traitsui.api import View, VGroup, HGroup, Item, Controller


class MyModel(HasTraits):
    """Define a simple model containing a single string, 'myname'"""

    # Simple model data:
    fpt= F()
if __name__ == '__main__': 
  test=MyModel()