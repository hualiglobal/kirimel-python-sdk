"""
KiriMel Python SDK Client
"""

import os
from typing import Optional
from .http_client import HttpClient
from .loyalty_http_client import LoyaltyHttpClient
from .resources import (
    Campaigns,
    Subscribers,
    Lists,
    Segments,
    Templates,
    Forms,
    Conversions,
    LandingPages,
    Workflows,
    Webhooks,
    Email,
)
from .resources.loyalty import (
    Customers as LoyaltyCustomers,
    Points as LoyaltyPoints,
    Vouchers as LoyaltyVouchers,
    Wallet as LoyaltyWallet,
)


class KiriMel:
    """
    KiriMel API Client

    Example:
        >>> import kirimel
        >>> client = kirimel.KiriMel(api_key="sk_test_xxx")
        >>> campaigns = client.campaigns.list()
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://kirimel.com/api",
        timeout: int = 30,
        retries: int = 3,
        loyalty_api_key: Optional[str] = None,
        key_secret: Optional[str] = None,
    ):
        """
        Create a new API client

        Args:
            api_key: API key (or use KIRIMEL_API_KEY env variable)
            base_url: Base URL (default: https://kirimel.com/api)
            timeout: Request timeout in seconds (default: 30)
            retries: Number of retries (default: 3)
            loyalty_api_key: Loyalty API key (or use KIRIMEL_LOYALTY_API_KEY env var)
            key_secret: Loyalty API key secret (or use KIRIMEL_LOYALTY_KEY_SECRET env var)
        """
        self._http_client = HttpClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            retries=retries,
        )
        self._campaigns: Optional[Campaigns] = None
        self._subscribers: Optional[Subscribers] = None
        self._lists: Optional[Lists] = None
        self._segments: Optional[Segments] = None
        self._templates: Optional[Templates] = None
        self._forms: Optional[Forms] = None
        self._conversions: Optional[Conversions] = None
        self._landing_pages: Optional[LandingPages] = None
        self._workflows: Optional[Workflows] = None
        self._webhooks: Optional[Webhooks] = None
        self._email: Optional[Email] = None

        # Loyalty API clients
        self._loyalty_http_client: Optional[LoyaltyHttpClient] = None
        self._loyalty_customers: Optional[LoyaltyCustomers] = None
        self._loyalty_points: Optional[LoyaltyPoints] = None
        self._loyalty_vouchers: Optional[LoyaltyVouchers] = None
        self._loyalty_wallet: Optional[LoyaltyWallet] = None

        # Store credentials for lazy initialization
        self._loyalty_base_url = base_url.replace("/api", "")
        self._loyalty_api_key = loyalty_api_key or os.getenv("KIRIMEL_LOYALTY_API_KEY")
        self._loyalty_key_secret = key_secret or os.getenv("KIRIMEL_LOYALTY_KEY_SECRET")
        self._loyalty_timeout = timeout
        self._loyalty_retries = retries

    def _init_loyalty_client(self) -> None:
        """Initialize loyalty HTTP client (lazy initialization)"""
        if self._loyalty_http_client is None:
            self._loyalty_http_client = LoyaltyHttpClient(
                api_key=self._loyalty_api_key,
                key_secret=self._loyalty_key_secret,
                base_url=self._loyalty_base_url,
                timeout=self._loyalty_timeout,
                retries=self._loyalty_retries,
            )

    @property
    def campaigns(self) -> Campaigns:
        """Get campaigns resource client"""
        if self._campaigns is None:
            self._campaigns = Campaigns(self._http_client)
        return self._campaigns

    @property
    def subscribers(self) -> Subscribers:
        """Get subscribers resource client"""
        if self._subscribers is None:
            self._subscribers = Subscribers(self._http_client)
        return self._subscribers

    @property
    def lists(self) -> Lists:
        """Get lists resource client"""
        if self._lists is None:
            self._lists = Lists(self._http_client)
        return self._lists

    @property
    def segments(self) -> Segments:
        """Get segments resource client"""
        if self._segments is None:
            self._segments = Segments(self._http_client)
        return self._segments

    @property
    def templates(self) -> Templates:
        """Get templates resource client"""
        if self._templates is None:
            self._templates = Templates(self._http_client)
        return self._templates

    @property
    def forms(self) -> Forms:
        """Get forms resource client"""
        if self._forms is None:
            self._forms = Forms(self._http_client)
        return self._forms

    @property
    def conversions(self) -> Conversions:
        """Get conversions resource client"""
        if self._conversions is None:
            self._conversions = Conversions(self._http_client)
        return self._conversions

    @property
    def landing_pages(self) -> LandingPages:
        """Get landing pages resource client"""
        if self._landing_pages is None:
            self._landing_pages = LandingPages(self._http_client)
        return self._landing_pages

    @property
    def workflows(self) -> Workflows:
        """Get workflows resource client"""
        if self._workflows is None:
            self._workflows = Workflows(self._http_client)
        return self._workflows

    @property
    def webhooks(self) -> Webhooks:
        """Get webhooks resource client"""
        if self._webhooks is None:
            self._webhooks = Webhooks(self._http_client)
        return self._webhooks

    @property
    def email(self) -> Email:
        """Get email resource client for transactional emails"""
        if self._email is None:
            self._email = Email(self._http_client)
        return self._email

    @property
    def loyalty_customers(self) -> LoyaltyCustomers:
        """Get loyalty customers resource client"""
        self._init_loyalty_client()
        if self._loyalty_customers is None:
            self._loyalty_customers = LoyaltyCustomers(self._loyalty_http_client)
        return self._loyalty_customers

    @property
    def loyalty_points(self) -> LoyaltyPoints:
        """Get loyalty points resource client"""
        self._init_loyalty_client()
        if self._loyalty_points is None:
            self._loyalty_points = LoyaltyPoints(self._loyalty_http_client)
        return self._loyalty_points

    @property
    def loyalty_vouchers(self) -> LoyaltyVouchers:
        """Get loyalty vouchers resource client"""
        self._init_loyalty_client()
        if self._loyalty_vouchers is None:
            self._loyalty_vouchers = LoyaltyVouchers(self._loyalty_http_client)
        return self._loyalty_vouchers

    @property
    def loyalty_wallet(self) -> LoyaltyWallet:
        """Get loyalty wallet resource client"""
        self._init_loyalty_client()
        if self._loyalty_wallet is None:
            self._loyalty_wallet = LoyaltyWallet(self._loyalty_http_client)
        return self._loyalty_wallet
