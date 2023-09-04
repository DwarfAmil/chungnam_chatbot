# import torch1
from torch1 import Torch


class PyTorch(Torch):
    def __init__(self, name):
        super().__init__(name)
        self.pyname = "py박형진"

    def sub_print(self):
        print(f"pyname: {self.pyname}\nname: {self.name}")

    # special method
    def __str__(self):
        return f"pyname: {self.pyname}\nname: {self.name}"
    
    def __eq__(self, value):
        return self.pyname == value.pyname


def main():
    # t = torch1.Torch("박형진")
    t = Torch("박형진")
    t.print()
    print()
    t2 = PyTorch("박아무개")
    t3 = PyTorch("박아무개")
    t2.print()
    t2.sub_print()
    print(isinstance(t, object))
    print(t2)
    print(t2 == t3)


if __name__ == "__main__":
    main()