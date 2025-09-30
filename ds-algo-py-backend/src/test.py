# import asyncio
# from typing import Any, Callable, Awaitable, List
# SendEvent = Callable[[str], Awaitable[None]]
# async def bubble_sort(arr: list[any], send_event: SendEvent):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             await send_event(f"Comparing {arr[j]} and {arr[j+1]}")
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#                 await send_event(f"Swap {arr[j]} and {arr[j+1]}")
#         if (swapped == False):
#             break
#     await send_event(f"Done Sorted")
#     print(arr)

# async def print_event(msg: str):
#     print(msg)

# async def main():
#     arr = [4,3,2,1]
#     await bubble_sort(arr, print_event)
#     print(f"Done")

# if __name__ == "__main__":
#     asyncio.run(main())

# response = {
#     "type": "random",
#     "cmd": "generate",
#     "minSize": 1,
#     "maxSize": 100,
#     "minRange": 5,
#     "maxRange": 500,
# }
# from typing import List
# from dataclasses import dataclass

# @dataclass
# class Request:
#     type: str
#     cmd: str
#     minSize: int
#     maxSize: int
#     minRange: int
#     maxRange: int

# def generate_array(r1: Request) -> List[int]:
#     print(r1)
#     return [1,2,3]

# r1 = Request(type="random", cmd="generate", minSize=1, maxSize=100, minRange=5, maxRange=500)
# arr = generate_array(r1)
# print(arr)

# import numpy as np
# import random as rs

# size_array = rs.randint(1, 5)
# print(f"Size of an array is {size_array}")

# # Generate a 1D array of 10 random integers between 0 (inclusive) and 100 (exclusive)
# random_integers_1d = np.random.randint(-30, 100, size=size_array)
# print(f"1D Array of Random Integers: {random_integers_1d}")
