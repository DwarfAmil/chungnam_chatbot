import numpy as np
from numpy03 import npprint


def main():
    a = np.arange(24).reshape(3, 2, 4)
    b1, b2, b3 = np.vsplit(a, 3)
    b4, b5 = np.vsplit(a, np.array([1]))
    c1, c2 = np.hsplit(a, 2)
    npprint(a)
    npprint(b1, b2, b3, b4, b5)
    npprint(c1, c2)


if __name__ == "__main__":
    main()