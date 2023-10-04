import numpy as np
from numpy03 import npprint


def main():
    a1 = np.fromfunction(lambda x, y, z: x + y + z, (2, 5, 4), dtype=int)
    a2 = a1[:, 1::2, :3] * 10
    a2[1, ...] = -1
    npprint(a1)
    for array in a2:
        print("out:\n", array)


if __name__ == "__main__":
    main()