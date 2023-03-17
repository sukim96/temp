class Test:
    def __init__(self, coco, objects365):
        self.classes = [k for k in coco if k in objects365]

    def find_key(self, key):
        return key in self.classes


def main(coco, objects365):
    tester = Test(coco, objects365)
    for key in ["teddy bear", "suitcase", "sports"]:
        if tester.find_key(key):
            print(f"{key} is in list")
        else:
            print(f"{key} is not in list")


if __name__ == "__main__":
    coco = ["Carrot", "Kite"]  # , ...
    objects365 = ["Cainsaw", "Eraser"]  # , ...

    main(coco, objects365)
