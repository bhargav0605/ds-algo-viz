from typing import Final
from types import MappingProxyType

_SHORTS = {
    "bubble_sort": "bs",
    "merge_sort": "ms",
    "quick_sort": "qs",
    "insertion_sort": "is",
    "selection_sort": "ss",
    "heap_sort": "hs",
    "radix_sort": "rs",
    "counting_sort": "cs",
    "shell_sort": "shs",
}

SHORT_FORMS: Final[dict[str, str]] = MappingProxyType(_SHORTS)

_LONG_FORMS = {v: k for k, v in _SHORTS.items()}
LONG_FORMS: Final[dict[str, str]] = MappingProxyType(_LONG_FORMS)