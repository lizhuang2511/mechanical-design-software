# -*- coding = utf-8 -*-
# @time:2023/4/16 11:48
# Author:lizhuang
# @File:修改绘画.py
# @Software:PyCharm
from sympy.physics.continuum_mechanics.beam import Beam as sympyBeam
import numpy
from sympy.core import S, Symbol, diff, symbols
from sympy.core.add import Add
from sympy.core.expr import Expr
from sympy.core.function import (Derivative, Function)
from sympy.core.mul import Mul
from sympy.core.relational import Eq
from sympy.core.sympify import sympify
from sympy.solvers import linsolve
from sympy.solvers.ode.ode import dsolve
from sympy.solvers.solvers import solve
from sympy.printing import sstr
from sympy.functions import SingularityFunction, Piecewise, factorial
from sympy.integrals import integrate
from sympy.series import limit
from sympy.plotting import plot, PlotGrid
from sympy.geometry.entity import GeometryEntity
from sympy.external import import_module
from sympy.sets.sets import Interval
from sympy.utilities.lambdify import lambdify
from sympy.utilities.decorator import doctest_depends_on
from sympy.utilities.iterables import iterable
from sympy.plotting.plot import check_arguments,LineOver1DRangeSeries,Plot
class Plot5(Plot):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print(2)
    def show(self):
        # TODO move this to the backend (also for save)
        if hasattr(self, '_backend'):
            self._backend.close()
        self._backend = self.backend(self)
    def save(self, path):
        if hasattr(self, '_backend'):
            self._backend.close()
        self._backend = self.backend(self)
        self._backend.close()
        self._backend.save(path)

def plot2(*args, **kwargs):
    """Plots a function of a single variable as a curve.

    Parameters
    ==========

    args :
        The first argument is the expression representing the function
        of single variable to be plotted.

        The last argument is a 3-tuple denoting the range of the free
        variable. e.g. ``(x, 0, 5)``

        Typical usage examples are in the followings:

        - Plotting a single expression with a single range.
            ``plot(expr, range, **kwargs)``
        - Plotting a single expression with the default range (-10, 10).
            ``plot(expr, **kwargs)``
        - Plotting multiple expressions with a single range.
            ``plot(expr1, expr2, ..., range, **kwargs)``
        - Plotting multiple expressions with multiple ranges.
            ``plot((expr1, range1), (expr2, range2), ..., **kwargs)``

        It is best practice to specify range explicitly because default
        range may change in the future if a more advanced default range
        detection algorithm is implemented.

    show : bool, optional
        The default value is set to ``True``. Set show to ``False`` and
        the function will not display the plot. The returned instance of
        the ``Plot`` class can then be used to save or display the plot
        by calling the ``save()`` and ``show()`` methods respectively.

    line_color : string, or float, or function, optional
        Specifies the color for the plot.
        See ``Plot`` to see how to set color for the plots.
        Note that by setting ``line_color``, it would be applied simultaneously
        to all the series.

    title : str, optional
        Title of the plot. It is set to the latex representation of
        the expression, if the plot has only one expression.

    label : str, optional
        The label of the expression in the plot. It will be used when
        called with ``legend``. Default is the name of the expression.
        e.g. ``sin(x)``

    xlabel : str, optional
        Label for the x-axis.

    ylabel : str, optional
        Label for the y-axis.

    xscale : 'linear' or 'log', optional
        Sets the scaling of the x-axis.

    yscale : 'linear' or 'log', optional
        Sets the scaling of the y-axis.

    axis_center : (float, float), optional
        Tuple of two floats denoting the coordinates of the center or
        {'center', 'auto'}

    xlim : (float, float), optional
        Denotes the x-axis limits, ``(min, max)```.

    ylim : (float, float), optional
        Denotes the y-axis limits, ``(min, max)```.

    annotations : list, optional
        A list of dictionaries specifying the type of annotation
        required. The keys in the dictionary should be equivalent
        to the arguments of the matplotlib's annotate() function.

    markers : list, optional
        A list of dictionaries specifying the type the markers required.
        The keys in the dictionary should be equivalent to the arguments
        of the matplotlib's plot() function along with the marker
        related keyworded arguments.

    rectangles : list, optional
        A list of dictionaries specifying the dimensions of the
        rectangles to be plotted. The keys in the dictionary should be
        equivalent to the arguments of the matplotlib's
        patches.Rectangle class.

    fill : dict, optional
        A dictionary specifying the type of color filling required in
        the plot. The keys in the dictionary should be equivalent to the
        arguments of the matplotlib's fill_between() function.

    adaptive : bool, optional
        The default value is set to ``True``. Set adaptive to ``False``
        and specify ``nb_of_points`` if uniform sampling is required.

        The plotting uses an adaptive algorithm which samples
        recursively to accurately plot. The adaptive algorithm uses a
        random point near the midpoint of two points that has to be
        further sampled. Hence the same plots can appear slightly
        different.

    depth : int, optional
        Recursion depth of the adaptive algorithm. A depth of value
        ``n`` samples a maximum of `2^{n}` points.

        If the ``adaptive`` flag is set to ``False``, this will be
        ignored.

    nb_of_points : int, optional
        Used when the ``adaptive`` is set to ``False``. The function
        is uniformly sampled at ``nb_of_points`` number of points.

        If the ``adaptive`` flag is set to ``True``, this will be
        ignored.

    size : (float, float), optional
        A tuple in the form (width, height) in inches to specify the size of
        the overall figure. The default value is set to ``None``, meaning
        the size will be set by the default backend.

    Examples
    ========

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True


    Single Plot

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True


       Plot object containing:
       [0]: cartesian line: x**2 for x over (-5.0, 5.0)

    Multiple plots with single range.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True


       Plot object containing:
       [0]: cartesian line: x for x over (-5.0, 5.0)
       [1]: cartesian line: x**2 for x over (-5.0, 5.0)
       [2]: cartesian line: x**3 for x over (-5.0, 5.0)

    Multiple plots with different ranges.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True


       Plot object containing:
       [0]: cartesian line: x**2 for x over (-6.0, 6.0)
       [1]: cartesian line: x for x over (-5.0, 5.0)

    No adaptive sampling.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True


       Plot object containing:
       [0]: cartesian line: x**2 for x over (-10.0, 10.0)

    See Also
    ========

    Plot, LineOver1DRangeSeries

    """
    args = list(map(sympify, args))
    free = set()
    for a in args:
        if isinstance(a, Expr):
            free |= a.free_symbols
            if len(free) > 1:
                raise ValueError(
                    'The same variable should be used in all '
                    'univariate expressions being plotted.')
    x = free.pop() if free else Symbol('x')
    kwargs.setdefault('xlabel', x.name)
    kwargs.setdefault('ylabel', 'f(%s)' % x.name)
    series = []
    plot_expr = check_arguments(args, 1, 1)
    series = [LineOver1DRangeSeries(*arg, **kwargs) for arg in plot_expr]
    plots = Plot5(*series, **kwargs,backend='matplotlib')
    print(type(plots))
    return plots

