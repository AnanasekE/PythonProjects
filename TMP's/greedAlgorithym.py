class Items:
    def __init__(self, name, weight, value):
        self.value = value
        self.weight = weight
        self.name = name




items = []


def pack(carHold, shopList: list):  # more shop, less car
    pass
    shopList.sort(key=lambda x: x[1] / x[0])
    return shopList

pack(10, items)
