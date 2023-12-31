import numpy as np
from numpy03 import npprint


def main():
    a1 = np.full((6, 3), -1)
    a2 = np.reshape(a1, (3, 3, 2))
    a3 = np.arange(1, 10 + 1, 0.5).reshape((5, 4))
    try:
        a4 = np.reshape(a3, (5, 5))
        npprint(a4)
    except Exception:
        print("Error")
    a5 = np.linspace(1, 10 + 1, 20).reshape((2, 5, 2))
    npprint(a1, a2, a3, a5)


if __name__ == "__main__":
    main()