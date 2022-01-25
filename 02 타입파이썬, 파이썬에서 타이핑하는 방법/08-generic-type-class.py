"""
* 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술
"""

from typing import Union, Optional, TypeVar, Generic

T = TypeVar("T", int, float, str)
K = TypeVar("K", int, float, str)


# class Robot():
#     def __init__(self, arm: Union[int, str], head: int):
#         self.arm = arm
#         self.head = head

#     def decode(self):
#         # 암호를 해독하는 코드
#         # 복잡
#         # bbb: Optional[Union[int, str]] = None # 이 상황에서 arm에서 온 타입과 같은 타입 쓰고싶은데,
#         # 이렇게 쓰면 int or str 둘중 하나임. 약간 애매

#         pass


# robot1 = Robot(12231413, 23908409)


class Robot(Generic[T, K]):
    def __init__(self, arm: T, head: K):
        self.arm: T = arm
        self.head: K = head

    def decode(self):
        # 암호를 해독하는 코드
        # 복잡
        # bbb: Optional[T] = None # 이런 식으로 Generic으로 코딩하면 확실하다
        pass


robot1 = Robot[int, int](12231413, 23908409)
robot2 = Robot[str, int]("12890309123", 79878789)
robot3 = Robot[float, str](1239.01823, "3243245")
# robot4 = Robot[bool, list](True, [1,2,3]) # mypy에서 에러
# print(robot4.arm)


class Siri(Generic[T, K], Robot[T, K]):  # 제네릭 클래스 상속할 때
    pass


siri1 = Siri[int, int](12231413, 23908409)
siri2 = Siri[str, int]("12890309123", 79878789)
# siri3 = Siri[float, str]('1123', "3243245")

print(siri1.arm)

# * function


def test(x: T) -> T:
    print(x)
    print(type(x))
    return x


test(898)
