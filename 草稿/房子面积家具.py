

class house:
    def __init__(self, houseType, houseArea):
        self.houseType = houseType
        self.area = houseArea
        self.fire_area = houseArea
        self.fitment = []

    def __str__(self):
        return '户型：%s\n总面积:%s平米\n剩余面积:%s平米\n家具：%s' % (self.houseType, self.area, self.fire_area, ','.join(self.fitment))

    def add_fitment(self, fitmentname):
        if fitmentname.area < self.fire_area:
            self.fitment.append(fitmentname.name)
            self.fire_area -= fitmentname.area
        else:
            print('%s的占地%s平米太大了，房子剩余面积%s平米太小了' % (fitmentname.name, fitmentname.area, self.fire_area))


class fitment:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '%s占地%s平米' % (self.name, self.area)


bed = fitment('架子床', 4)
bureau = fitment('折叠衣柜', 2)
cutlery = fitment('餐桌', 1.5)

xiaoming_house = house('两室一厅', 100)
xiaoming_house.add_fitment(bed)
xiaoming_house.add_fitment(cutlery)
print(xiaoming_house)
pass