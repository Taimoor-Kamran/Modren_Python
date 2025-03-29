from typing import Callable

add: Callable[[int, int], int] = lambda x, y: x + y
result = add(10, 20) # result will be 30
print(result)