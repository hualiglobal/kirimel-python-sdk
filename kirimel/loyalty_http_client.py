"""
Loyalty HTTP Client with HMAC SHA256 authentication
"""

import os
import time
import hmac
import hashlib
import json
import logging
from typing import Optional, Dict, Any
from datetime import datetime, timezone

from .exceptions import ApiException, AuthenticationException


class LoyaltyHttpClient:
    """HTTP client for Loyalty API with HMAC SHA256 signature authentication"""

    def __init__(
        self,
        client_key: Optional[str] = None,
        client_secret: Optional[str] = None,
        base_url: str = "https://kirimel.com",
        timeout: int = 30,
        retries: int = 3,
    ):
        self.base_url = base_url.rstrip("/")
        self.client_key = client_key or os.getenv("KIRIMEL_LOYALTY_CLIENT_KEY")
        self.client_secret = client_secret or os.getenv("KIRIMEL_LOYALTY_CLIENT_SECRET")
        self.timeout = timeout
        self.retries = retries

        if not self.client_key or not self.client_secret:
            raise AuthenticationException(
                "Loyalty API requires both client_key and client_secret. "
                "Set KIRIMEL_LOYALTY_CLIENT_KEY and KIRIMEL_LOYALTY_CLIENT_SECRET environment variables, "
                "or pass them in the config."
            )

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
        """Make HTTP request with HMAC signature"""
        import requests

        # Build signature headers
        timestamp = self._get_timestamp()
        payload = json.dumps(data) if data else ""
        signature = self._calculate_signature(timestamp, payload)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "KiriMel-Python-SDK/2.0.0",
            "X-Client-Key": self.client_key,
            "X-Timestamp": timestamp,
            "X-Signature": signature,
        }

        try:
            response = requests.request(
                method=method,
                url=url,
                data=payload if payload else None,
                headers=headers,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            # Network error - retry if attempts remain
            if attempt < self.retries - 1:
                time.sleep(0.1 * (attempt + 1))  # Exponential backoff
                return self._request(method, url, data, attempt + 1)
            raise ApiException(f"Network error: {str(e)}")

        if response.status_code >= 400:
            self._handle_error(response)

        return response.json()

    def _get_timestamp(self) -> str:
        """Get ISO 8601 timestamp in UTC"""
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def _calculate_signature(self, timestamp: str, payload: str) -> str:
        """Calculate HMAC SHA256 signature"""
        signing_string = f"{timestamp}.{payload}"
        signature = hmac.new(
            self.client_secret.encode(), signing_string.encode(), hashlib.sha256
        ).hexdigest()
        return signature

    def _handle_error(self, response) -> None:
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
        else:
            raise ApiException(message, response.status_code, errors)
