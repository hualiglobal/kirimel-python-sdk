"""Loyalty API resources"""

from .customers import Customers
from .points import Points
from .vouchers import Vouchers
from .wallet import Wallet

__all__ = ["Customers", "Points", "Vouchers", "Wallet"]
