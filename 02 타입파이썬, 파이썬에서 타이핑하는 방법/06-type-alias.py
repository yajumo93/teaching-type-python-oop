# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#type-aliases

from typing import Union, List, Tuple, Dict, Optional
from typing_extensions import TypedDict

# * type alias
Value = Union[
    int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]
]

# * type alias
X = int

x: X = 8

value: Value = 17


def cal(v: Value) -> Value:
    # 연산..
    return v


# * dict alias

ddd: Dict[str, Union[str, int]] = {"hello": "world", "world": "wow!!", "hee": 17}

# key 값을 사전에 정의하고 타입을 정확히 지정
class Point(TypedDict):
    x: int
    y: float
    z: str
    hello: int


point: Point = {"x": 8, "y": 8.4, "z": "hello", "hello": 12}
