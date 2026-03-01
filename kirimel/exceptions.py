"""
KiriMel SDK Exception Classes
"""


class ApiException(Exception):
    """Base API exception"""

    def __init__(self, message: str, status_code: int = None, errors: dict = None):
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

    def __init__(self, message: str, status_code: int = None, errors: dict = None, retry_after: int = None):
        super().__init__(message, status_code, errors)
        self.retry_after = retry_after


class ValidationException(ApiException):
    """Validation exception (422)"""

    error_type = "validation_error"
