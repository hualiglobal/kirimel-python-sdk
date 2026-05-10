"""Loyalty Customers resource"""

from typing import Dict, Any, Optional


class Customers:
    """Loyalty Customers resource client"""

    def __init__(self, http_client):
        self._http = http_client

    def register(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Register a new loyalty customer

        Args:
            data: Customer data including phone, name, email, birth_date, qr_code

        Returns:
            Created customer data
        """
        return self._http.post("/api/loyalty/customers/register", data)

    def lookup(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Look up customer by phone

        Args:
            data: Lookup criteria including phone

        Returns:
            Customer data
        """
        return self._http.post("/api/loyalty/customers/lookup", data)

    def get(self, customer_id: str) -> Dict[str, Any]:
        """
        Get customer profile

        Args:
            customer_id: Customer ID

        Returns:
            Customer profile data
        """
        return self._http.get(f"/api/loyalty/customers/{customer_id}")

    def transactions(
        self, customer_id: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Get customer transactions

        Args:
            customer_id: Customer ID
            params: Query parameters (page, per_page)

        Returns:
            Transaction history
        """
        return self._http.get(f"/api/loyalty/customers/{customer_id}/transactions", params)

    def adjust(self, customer_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Manually adjust customer points

        Args:
            customer_id: Customer ID
            data: Adjustment data (points, reference, description, adjusted_by)

        Returns:
            Adjustment result
        """
        return self._http.post(f"/api/loyalty/customers/{customer_id}/adjust", data)

    def tier(self, customer_id: str) -> Dict[str, Any]:
        """
        Get customer tier information

        Args:
            customer_id: Customer ID

        Returns:
            Tier data
        """
        return self._http.get(f"/api/loyalty/customers/{customer_id}/tier")

    def list(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        List all customers

        Args:
            params: Query parameters (page, per_page, tier)

        Returns:
            Paginated customer list
        """
        return self._http.get("/api/loyalty/customers", params)
