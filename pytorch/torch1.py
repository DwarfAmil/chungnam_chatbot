import torch

class Torch:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"This is Torch class\nname: {self.name}")

def main():
    torch1 = Torch("park hyung jin")
    torch2 = Torch("DwarfAmil")
    torch3 = Torch("choi su gil")
    torch1.print()
    print(torch1.name)
    print(torch2.name)
    print(torch3.name)

if __name__ == "__main__":
    main()
