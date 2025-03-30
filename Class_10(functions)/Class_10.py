from typing import Callable

# add: Callable[[int, int], int] = lambda x, y: x + y
# result = add(10, 20) # result will be 30
# print(result)

# from collections.abc import Iterator

# def my_range(start:int, end:int, stop: int=1) -> Iterator[int]:
#     for i in range(start,end,stop):
#         yield i

# a:Iterator[int] = my_range(1, 10)
# print(next(a))
# print(next(a))
# print(type(a))

def decorator(func: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is calling")
    return wrapper
    
@decorator
def say_hello()-> None:
    print("Hello!")

say_hello()
