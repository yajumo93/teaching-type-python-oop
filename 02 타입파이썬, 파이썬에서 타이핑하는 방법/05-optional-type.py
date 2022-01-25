# * Optional type

from typing import Optional


# return이 str일수도 있고 None일수도 있다
def foo(name: str) -> Optional[str]:
    if name == "amamov":
        return None
    else:
        return name


xxx: Optional[str] = foo("amamov")

print(xxx)