"""
KiriMel SDK Exception Classes
"""

from typing import Optional, Dict, Any


class ApiException(Exception):
    """Base API exception"""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        errors: Optional[Dict[str, Any]] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.errors = errors
        super().__init__(self.message)

    def __str__(self):
        return self.message


class AuthenticationException(ApiException):
    """Authentication exception (401)"""

    error_type = "authentication_error"


class RateLimitException(ApiException):
    """Rate limit exception (429)"""

    error_type = "rate_limit_error"

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        errors: Optional[Dict[str, Any]] = None,
        retry_after: Optional[int] = None,
    ):
        super().__init__(message, status_code, errors)
        self.retry_after = retry_after


class ValidationException(ApiException):
    """Validation exception (422)"""

    error_type = "validation_error"
