"""Loyalty Vouchers resource"""

from typing import Dict, Any, Optional


class Vouchers:
    """Loyalty Vouchers resource client"""

    def __init__(self, http_client):
        self._http = http_client

    def create_batch(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a voucher batch

        Args:
            data: Batch data (name, type, value, quantity, valid_from, valid_until, etc.)

        Returns:
            Created batch data
        """
        return self._http.post("/api/loyalty/vouchers/batches", data)

    def list_batches(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        List voucher batches

        Args:
            params: Query parameters (page, per_page)

        Returns:
            Paginated batch list
        """
        return self._http.get("/api/loyalty/vouchers/batches", params)

    def issue(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Issue voucher to customer

        Args:
            data: Issue data (voucher_batch_id, customer_id, delivered_via, reference_id)

        Returns:
            Issued voucher data
        """
        return self._http.post("/api/loyalty/vouchers/issue", data)

    def redeem(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Redeem voucher

        Args:
            data: Redemption data (code, customer_id, purchase_amount, reference_id)

        Returns:
            Redemption result with discount amount
        """
        return self._http.post("/api/loyalty/vouchers/redeem", data)

    def get(self, code: str) -> Dict[str, Any]:
        """
        Get voucher details

        Args:
            code: Voucher code

        Returns:
            Voucher details
        """
        return self._http.get(f"/api/loyalty/vouchers/{code}")
