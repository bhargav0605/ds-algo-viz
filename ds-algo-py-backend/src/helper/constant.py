from typing import Final
from types import MappingProxyType

_SHORTS = {
    "bubble_sort": "bs"
}

SHORT_FORMS: Final[dict[str, str]] = MappingProxyType(_SHORTS)

_LONG_FORMS = {v: k for k, v in _SHORTS.items()}
LONG_FORMS: Final[dict[str, str]] = MappingProxyType(_LONG_FORMS)