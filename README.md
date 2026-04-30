# KiriMel Python SDK

Official Python SDK for KiriMel Email Marketing API.

## Installation

```bash
pip install kirimel-python
```

## Quick Start

```python
import kirimel

# Initialize the client
client = kirimel.KiriMel(
    api_key='sk_test_xxx',  # Or set KIRIMEL_API_KEY env variable
    base_url='https://kirimel.com/api',
    timeout=30,
    retries=3
)

# List campaigns
campaigns = client.campaigns.list(status='sent', limit=20)

# Create a campaign
campaign = client.campaigns.create({
    'name': 'Welcome Email',
    'subject': 'Welcome to KiriMel!',
    'list_id': 123,
    'template_id': 456
})

# Get campaign statistics
stats = client.campaigns.stats(campaign['id'])
```

## Authentication

The SDK supports two authentication methods:

```python
# Method 1: API Key (recommended)
client = kirimel.KiriMel(api_key='sk_test_xxx')

# Method 2: Environment variable
# Set KIRIMEL_API_KEY=sk_test_xxx in your environment
client = kirimel.KiriMel()
```

## Resources

### Campaigns

```python
# List campaigns
campaigns = client.campaigns.list(limit=20, status='sent')

# Get recent campaigns
recent = client.campaigns.recent()

# Get single campaign
campaign = client.campaigns.get(id)

# Create campaign
campaign = client.campaigns.create({
    'name': 'Summer Sale',
    'subject': '50% Off Everything!',
    'list_id': 123,
    'template_id': 456
})

# Update campaign
client.campaigns.update(id, {'subject': 'New Subject'})

# Delete campaign
client.campaigns.delete(id)

# Duplicate campaign
duplicate = client.campaigns.duplicate(id)

# Schedule campaign
client.campaigns.schedule(id, '2024-06-01 10:00:00')

# Pause campaign
client.campaigns.pause(id)

# Resume campaign
client.campaigns.resume(id)

# Get campaign statistics
stats = client.campaigns.stats(id)
```

### Subscribers

```python
# List subscribers for a list
subscribers = client.subscribers.list(list_id, limit=50)

# List all subscribers
all_subscribers = client.subscribers.list_all(limit=50)

# Get single subscriber
subscriber = client.subscribers.get(id)

# Add subscriber
subscriber = client.subscribers.create({
    'email': 'user@example.com',
    'first_name': 'John',
    'last_name': 'Doe'
})

# Update subscriber
client.subscribers.update(id, {'first_name': 'Jane'})

# Delete subscriber
client.subscribers.delete(id)

# Unsubscribe subscriber
client.subscribers.unsubscribe(id)

# Bulk unsubscribe
client.subscribers.bulk_unsubscribe([id1, id2, id3])

# Bulk delete
client.subscribers.bulk_delete([id1, id2, id3])

# Get subscriber activity
activity = client.subscribers.activity(id)

# Get subscriber statistics
stats = client.subscribers.stats(id)

# Toggle VIP status
client.subscribers.toggle_vip(id)

# Search subscribers
results = client.subscribers.search('john@example.com')

# Add tag
client.subscribers.add_tag(id, 'premium-customer')

# Remove tag
client.subscribers.remove_tag(id, 'premium-customer')

# Import subscribers
result = client.subscribers.import_subscribers(list_id, {
    'subscribers': [
        {'email': 'user1@example.com', 'first_name': 'User 1'},
        {'email': 'user2@example.com', 'first_name': 'User 2'}
    ]
})
```

### Lists

```python
# List all lists
lists = client.lists.list()

# Get single list
lst = client.lists.get(id)

# Create list
lst = client.lists.create({
    'name': 'Newsletter Subscribers',
    'description': 'Monthly newsletter'
})

# Update list
client.lists.update(id, {'name': 'Updated Name'})

# Delete list
client.lists.delete(id)

# Get list statistics
stats = client.lists.stats(id)
```

### Segments

```python
# List segments for a list
segments = client.segments.list(list_id)

# Get single segment
segment = client.segments.get(id)

# Create segment
segment = client.segments.create(list_id, {
    'name': 'Active Subscribers',
    'conditions': [
        {'field': 'status', 'operator': 'equals', 'value': 'active'}
    ]
})

# Update segment
client.segments.update(id, {'name': 'Updated Name'})

# Delete segment
client.segments.delete(id)

# Preview segment (without saving)
preview = client.segments.preview(list_id, [
    {'field': 'status', 'operator': 'equals', 'value': 'active'}
])

# Get segment subscribers
subscribers = client.segments.subscribers(id)

# Refresh segment count
client.segments.refresh(id)

# Get segment build logs
logs = client.segments.logs(id)

# Get segment templates
templates = client.segments.templates()

# Get available fields
fields = client.segments.fields()
```

### Templates

```python
# List all templates
templates = client.templates.list(limit=20)

# Get single template
template = client.templates.get(id)

# Create template
template = client.templates.create({
    'name': 'Welcome Email',
    'subject': 'Welcome!',
    'html_content': '<h1>Hello {{name}}</h1>',
    'category': 'transactional'
})

# Update template
client.templates.update(id, {'name': 'Updated Name'})

# Delete template
client.templates.delete(id)

# Duplicate template
duplicate = client.templates.duplicate(id)

# Get templates by category
templates = client.templates.by_category('newsletter')

# Search templates
results = client.templates.search('welcome')

# Get categories
categories = client.templates.categories()
```

### Forms

