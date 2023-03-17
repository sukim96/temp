class Test:
    def __init__(self, coco, objects365):
        self.classes = [k for k in coco if k in objects365]

    def find_key(self, key):
        return key in self.classes


def main(coco, objects365, keys=["teddy bear", "suitcase", "sports ball"]):
    tester = Test(coco, objects365)
    for key in keys:
        if tester.find_key(key):
            print(f"{key} is in list")
        else:
            print(f"{key} is not in list")


if __name__ == "__main__":
    from coco import coco
    from objects365 import objects365

    keys = ["teddy bear", "suitcase", "sports ball"]

    main(coco, objects365, keys)
