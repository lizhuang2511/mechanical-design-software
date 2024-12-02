# -*- coding = utf-8 -*-
# @time:2024/11/29 13:23
# Author:lizhuang
# @File:曲率半径.py
# @Software:PyCharm
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

ComicallyLargeNumber = 2147483647  # to not go to infinity


def signum(x):
    if x >= 0:
        return 1
    else:
        return -1


def derivative(x, y):
    z = np.array([])
    for i in range(y.size - 1):
        z = np.append(z, (y[i + 1] - y[i]) / (x[i + 1] - x[i]))
    x = np.delete(x, x.size - 1)
    return [x, z]


def CurvatureR(y1, y2):
    x = y2[0]
    r = np.array([])
    for i in range(x.size):
        r = np.append(r, (1 + (y1[1][i]) ** 2) ** 1.5 / y2[1][i])
    return [x, r]


def DotOfCurvature(y0, y1, R):
    DotX = np.array([])
    DotY = np.array([])
    for i in range(R[0].size):
        if y1[1][i] != 0:
            k2 = -1 / y1[1][i]
        else:
            k2 = -ComicallyLargeNumber
        dX = R[1][i] / (np.sqrt(k2 ** 2 + 1))
        x2 = y0[0][i] + dX * signum(k2)
        y2 = y0[1][i] + dX * k2 * signum(k2)
        DotY = np.append(DotY, y2)
        DotX = np.append(DotX, x2)

    return [DotX, DotY]



if __name__ == '__main__':

    x = np.linspace(-2, 2, 10000)  # Sample data.
    y = np.array([])
    for i in range(x.size):
        y = np.append(y, 9.8 * x[i] ** 2 / 2)  # there is the main formula

    y0 = [x, y]
    y1 = derivative(x, y)
    y2 = derivative(y1[0], y1[1])
    R = CurvatureR(y1, y2)
    R2 = DotOfCurvature(y0, y1, R)

    fig, ax = plt.subplots(figsize=(16, 9), layout='constrained')

    ax.plot(x, y, label='x**2', color='green')  # it is out function
    ax.plot(y1[0], y1[1], label='y`', color='grey')  # it is a derivative
    ax.plot(y2[0], y2[1], label='y``', color='#00ff8c')  # it is a derivative of a derivative
    ax.plot(R[0], R[1], label='R')  # it is a radius of curvature
    ax.scatter(R2[0], R2[1], label='R2', color='red')  # it is "centre of a circle of curvature"

    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.set_title("yamolodets")
    ax.legend()

    plt.show()