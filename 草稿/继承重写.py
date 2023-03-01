class Animal:
    def eat(self):
        print('吃~~~~')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')


class Cat(Animal):
    def call(self):
        print('喵～')


class Tom(Cat):
    def speak(self):
        print('我可以说日语')

    def call(self):
        # 1.针对子类特有的需求，编写代码
        print('子类的方法')
        # 2.调用原本在父类中封装的方法
        # Cat.call(self)
        super().call()

kaili = Tom()
kaili.call()