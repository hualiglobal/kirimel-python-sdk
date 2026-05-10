"""Loyalty Points resource"""
from typing import Dict, Any, Optional


class Points:
    """Loyalty Points resource client"""

    def __init__(self, http_client):
        self._http = http_client

    def earn(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Award points to customer

        Args:
            data: Earn data (customer_id, points, amount, reference_id, description)

        Returns:
            Points transaction result
        """
        return self._http.post("/api/loyalty/points/earn", data)

    def preview_redeem(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Preview points redemption (check before confirming)

        Args:
            data: Preview data (customer_id, points_to_redeem)

        Returns:
            Preview with points_value, max_redeemable, amount_discount
        """
        return self._http.post("/api/loyalty/points/preview-redeem", data)

    def commit_redeem(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Confirm points redemption

        Args:
            data: Redemption data (customer_id, points_to_redeem, reference_id)

        Returns:
            Redemption transaction result
        """
        return self._http.post("/api/loyalty/points/redeem", data)

    def reverse(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reverse a points transaction

        Args:
            data: Reverse data (transaction_id, reason, reference_id)

        Returns:
            Reversal result
        """
        return self._http.post("/api/loyalty/points/reverse", data)
