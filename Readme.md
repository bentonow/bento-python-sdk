
# Bento SDK for Python

🍱 Simple, powerful email marketing and automation for python projects!

Import Subscribers, Update user data, create custom fields, tags and send broadcasts in python. Data is stored in your Bento account so you can easily research and investigate what's going on. Use this python package to integrate Bento into your app!

👋 To get personalized support, please tweet @bento or email jesse@bentonow.com!

🤝 Contributions welcome and rewarded! Add a PR request for a surprise!

## Installation

**Important note:** Requests is currently a dependency of this sdk, and the minimum python version required is **3**.

```
pip install git+https://github.com/bentonow/bento-python-sdk.git
```
## Configuration

Configure the SDK in an initializer:

```python
bento = BentoAPI(
    site_uuid=os.getenv('BENTO_SITE_UUID'),
    username=os.getenv('BENTO_PUBLISHABLE_KEY'),
    password=os.getenv('BENTO_SECRET_KEY')
)
```

## Typical Usage

```python
# Get subscriber by email
subscriber = bento.get_subscriber(email="example@example.com")
print(f"Subscriber email: {subscriber['email']}")

# List all tags
tags = bento.get_tags()
print(f"tags: {tags}")

# Create a new tag
new_tag = bento.create_tag(name="new_customer")
print(f"New tag: {new_tag['name']}")

# Use an experimental feature
gender_guess = bento.guess_gender(name="Alex Smith")
print(f"Gender guess: {gender_guess}")

```

## Available Methods

This Python SDK does not contain _all_ available API methods. Please refer to the [Bento API docs](https://docs.bentonow.com/) for all available methods. This remains an opinionated thin SDK based on the top use cases we've found at Bento for apps.

### # Bento API SDK Usage Examples

This document provides examples for each method available in the Bento API SDK. Make sure you have installed the SDK and have your credentials ready before trying these examples.

### Setup

First, import the SDK and initialize the client:

```python
from bento_api import BentoAPI
import os

api = BentoAPI(
    site_uuid=os.getenv('BENTO_SITE_UUID'),
    username=os.getenv('BENTO_USERNAME'),
    password=os.getenv('BENTO_PASSWORD')
)
```

### Subscribers

#### Get Subscriber

```python
# Get subscriber by email
subscriber = api.get_subscriber(email="example@example.com")
print(f"Subscriber: {subscriber}")

# Get subscriber by UUID
subscriber = api.get_subscriber(uuid="12345678-1234-5678-1234-567812345678")
print(f"Subscriber: {subscriber}")
```

#### Create Subscriber

```python
new_subscriber = api.create_subscriber(email="newuser@example.com")
print(f"New subscriber: {new_subscriber}")
```

### Batch Operations

#### Batch Create Subscribers

```python
subscribers = [
    {"email": "user1@example.com", "first_name": "User", "last_name": "One"},
    {"email": "user2@example.com", "first_name": "User", "last_name": "Two"}
]
result = api.batch_create_subscribers(subscribers)
print(f"Batch create subscribers result: {result}")
```

#### Batch Create Emails

```python
emails = [
    {
        "to": "recipient1@example.com",
        "from": "sender@example.com",
        "subject": "Test Email 1",
        "html_body": "<h1>Hello, Recipient 1!</h1>"
    },
    {
        "to": "recipient2@example.com",
        "from": "sender@example.com",
        "subject": "Test Email 2",
        "html_body": "<h1>Hello, Recipient 2!</h1>"
    }
]
result = api.batch_create_emails(emails)
print(f"Batch create emails result: {result}")
```

####  Batch Create Events

```python
events = [
    {
        "type": "purchase",
        "email": "user1@example.com",
        "fields": {"amount": 100},
        "details": {"product": "Widget"}
    },
    {
        "type": "login",
        "email": "user2@example.com",
        "fields": {},
        "details": {"ip_address": "192.168.1.1"}
    }
]
result = api.batch_create_events(events)
print(f"Batch create events result: {result}")
```

#### Batch Create Broadcasts

```python
broadcasts = [
    {
        "name": "Newsletter 1",
        "subject": "Check out our latest news!",
        "content": "<h1>Newsletter 1 Content</h1>",
        "type": "plain"
    },
    {
        "name": "Newsletter 2",
        "subject": "More exciting updates!",
        "content": "<h1>Newsletter 2 Content</h1>",
        "type": "raw"
    }
]
result = api.batch_create_broadcasts(broadcasts)
print(f"Batch create broadcasts result: {result}")
```

### Broadcasts

#### Get Broadcasts

```python
broadcasts = api.get_broadcasts()
print(f"Broadcasts: {broadcasts}")
```

### Fields

#### Get Fields

```python
fields = api.get_fields()
print(f"Fields: {fields}")
```

#### Create Field

```python
new_field = api.create_field(key="favorite_color")
print(f"New field: {new_field}")
```

### Tags

#### Get Tags

```python
tags = api.get_tags()
print(f"Tags: {tags}")
```

#### Create Tag

```python
new_tag = api.create_tag(name="new_customer")
print(f"New tag: {new_tag}")
```

### Commands

#### Execute Commands

```python
commands = [
    {"command": "add_tag", "email": "user@example.com", "query": "new_tag"},
    {"command": "remove_tag", "email": "user@example.com", "query": "old_tag"}
]
result = api.execute_commands(commands)
print(f"Execute commands result: {result}")
```

### Stats

#### Get Site Stats

```python
site_stats = api.get_site_stats()
print(f"Site stats: {site_stats}")
```

#### Get Segment Stats

```python
segment_stats = api.get_segment_stats(segment_id="12345")
print(f"Segment stats: {segment_stats}")
```

### Experimental Features

#### Check Blacklist

```python
# Check domain
blacklist_check = api.check_blacklist(domain="example.com")
print(f"Domain blacklist check: {blacklist_check}")

# Check IP
blacklist_check = api.check_blacklist(ip="192.168.1.1")
print(f"IP blacklist check: {blacklist_check}")
```

#### Validate Email

```python
validation_result = api.validate_email(
    email="user@example.com",
    name="John Doe",
    user_agent="Mozilla/5.0",
    ip="192.168.1.1"
)
print(f"Email validation result: {validation_result}")
```

#### Moderate Content

```python
moderation_result = api.moderate_content(content="This is a test message.")
print(f"Content moderation result: {moderation_result}")
```

#### Guess Gender

```python
gender_guess = api.guess_gender(name="Alex Smith")
print(f"Gender guess: {gender_guess}")
```

#### Geolocate IP

```python
geolocation = api.geolocate_ip(ip="8.8.8.8")
print(f"Geolocation result: {geolocation}")
```

These examples demonstrate how to use each method in the Bento API SDK. Remember to handle potential exceptions and errors in your production code, and always refer to the official Bento API documentation for the most up-to-date information on request and response formats.

## Contributing

Bug reports and pull requests are welcome on GitHub at [bentonow/bento-python-sdk](https://github.com/bentonow/bento-python-sdk). This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).