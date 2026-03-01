"""
KiriMel Python SDK

Official Python SDK for KiriMel Email Marketing API.
"""
from .client import KiriMel
from .exceptions import (
    ApiException,
    AuthenticationException,
    RateLimitException,
    ValidationException,
)

__version__ = "0.1.0"
__all__ = [
    "KiriMel",
    "ApiException",
    "AuthenticationException",
    "RateLimitException",
    "ValidationException",
]
