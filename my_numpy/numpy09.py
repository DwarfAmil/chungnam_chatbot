import numpy as np
from numpy03 import npprint


def main():
    a1 = np.fromfunction(lambda x, y, z: x + y + z, (2, 5, 4), dtype=int)
    a2 = np.arange(1, (1 * 5 * 4) + 1).reshape((1, 5, 4)) * 10
    a3 = np.vstack((a1[0, ...], a2[0, ...]))
    a4 = np.hstack((a1[1, ...], a2[0, ...]))
    a5 = np.concatenate((a1, a2), 0)
    npprint(a1, a2)
    npprint(a3, a4, a5)


if __name__ == "__main__":
    main()