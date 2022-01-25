from typing import List, Tuple, Dict

# 중요한 함수에 타입 힌트를 쓰는게 좋다
# type hint. 단지 hint역할이라 검사를 해서 에러를 발생시키지는 않음
int_var: int = 88
str_var: str = "hello world"
float_var: float = 88.9
bool_var: bool = True

str_var2: str = 8  # mypy error check

list_var: List[str] = ["1", "2", "3"]
tuple_var: Tuple[int, ...] = (1, 3, 4)

dic_var: Dict[str, int] = {"hello": 47}


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


# 인자도, 리턴도 int다
def cal_add(x: int, y: int) -> int:
    # code
    # type_check(x, int)
    # type_check(y, int)
    return x + y


print(cal_add(1, 3))

# print(cal_add("1, ", "3, dsjkakljas"))

# print(cal_add([1, 3], [4, 5]))

# * isinstance(obj, class)

# print(isinstance("ashdjkasd", str))
# print(isinstance(88.9, float))

print(int_var)
