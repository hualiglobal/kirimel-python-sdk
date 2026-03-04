"""
Resource clients for KiriMel API
"""
from typing import Optional, Dict, Any, List
from ..http_client import HttpClient


class ResourceClient:
    """Base class for resource clients"""

    def __init__(self, http_client: HttpClient):
        self._http_client = http_client


class Campaigns(ResourceClient):
    """Campaigns resource client"""

    def list(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """List campaigns"""
        return self._http_client.get("campaigns", params or {})

    def recent(self) -> Dict[str, Any]:
        """Get recent campaigns"""
        return self._http_client.get("campaigns/recent")

    def get(self, campaign_id: int) -> Dict[str, Any]:
        """Get single campaign"""
        return self._http_client.get(f"campaigns/{campaign_id}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create campaign"""
        return self._http_client.post("campaigns", data)

    def update(self, campaign_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update campaign"""
        return self._http_client.post(f"campaigns/{campaign_id}", data)

    def delete(self, campaign_id: int) -> Dict[str, Any]:
        """Delete campaign"""
        return self._http_client.post(f"campaigns/{campaign_id}/delete")

    def duplicate(self, campaign_id: int) -> Dict[str, Any]:
        """Duplicate campaign"""
        return self._http_client.post(f"campaigns/{campaign_id}/duplicate")

    def schedule(self, campaign_id: int, scheduled_at: str) -> Dict[str, Any]:
        """Schedule campaign"""
        return self._http_client.post(f"campaigns/{campaign_id}/schedule", {"scheduled_at": scheduled_at})

    def pause(self, campaign_id: int) -> Dict[str, Any]:
        """Pause campaign"""
        return self._http_client.post(f"campaigns/{campaign_id}/pause")

    def resume(self, campaign_id: int) -> Dict[str, Any]:
        """Resume campaign"""
        return self._http_client.post(f"campaigns/{campaign_id}/resume")

    def stats(self, campaign_id: int) -> Dict[str, Any]:
        """Get campaign statistics"""
        return self._http_client.get(f"campaigns/{campaign_id}/stats")


class Subscribers(ResourceClient):
    """Subscribers resource client"""

    def list(self, list_id: int, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """List subscribers for a list"""
        return self._http_client.get(f"lists/{list_id}/subscribers", params or {})

    def list_all(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """List all subscribers"""
        return self._http_client.get("subscribers", params or {})

    def get(self, subscriber_id: int) -> Dict[str, Any]:
        """Get single subscriber"""
        return self._http_client.get(f"subscribers/{subscriber_id}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Add subscriber"""
        return self._http_client.post("subscribers", data)

    def update(self, subscriber_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update subscriber"""
        return self._http_client.post(f"subscribers/{subscriber_id}", data)

    def delete(self, subscriber_id: int) -> Dict[str, Any]:
        """Delete subscriber"""
        return self._http_client.delete(f"subscribers/{subscriber_id}")

    def unsubscribe(self, subscriber_id: int) -> Dict[str, Any]:
        """Unsubscribe subscriber"""
        return self._http_client.post(f"subscribers/{subscriber_id}/unsubscribe")

    def bulk_unsubscribe(self, subscriber_ids: List[int]) -> Dict[str, Any]:
        """Bulk unsubscribe"""
        return self._http_client.post("subscribers/bulk-unsubscribe", {"subscriber_ids": subscriber_ids})

    def bulk_delete(self, subscriber_ids: List[int]) -> Dict[str, Any]:
        """Bulk delete"""
        return self._http_client.post("subscribers/bulk-delete", {"subscriber_ids": subscriber_ids})

    def activity(self, subscriber_id: int) -> Dict[str, Any]:
        """Get subscriber activity"""
        return self._http_client.get(f"subscribers/{subscriber_id}/activity")

    def stats(self, subscriber_id: int) -> Dict[str, Any]:
        """Get subscriber statistics"""
        return self._http_client.get(f"subscribers/{subscriber_id}/stats")

    def toggle_vip(self, subscriber_id: int) -> Dict[str, Any]:
        """Toggle VIP status"""
        return self._http_client.post(f"subscribers/{subscriber_id}/toggle-vip")

    def search(self, query: str) -> Dict[str, Any]:
        """Search subscribers"""
        return self._http_client.get("subscribers/search", {"q": query})

    def add_tag(self, subscriber_id: int, tag: str) -> Dict[str, Any]:
        """Add tag to subscriber"""
        return self._http_client.post(f"subscribers/{subscriber_id}/tags", {"tag": tag})

    def remove_tag(self, subscriber_id: int, tag: str) -> Dict[str, Any]:
        """Remove tag from subscriber"""
        return self._http_client.post(f"subscribers/{subscriber_id}/tags/{tag}/remove")

    def import_subscribers(self, list_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Import subscribers"""
        return self._http_client.post(f"lists/{list_id}/subscribers/import", data)


class Lists(ResourceClient):
    """Lists resource client"""

    def list(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """List all lists"""
        return self._http_client.get("lists", params or {})

    def get(self, list_id: int) -> Dict[str, Any]:
        """Get single list"""
        return self._http_client.get(f"lists/{list_id}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create list"""
        return self._http_client.post("lists", data)

    def update(self, list_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update list"""
        return self._http_client.post(f"lists/{list_id}", data)

    def delete(self, list_id: int) -> Dict[str, Any]:
        """Delete list"""
        return self._http_client.delete(f"lists/{list_id}")

    def stats(self, list_id: int) -> Dict[str, Any]:
        """Get list statistics"""
        return self._http_client.get(f"lists/{list_id}/stats")


class Segments(ResourceClient):
    """Segments resource client"""

    def list(self, list_id: int) -> Dict[str, Any]:
        """List segments for a list"""
        return self._http_client.get(f"lists/{list_id}/segments")

    def get(self, segment_id: int) -> Dict[str, Any]:
        """Get single segment"""
        return self._http_client.get(f"segments/{segment_id}")

    def create(self, list_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create segment"""
        return self._http_client.post(f"lists/{list_id}/segments", data)

    def update(self, segment_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update segment"""
        return self._http_client.post(f"segments/{segment_id}", data)

    def delete(self, segment_id: int) -> Dict[str, Any]:
        """Delete segment"""
        return self._http_client.post(f"segments/{segment_id}/delete")

    def preview(self, list_id: int, conditions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Preview segment (without saving)"""
        return self._http_client.post(f"lists/{list_id}/segments/preview", {"conditions": conditions})

    def subscribers(self, segment_id: int, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Get segment subscribers"""
        return self._http_client.get(f"segments/{segment_id}/subscribers", params or {})

    def refresh(self, segment_id: int) -> Dict[str, Any]:
        """Refresh segment count"""
        return self._http_client.post(f"segments/{segment_id}/refresh")

    def logs(self, segment_id: int) -> Dict[str, Any]:
        """Get segment build logs"""
        return self._http_client.get(f"segments/{segment_id}/logs")

    def templates(self) -> Dict[str, Any]:
        """Get segment templates"""
        return self._http_client.get("segments/templates")

    def fields(self) -> Dict[str, Any]:
        """Get available fields"""
        return self._http_client.get("segments/fields")


class Templates(ResourceClient):
    """Templates resource client"""

    def list(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """List all templates"""
        return self._http_client.get("templates", params or {})

    def get(self, template_id: int) -> Dict[str, Any]:
        """Get single template"""
        return self._http_client.get(f"templates/{template_id}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create template"""
        return self._http_client.post("templates", data)

    def update(self, template_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update template"""
        return self._http_client.post(f"templates/{template_id}", data)

    def delete(self, template_id: int) -> Dict[str, Any]:
        """Delete template"""
        return self._http_client.post(f"templates/{template_id}/delete")

    def duplicate(self, template_id: int) -> Dict[str, Any]:
        """Duplicate template"""
        return self._http_client.post(f"templates/{template_id}/duplicate")

    def by_category(self, category: str) -> Dict[str, Any]:
        """Get templates by category"""
        return self._http_client.get(f"templates/category/{category}")

    def search(self, query: str) -> Dict[str, Any]:
        """Search templates"""
        return self._http_client.get("templates/search", {"q": query})

    def categories(self) -> Dict[str, Any]:
        """Get categories"""
        return self._http_client.get("templates/categories")


class Forms(ResourceClient):
    """Forms resource client"""

    def list(self) -> Dict[str, Any]:
        """List all forms"""
        return self._http_client.get("forms")

    def get(self, form_id: int) -> Dict[str, Any]:
        """Get single form"""
        return self._http_client.get(f"forms/{form_id}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create form"""
        return self._http_client.post("forms", data)

    def update(self, form_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update form"""
        return self._http_client.post(f"forms/{form_id}", data)

    def delete(self, form_id: int) -> Dict[str, Any]:
        """Delete form"""
        return self._http_client.post(f"forms/{form_id}/delete")

    def duplicate(self, form_id: int) -> Dict[str, Any]:
        """Duplicate form"""
        return self._http_client.post(f"forms/{form_id}/duplicate")

    def analytics(self, form_id: int) -> Dict[str, Any]:
        """Get form analytics"""
        return self._http_client.get(f"forms/{form_id}/analytics")

    def submissions(self, form_id: int, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Get form submissions"""
        return self._http_client.get(f"forms/{form_id}/submissions", params or {})

    def embed(self, form_id: int) -> Dict[str, Any]:
        """Get embed code"""
        return self._http_client.get(f"forms/{form_id}/embed")


class Conversions(ResourceClient):
    """Conversions resource client"""

    def list(self) -> Dict[str, Any]:
        """List all conversion goals"""
        return self._http_client.get("conversions")

    def get(self, goal_id: int) -> Dict[str, Any]:
        """Get single conversion goal"""
        return self._http_client.get(f"conversions/{goal_id}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create conversion goal"""
        return self._http_client.post("conversions", data)

    def update(self, goal_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update conversion goal"""
        return self._http_client.post(f"conversions/{goal_id}", data)

    def delete(self, goal_id: int) -> Dict[str, Any]:
        """Delete conversion goal"""
        return self._http_client.post(f"conversions/{goal_id}/delete")

    def track(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Track a conversion"""
        return self._http_client.post("conversions/track", data)

    def conversions(self, goal_id: int) -> Dict[str, Any]:
        """Get conversions for a goal"""
        return self._http_client.get(f"conversions/{goal_id}/conversions")

    def roi(self) -> Dict[str, Any]:
        """Get ROI report"""
        return self._http_client.get("conversions/roi")

    def funnel(self, goal_id: int) -> Dict[str, Any]:
        """Get funnel analysis"""
        return self._http_client.get(f"conversions/{goal_id}/funnel")


class LandingPages(ResourceClient):
    """Landing Pages resource client"""

    def list(self) -> Dict[str, Any]:
        """List all landing pages"""
        return self._http_client.get("landing-pages")

    def get(self, page_id: int) -> Dict[str, Any]:
        """Get single landing page"""
        return self._http_client.get(f"landing-pages/{page_id}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create landing page"""
        return self._http_client.post("landing-pages", data)

    def update(self, page_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update landing page"""
        return self._http_client.post(f"landing-pages/{page_id}", data)

    def delete(self, page_id: int) -> Dict[str, Any]:
        """Delete landing page"""
        return self._http_client.post(f"landing-pages/{page_id}/delete")

    def duplicate(self, page_id: int) -> Dict[str, Any]:
        """Duplicate landing page"""
        return self._http_client.post(f"landing-pages/{page_id}/duplicate")

    def publish(self, page_id: int) -> Dict[str, Any]:
        """Publish landing page"""
        return self._http_client.post(f"landing-pages/{page_id}/publish")

    def unpublish(self, page_id: int) -> Dict[str, Any]:
        """Unpublish landing page"""
        return self._http_client.post(f"landing-pages/{page_id}/unpublish")

    def analytics(self, page_id: int) -> Dict[str, Any]:
        """Get landing page analytics"""
        return self._http_client.get(f"landing-pages/{page_id}/analytics")

    def templates(self) -> Dict[str, Any]:
        """Get templates"""
        return self._http_client.get("landing-pages/templates")


class Workflows(ResourceClient):
    """Workflows resource client"""

    def list(self) -> Dict[str, Any]:
        """List all workflows"""
        return self._http_client.get("workflows")

    def get(self, workflow_id: int) -> Dict[str, Any]:
        """Get single workflow"""
        return self._http_client.get(f"workflows/{workflow_id}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create workflow"""
        return self._http_client.post("workflows", data)

    def update(self, workflow_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update workflow"""
        return self._http_client.post(f"workflows/{workflow_id}", data)

    def delete(self, workflow_id: int) -> Dict[str, Any]:
        """Delete workflow"""
        return self._http_client.post(f"workflows/{workflow_id}/delete")

    def duplicate(self, workflow_id: int) -> Dict[str, Any]:
        """Duplicate workflow"""
        return self._http_client.post(f"workflows/{workflow_id}/duplicate")

    def activate(self, workflow_id: int) -> Dict[str, Any]:
        """Activate workflow"""
        return self._http_client.post(f"workflows/{workflow_id}/activate")

    def pause(self, workflow_id: int) -> Dict[str, Any]:
        """Pause workflow"""
        return self._http_client.post(f"workflows/{workflow_id}/pause")

    def validate(self, workflow_id: int) -> Dict[str, Any]:
        """Validate workflow"""
        return self._http_client.post(f"workflows/{workflow_id}/validate")

    def executions(self, workflow_id: int) -> Dict[str, Any]:
        """Get workflow executions"""
        return self._http_client.get(f"workflows/{workflow_id}/executions")

    def templates(self) -> Dict[str, Any]:
        """Get workflow templates"""
        return self._http_client.get("workflows/templates")

    def from_template(self, template_id: int) -> Dict[str, Any]:
        """Create workflow from template"""
        return self._http_client.post("workflows/from-template", {"template_id": template_id})

    def node_types(self) -> Dict[str, Any]:
        """Get available node types"""
        return self._http_client.get("workflows/node-types")

    def get_data(self, workflow_id: int) -> Dict[str, Any]:
        """Get workflow data"""
        return self._http_client.get(f"workflows/{workflow_id}/data")


class Webhooks(ResourceClient):
    """Webhooks resource client"""

    def list(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """List all webhooks"""
        return self._http_client.get("webhooks", params or {})

    def get(self, webhook_id: int) -> Dict[str, Any]:
        """Get single webhook"""
        return self._http_client.get(f"webhooks/{webhook_id}")

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create webhook"""
        return self._http_client.post("webhooks", data)

    def update(self, webhook_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update webhook"""
        return self._http_client.post(f"webhooks/{webhook_id}", data)

    def delete(self, webhook_id: int) -> Dict[str, Any]:
        """Delete webhook"""
        return self._http_client.delete(f"webhooks/{webhook_id}")

    def test(self, webhook_id: int) -> Dict[str, Any]:
        """Test webhook"""
        return self._http_client.post(f"webhooks/{webhook_id}/test")

    def logs(self, webhook_id: int) -> Dict[str, Any]:
        """Get webhook logs"""
        return self._http_client.get(f"webhooks/{webhook_id}/logs")

    def events(self) -> Dict[str, Any]:
        """Get supported webhook events"""
        return self._http_client.get("webhooks/events")

    def regenerate_secret(self, webhook_id: int) -> Dict[str, Any]:
        """Regenerate webhook secret"""
        return self._http_client.post(f"webhooks/{webhook_id}/secret/regenerate")


__all__ = [
    "Campaigns",
    "Subscribers",
    "Lists",
    "Segments",
    "Templates",
    "Forms",
    "Conversions",
    "LandingPages",
    "Workflows",
    "Webhooks",
]
