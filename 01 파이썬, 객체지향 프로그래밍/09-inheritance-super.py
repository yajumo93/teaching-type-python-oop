"""
* [클래스 상속]

* 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

* 2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

* 3. 메서드 오버라이딩

* 4. super() -> super()는 부모 객체라고 생각

* 5. Python의 모든 클래스는 object 클레스를 상속한다. : 모든 것은 객체이다.

* MyClass.mro() --> 상속 관계를 보여준다.
"""


class Robot:

    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

    @staticmethod
    def are_you_robot():
        print(f"{Robot.population} num!")
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name)  #  이렇게하면 self.name = name과 Siri.population += 1을 안적어줘도 됨!!
        self.age = age

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b

    def cal_flexable(self, a, b):
        super().say_hi()  # Greetings, my masters call me iphone8. # 오버라이딩 전 함수 실행
        self.say_hi()  # Greetings, my masters call me iphone8. by apple. # 오버라이딩 한 함수 실행
        return (
            self.cal_mul(a, b) + self.cal_add(a, b) + super().cal_add(a, b)
        )  # 여기서 self.cal_add()와 super().cal_add()는 동일한 함수임

    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple!!")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}. by apple.")

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots. by apple"


siri = Siri("iphone8", 17)

print(siri.age)
print(siri.name)

siri.say_hi()
print(Siri.how_many())

print(siri.cal_flexable(1, 3))


"""
Python 2:

class A:
    def __init__(self):
        ...

class B(A):
    def __init__(self):
        super(B, self).__init__()
"""
