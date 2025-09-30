# import random
# import time
# import numpy
# from typing import List, Any, Dict, Optional

# def create_response(
#         event_type: str,
#         cmd: str,
#         sorting: str,
#         array: Optional[List[Any]] = None,
#         minSize: int = 0,
#         maxSize: int = 0,
#         minRange: int = 0,
#         maxRange: int = 0,
#         i: int = 0,
#         j: int = 0) -> Dict:
#     return {
#         "type": event_type,
#         "cmd": cmd,
#         "array": array,
#         "sorting": sorting,
#         "minSize": minSize,
#         "maxSize": maxSize,
#         "minRange": minRange,
#         "maxRange": maxRange,
#         "i": i,
#         "j": j,
#     }

# # Generating an array here (kept exactly as your original prints/behaviour)
# def generate_array(minRange: int, maxRange: int, minSize: int, maxSize: int):
#     print("Generating number")
#     size_array = random.randint(minSize, maxSize)
#     print(f"Size of an array is {size_array}")

#     random_integers_1D = numpy.random.randint(minRange, maxRange, size=size_array)
#     return random_integers_1D.tolist()
