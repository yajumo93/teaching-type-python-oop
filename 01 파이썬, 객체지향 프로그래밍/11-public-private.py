"""
캡슐화

파이썬은 public, private만 제공

* public vs private

protect는 언더바 하나로 쓰기로 약속, 그러나 외부에서도 접근가능해서 명실상부함

"""


class Robot:

    """
    Robot Class
    """

    __population = 0

    def __init__(self, name, age, protected_num):
        self.name = name
        self.__age = age  # age 은닉
        self._protected_num = protected_num
        # Robot.population += 1
        Robot.__population += 1

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."


class Siri(Robot):
    def __init__(self, name, age, protected_num):
        super().__init__(name, age, protected_num)
        print(self.name)
        # print(self.__age) # 읽지못함
        print("== private reassign ==")
        self.__age = 999  # 새로 쓰기 가능
        print(self.__age)  # 999
        print(self.name)

        print(self._protected_num)  # 언더바 하나로 protect 사용


ss = Robot("yss", 8, 6)

# print(ss.__age)  # 읽지도 못함

# ss.age = -999


ssss = Siri("iphone8", 9, 8)

# print(ssss._age)

