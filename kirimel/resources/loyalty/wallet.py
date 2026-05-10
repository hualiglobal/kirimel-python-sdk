"""Loyalty Wallet resource"""
from typing import Dict, Any, Optional


class Wallet:
    """Loyalty Wallet resource client"""

    def __init__(self, http_client):
        self._http = http_client

    def balance(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get wallet balance

        Args:
            data: Query data (customer_id)

        Returns:
            Balance data with available_points, pending_points, expired_points
        """
        return self._http.post("/api/loyalty/wallet/balance", data)

    def recalculate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recalculate balance from ledger

        Args:
            data: Customer data (customer_id)

        Returns:
            Recalculated balance
        """
        return self._http.post("/api/loyalty/wallet/recalculate", data)
