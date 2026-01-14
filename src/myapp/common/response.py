"""
Docstring for myapp.Common.response
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class Response:
    """
    Docstring for Response
    """

    status: int
    msg: str
    content: Any
