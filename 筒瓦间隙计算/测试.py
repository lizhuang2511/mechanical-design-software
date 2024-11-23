import time
import feon
from feon.sa import *

if __name__ == "__main__":
    # 定义材料参数
    E = 210e6  # 弹性模量
    A = 0.005  # 截面面积
    K = 79e3  # 弹簧刚度

    # 通过Node对象创建节点，需要输入节点坐标
    n0 = Node(0, 0)
    n1 = Node(5, 0)
    n2 = Node(10, 0)
    n3 = Node(15, 0)
    n4 = Node(5, 7)
    n5 = Node(10, 7)
    n6 = Node(15, -1)

    # 通过节点创建单元，Link2D11为二维杆单元，输入参数为单元节点，弹性模量和截面面积
    e0 = Link2D11((n0, n1), E, A)
    e1 = Link2D11((n1, n2), E, A)
    e2 = Link2D11((n2, n3), E, A)
    e3 = Link2D11((n4, n0), E, A)
    e4 = Link2D11((n4, n1), E, A)
    e5 = Link2D11((n4, n2), E, A)
    e6 = Link2D11((n4, n5), E, A)
    e7 = Link2D11((n5, n2), E, A)
    e8 = Link2D11((n5, n3), E, A)

    # 创建弹簧单元
    e9 = Spring2D11((n3, n6), K)

    # 创建一个有限元系统
    s = System()

    # 将节点和单元添加到系统中
    s.add_nodes(n0, n1, n2, n3, n4, n5, n6)
    s.add_elements(e0, e1, e2, e3, e4, e5, e6, e7, e8, e9)

    # 添加力边界条件
    s.add_node_force(4, Fx=30)

    # 添加固定支座，输入节点的编号0和6
    s.add_fixed_sup(0, 6)

    # 求解系统
    s.solve()
print(e1.force)
