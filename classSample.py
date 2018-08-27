#coding=utf-8
class Person:
    def sayHi(self):
        print("你好")


p = Person()
p.sayHi()


class Dog:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('你好:', self.name)


dog = Dog('小狗')
dog.sayHi()