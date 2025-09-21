import asyncio
from typing import Any, Callable, Awaitable, List
SendEvent = Callable[[str], Awaitable[None]]
async def bubble_sort(arr: list[any], send_event: SendEvent):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            await send_event(f"Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                await send_event(f"Swap {arr[j]} and {arr[j+1]}")
        if (swapped == False):
            break
    await send_event(f"Done Sorted")
    print(arr)

async def print_event(msg: str):
    print(msg)

async def main():
    arr = [4,3,2,1]
    await bubble_sort(arr, print_event)
    print(f"Done")

if __name__ == "__main__":
    asyncio.run(main())