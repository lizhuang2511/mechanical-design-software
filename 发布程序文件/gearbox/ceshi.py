# -*- coding = utf-8 -*-
# @time:2024/8/21 16:22
# Author:lizhuang
# @File:ceshi.py
# @Software:PyCharm
# (C) Copyright 2004-2023 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

"""
Supporting Model/View/Controller (MVC) pattern

Demonstrates one approach to writing Model/View/Controller (MVC)-based
applications using Traits UI.

This example contains a trivial model containing only one data object, the
string 'myname'.

In this example, the Controller contains the View. A more rigorous example
would separate these.

A few key points:

- the Controller itself accesses the model as self.model
- the Controller's View can access model traits directly ('myname')
"""

from traits.api import HasTraits, Str, Bool, TraitError
from traitsui.api import View, VGroup, HGroup, Item, Controller


class MyModel(HasTraits):
    """Define a simple model containing a single string, 'myname'"""

    # Simple model data:
    myname = Str()


class MyViewController(MyModel):
    """Define a combined controller/view class that validates that
    MyModel.myname is consistent with the 'allow_empty_string' flag.
    """

    # When False, the model.myname trait is not allowed to be empty:
    allow_empty_string = Bool()

    # Last attempted value of model.myname to be set by user:
    last_name = Str()

    # Define the view associated with this controller:
    view = View(
        VGroup(
            HGroup(
                Item('myname', springy=True),
                '10',
            ),
            # Add an empty vertical group so the above items don't end up
            # centered vertically:
            VGroup(),
        ),
        resizable=True,
    )

    # -- Handler Interface ----------------------------------------------------



    # -- Event handlers -------------------------------------------------------




# Create the model and (demo) view/controller:
demo = MyViewController()

# Run the demo (if invoked from the command line):
if __name__ == '__main__':
    demo.configure_traits()
