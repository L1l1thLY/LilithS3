import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


class LilithS3(object):
    def __init__(self):
        self.red = list()
        self.green = list()
        self.blue = list()
        self.index = 0

    def hilbert(self, s, x, y, z, dx, dy, dz, dx2, dy2, dz2, dx3, dy3, dz3):

        if s == 1:
            self.red.append(x)
            self.green.append(y)
            self.blue.append(z)
        else:
            s = s / 2
            if dx < 0:
                x = x - s * dx
            if dy < 0:
                y = y - s * dy
            if dz < 0:
                z = z - s * dz
            if dx2 < 0:
                x = x - s * dx2
            if dy2 < 0:
                y = y - s * dy2
            if dz2 < 0:
                z = z - s * dz2
            if dx3 < 0:
                x = x - s * dx3
            if dy3 < 0:
                y = y - s * dy3
            if dz3 < 0:
                z = z - s * dz3

            self.hilbert(s, x, y, z, dx2, dy2, dz2, dx3, dy3, dz3, dx, dy, dz)
            self.hilbert(s, x + s * dx, y + s * dy, z + s * dz, dx3, dy3, dz3, dx, dy, dz, dx2, dy2, dz2)
            self.hilbert(s, x + s * dx + s * dx2, y + s * dy + s * dy2, z + s * dz + s * dz2, dx3, dy3, dz3, dx, dy, dz, dx2, dy2, dz2)
            self.hilbert(s, x + s * dx2, y + s * dy2, z + s * dz2, -dx, -dy, -dz, -dx2, -dy2, -dz2, dx3, dy3, dz3)
            self.hilbert(s, x + s * dx2 + s * dx3, y + s * dy2 + s * dy3, z + s * dz2 + s * dz3, -dx, -dy, -dz, -dx2, -dy2, -dz2, dx3, dy3, dz3)
            self.hilbert(s, x + s * dx + s * dx2 + s * dx3, y + s * dy + s * dy2 + s * dy3, z + s * dz + s * dz2 + s * dz3, -dx3, -dy3, -dz3, dx, dy, dz, -dx2, -dy2, -dz2)
            self.hilbert(s, x + s * dx + s * dx3, y + s * dy + s * dy3, z + s * dz + s * dz3, -dx3, -dy3, -dz3, dx, dy, dz, -dx2, -dy2, -dz2)
            self.hilbert(s, x + s * dx3, y + s * dy3, z + s * dz3, dx2, dy2, dz2, -dx3, -dy3, -dz3, -dx, -dy, -dz)
            self.hilbert(s, x + s * dx3, y + s * dy3, z + s * dz3, dx2, dy2, dz2, -dx3, -dy3, -dz3, -dx, -dy, -dz)

    def test3D(self):
        fig = plt.figure()


        ax = fig.gca(projection='3d')
        ax.plot(self.red, self.green, self.blue, label='parametric curve', linewidth=1)

        ax.legend()
        plt.show()