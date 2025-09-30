# import asyncio
# from typing import List, Any, Dict
# from utils import create_response
# from algorithms.registry import register

# @register("bubble_sort")
# async def bubblesort(arr: List, send_event, data: Dict[str, Any]):
#     n = len(arr)

#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             # Send event when comparing
#             res = create_response(event_type=data["type"], cmd="compare", i=j, j=j+1, array=arr, sorting=data["sorting"])
#             await send_event(res)
#             await asyncio.sleep(3)

#             if(arr[j] > arr[j+1]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 # Send swapping event
#                 res = create_response(event_type=data["type"], cmd="swap", i=j, j=j+1, array=arr, sorting=data["sorting"])
#                 print(f"Response: {res}")
#                 await send_event(res)
#                 await asyncio.sleep(3.0)
#                 swapped = True
#         if (swapped == False):
#             break

#     # send done event
#     res = create_response(event_type=data["type"], cmd="done", array=arr, sorting=data["sorting"])
#     await send_event(res)
#     await asyncio.sleep(3.0)
