# class types: 클래스 자체를 타이핑


class Hello:
    def world(self) -> int:
        return 7


class World:
    pass


hello: Hello = Hello()
world: World = World()
 

# 타이핑을 해주어서 ins에 점찍으면 world 메소드 보임.
def foo(ins: Hello) -> int:
    return ins.world()


print(foo(hello))


# * class type 보충

from typing import Optional


# 연결리스트

class Node:
    def __init__(self, data: int, node: Optional["Node"] = None):
        self.data = data
        self.node = node


node2 = Node(12)

node1 = Node(27, node2)
print((node1.node.data))  # 12

node0 = Node(30, node1)

# node2 <- node1 <- node0
