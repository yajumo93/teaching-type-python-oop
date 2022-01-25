"""
# 객체 내에 있는 변수들은 __dict__를 통해서 관리가 된다.
# __slots__을 통해 변수를 관리 :
# 파이썬 인터프리터에게 통보 해당 클래스가 가지는 속성을 제한한다.
# __dict__를 통해 관리되는 객체의 성능을 최적화한다. -> 다수의 객체 생성시 메모리 사용 공간 대폭 감소한다.
"""

import timeit


# 슬롯 X
class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithoutSlotClass("amamov", 12)

print(wos.__dict__)  # {'name': 'amamov', 'age': 12}

wos.__dict__["hello"] = "world"

print(wos.__dict__)  # 추가됨. {'name': 'amamov', 'age': 12, 'hello': 'world'}


# 슬롯 O
class WithSlotClass:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age


ws = WithSlotClass("amamov", 12)

# print(ws.__dict__) # AttributeError: 'WithSlotClass' object has no attribute '__dict__'
print(ws.__slots__)  # ['name', 'age'] // 딕셔너리를 사용하지 않아서 메모리 절감 효과


# * 메모리 사용량 비교


def repeat(obj):
    def inner():
        obj.name = "amamov"
        obj.age = 222
        del obj.name
        del obj.age

    return inner


use_slot_time = timeit.repeat(repeat(ws), number=9999999)  # name을 썼다 지웠다 반복
no_slot_time = timeit.repeat(repeat(wos), number=9999999)


print("use slot : ", min(use_slot_time))
print("no slot : ", min(no_slot_time))
