# from typing import Callable, Dict
# from helper.constant import SHORT_FORMS, LONG_FORMS

# # registry: canonical name -> coroutine function
# _REGISTRY: Dict[str, Callable] = {}

# def register(name: str):
#     """Decorator to register an algorithm under its canonical name."""
#     def _decorator(func):
#         _REGISTRY[name] = func
#         return func
#     return _decorator

# def get_by_input(name: str):
#     """Resolve an input (short or long) to canonical name and return function.

#     name: either 'bubble_sort' or 'bs' (or other entries in constants)
#     """
#     if name in SHORT_FORMS:
#         canonical = name
#     elif name in LONG_FORMS:
#         canonical = LONG_FORMS[name]
#     else:
#         raise KeyError(f"Unknown algorithm: {name}")
#     return _REGISTRY[canonical]
