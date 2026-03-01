"""Unit tests for KiriMel Python SDK"""
import pytest
from kirimel import KiriMel


class TestKiriMelClient:
    """Test KiriMel client initialization and resources"""

    def test_client_instantiation(self):
        """Test client can be instantiated"""
        client = KiriMel(api_key="test_key")
        assert client is not None

    def test_campaigns_resource_exists(self):
        """Test campaigns resource exists"""
        client = KiriMel(api_key="test_key")
        assert client.campaigns is not None

    def test_subscribers_resource_exists(self):
        """Test subscribers resource exists"""
        client = KiriMel(api_key="test_key")
        assert client.subscribers is not None

    def test_lists_resource_exists(self):
        """Test lists resource exists"""
        client = KiriMel(api_key="test_key")
        assert client.lists is not None
