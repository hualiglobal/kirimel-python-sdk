"""
HTTP Client for KiriMel API
"""
import os
import time
import logging
from typing import Optional, Dict, Any, List
import requests

from .exceptions import ApiException, AuthenticationException, RateLimitException, ValidationException


class HttpClient:
    """HTTP client for making API requests"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://kirimel.com/api",
        timeout: int = 30,
        retries: int = 3,
    ):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key or os.getenv("KIRIMEL_API_KEY")
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)

    def set_logger(self, logger: logging.Logger) -> None:
        """Set a custom logger"""
        self.logger = logger

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request"""
        url = self._build_url(path, params or {})
        return self._request("GET", url)

    def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a POST request"""
        return self._request("POST", self._build_url(path), data)

    def put(self, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a PUT request"""
        return self._request("PUT", self._build_url(path), data)

    def delete(self, path: str) -> Dict[str, Any]:
        """Make a DELETE request"""
        return self._request("DELETE", self._build_url(path))

    def _build_url(self, path: str, params: Optional[Dict[str, Any]] = None) -> str:
        """Build URL with query parameters"""
        url = f"{self.base_url}/{path.lstrip('/')}"
        if params:
            import urllib.parse
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"
        return url

    def _request(
        self,
        method: str,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        attempt: int = 0,
    ) -> Dict[str, Any]:
        """Make HTTP request with retry logic"""
        self.logger.debug(f"Making {method} request to {url}", extra={"attempt": attempt + 1})

        headers = self._build_headers()

        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                headers=headers,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            # Network error - retry if attempts remain
            if attempt < self.retries - 1:
                self.logger.warning(f"Network error, retrying...", extra={"error": str(e)})
                time.sleep(0.1 * (attempt + 1))  # Exponential backoff
                return self._request(method, url, data, attempt + 1)
            raise ApiException(f"Network error: {str(e)}")

        if response.status_code >= 400:
            self._handle_error(response, url, attempt)

        return response.json()

    def _build_headers(self) -> Dict[str, str]:
        """Build request headers"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "KiriMel-Python-SDK/0.1.0",
        }

        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        return headers

    def _handle_error(self, response: requests.Response, url: str, attempt: int) -> None:
        """Handle API errors"""
        try:
            data = response.json()
            message = data.get("message", "API request failed")
            errors = data.get("errors")
        except ValueError:
            message = response.text or "API request failed"
            errors = None

        if response.status_code == 401:
            raise AuthenticationException(message, response.status_code, errors)
        elif response.status_code == 429:
            retry_after = data.get("retry_after") if errors else None
            if retry_after and attempt < self.retries - 1:
                self.logger.info(f"Rate limited, waiting {retry_after}s...")
                time.sleep(retry_after)
                return  # Will retry
            raise RateLimitException(message, response.status_code, errors, retry_after)
        elif response.status_code == 422:
            raise ValidationException(message, response.status_code, errors)
        else:
            raise ApiException(message, response.status_code, errors)
