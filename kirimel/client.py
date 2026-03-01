"""
KiriMel Python SDK Client
"""
from typing import Optional
from .http_client import HttpClient
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
    ):
        """
        Create a new API client

        Args:
            api_key: API key (or use KIRIMEL_API_KEY env variable)
            base_url: Base URL (default: https://kirimel.com/api)
            timeout: Request timeout in seconds (default: 30)
            retries: Number of retries (default: 3)
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