numpy = import_module('numpy', import_kwargs={'fromlist':['arange']})
class sympyBeam_1(sympyBeam):
    def __init__(self,length1, elastic_modulus2, second_moment3):
        super().__init__(length=length1, elastic_modulus=elastic_modulus2, second_moment= second_moment3, area=Symbol('A'), variable=Symbol('x'), base_char='C')
        print(1)
    @doctest_depends_on(modules=('numpy',))
    def draw(self, pictorial=False):
        """
        Returns a plot object representing the beam diagram of the beam.

        .. note::
            The user must be careful while entering load values.
            The draw function assumes a sign convention which is used
            for plotting loads.
            Given a right handed coordinate system with XYZ coordinates,
            the beam's length is assumed to be along the positive X axis.
            The draw function recognizes positve loads(with n>-2) as loads
            acting along negative Y direction and positve moments acting
            along positive Z direction.

        Parameters
        ==========

        pictorial: Boolean (default=True)
            Setting ``pictorial=True`` would simply create a pictorial (scaled) view
            of the beam diagram not with the exact dimensions.
            Although setting ``pictorial=False`` would create a beam diagram with
            the exact dimensions on the plot

        Examples
        ========

        .. plot::
            :context: close-figs
            :format: doctest
            :include-source: True


            Plot object containing:
            [0]: cartesian line: 25*SingularityFunction(x, 5, 0) - 25*SingularityFunction(x, 23, 0)
            + SingularityFunction(x, 30, 1) - 20*SingularityFunction(x, 50, 0)
            - SingularityFunction(x, 50, 1) + 5 for x over (0.0, 50.0)
            [1]: cartesian line: 5 for x over (0.0, 50.0)

        """
        if not numpy:
            raise ImportError("To use this function numpy module is required")

        x = self.variable

        # checking whether length is an expression in terms of any Symbol.
        if isinstance(self.length, Expr):
            l = list(self.length.atoms(Symbol))
            # assigning every Symbol a default value of 10
            l = {i: 10 for i in l}
            length = self.length.subs(l)
        else:
            l = {}
            length = self.length
        height = length / 10

        rectangles = []
        rectangles.append({'xy': (0, 0), 'width': length, 'height': height, 'facecolor': "brown"})
        annotations, markers, load_eq, load_eq1, fill = self._draw_load(pictorial, length, l)
        support_markers, support_rectangles = self._draw_supports(length, l)

        rectangles += support_rectangles
        markers += support_markers

        sing_plot = plot2(height + load_eq, height + load_eq1, (x, 0, length),
                         xlim=(-height, length + height), ylim=(-length, 1.25 * length), annotations=annotations,
                         markers=markers, rectangles=rectangles, line_color='brown', fill=fill, axis=False)

        return sing_plot