```python
# List all forms
forms = client.forms.list()

# Get single form
form = client.forms.get(id)

# Create form
form = client.forms.create({
    'name': 'Newsletter Signup',
    'list_id': 123,
    'fields': [
        {'name': 'email', 'type': 'email', 'required': True},
        {'name': 'first_name', 'type': 'text', 'required': False}
    ]
})

# Update form
client.forms.update(id, {'name': 'Updated Name'})

# Delete form
client.forms.delete(id)

# Duplicate form
duplicate = client.forms.duplicate(id)

# Get form analytics
analytics = client.forms.analytics(id)

# Get form submissions
submissions = client.forms.submissions(id)

# Get embed code
embed = client.forms.embed(id)
```

### Conversions

```python
# List all conversion goals
conversions = client.conversions.list()

# Get single conversion goal
goal = client.conversions.get(id)

# Create conversion goal
goal = client.conversions.create({
    'name': 'Purchase',
    'event_type': 'purchase',
    'value': 100
})

# Update conversion goal
client.conversions.update(id, {'name': 'Updated Name'})

# Delete conversion goal
client.conversions.delete(id)

# Track a conversion
client.conversions.track({
    'goal_id': id,
    'subscriber_id': 123,
    'value': 50
})

# Get conversions for a goal
conversions = client.conversions.conversions(id)

# Get ROI report
roi = client.conversions.roi()

# Get funnel analysis
funnel = client.conversions.funnel(id)
```

### Landing Pages

```python
# List all landing pages
pages = client.landing_pages.list()

# Get single landing page
page = client.landing_pages.get(id)

# Create landing page
page = client.landing_pages.create({
    'name': 'Thank You Page',
    'slug': 'thank-you',
    'html_content': '<h1>Thank you!</h1>'
})

# Update landing page
client.landing_pages.update(id, {'name': 'Updated Name'})

# Delete landing page
client.landing_pages.delete(id)

# Duplicate landing page
duplicate = client.landing_pages.duplicate(id)

# Publish landing page
client.landing_pages.publish(id)

# Unpublish landing page
client.landing_pages.unpublish(id)

# Get landing page analytics
analytics = client.landing_pages.analytics(id)

# Get templates
templates = client.landing_pages.templates()
```

### Workflows

```python
# List all workflows
workflows = client.workflows.list()

# Get single workflow
workflow = client.workflows.get(id)

# Create workflow
workflow = client.workflows.create({
    'name': 'Welcome Series',
    'nodes': [...],
    'edges': [...]
})

# Update workflow
client.workflows.update(id, {'name': 'Updated Name'})

# Delete workflow
client.workflows.delete(id)

# Duplicate workflow
duplicate = client.workflows.duplicate(id)

# Activate workflow
client.workflows.activate(id)

# Pause workflow
client.workflows.pause(id)

# Validate workflow
validation = client.workflows.validate(id)

# Get workflow executions
executions = client.workflows.executions(id)

# Get workflow templates
templates = client.workflows.templates()

# Create workflow from template
workflow = client.workflows.from_template(template_id)

# Get available node types
node_types = client.workflows.node_types()

# Get workflow data
data = client.workflows.get_data(id)
```

### Email (Transactional)

Send transactional emails with attachment support:

```python
# Send transactional email
result = client.email.send({
    'to': 'user@example.com',
    'subject': 'Welcome to our service!',
    'html': '<h1>Welcome!</h1><p>Thanks for signing up.</p>',
    'text': 'Welcome! Thanks for signing up.',
    'from_name': 'My App',
    'reply_to': 'support@example.com',
    'cc': 'cc@example.com',
    'bcc': ['bcc1@example.com', 'bcc2@example.com'],
    'attachments': [
        {
            'name': 'invoice.pdf',
            'content': base64.b64encode(open('/path/to/invoice.pdf', 'rb').read()).decode()
        },
        {
            'name': 'report.csv',
            'content': base64.b64encode(open('/path/to/report.csv', 'rb').read()).decode()
        }
    ]
})

# Response includes message_id and tracking_id
print(f"Message ID: {result['message_id']}")
print(f"Tracking ID: {result['tracking_id']}")

# Send to multiple recipients
result = client.email.send({
    'to': ['user1@example.com', 'user2@example.com'],
    'subject': 'Team update',
    'html': '<p>Here is the latest update.</p>'
})

# Get SES send quota
quota = client.email.quota()
print(f"Remaining: {quota['remaining']}")
print(f"Max 24h: {quota['max_24_hour_send']}")
print(f"Utilization: {quota['utilization_percent']}%")

# Get verified emails
verified = client.email.verified_emails()

# Verify a new email address
result = client.email.verify_email('new@example.com')
```

## Error Handling

```python
from kirimel import (
    ApiException,
    AuthenticationException,
    RateLimitException,
    ValidationException
)

try:
    campaign = client.campaigns.create(data)
except AuthenticationException as e:
    # Invalid API key
    print(f"Authentication failed: {e.message}")
except RateLimitException as e:
    # Too many requests
    print(f"Rate limited. Retry after: {e.retry_after} seconds")
except ValidationException as e:
    # Invalid data
    print(f"Validation errors: {e.errors}")
except ApiException as e:
    # General API error
    print(f"API error ({e.status_code}): {e.message}")
```

## Logging

```python
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# The SDK will use the root logger by default
```

## Requirements

- Python 3.8 or higher
- requests >= 2.28.0

## License

MIT License

## Support

- Documentation: https://kirimel.com/api-docs
- GitHub: https://github.com/hualiglobal/kirimel-python-sdk
- Issues: https://github.com/hualiglobal/kirimel-python-sdk/issues
