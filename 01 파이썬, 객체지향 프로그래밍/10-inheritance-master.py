"""
* [클래스 상속]

* 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

* 2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

* 3. 메서드 오버라이딩

* 4. super()

* 5. Python의 모든 클래스는 object 클레스를 상속한다. : 모든 것은 객체이다. # 파이썬의 핵심

    * MyClass.mro() --> 상속 관계를 보여준다.
"""


class Robot(object):  # Robot() == Robot(object)

    """
    Robot Class
    """

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."


class Siri(Robot):
    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b


siri = Siri("iphone8")


print(
    Siri.mro()  # 상속의 관계 표현.
)  # * [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>] # Siri가 Robot을 상속 받았고, Robot은 object를 상속받는다

print(Robot.mro())  # * [<class '__main__.Robot'>, <class 'object'>]

print(object)  # <class 'object'>

print(dir(object))
"""
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__']
"""

print(object.__name__)  # object

print(int.mro())  # [<class 'int'>, <class 'object'>]
print(int.__init__(8.9))
print(int(8.9))


# 다중상속 -> 좋지 않은 패턴(정신없음), 독립된 부품을 조립하는 용도로는 사용


class A:  # 부품1
    pass


class B:  # 부품2
    pass


class C:  # 부품3
    pass


class D(A, B, C):  # 자동차
    pass


print(D.mro())
