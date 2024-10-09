# Bento Python SDK
<img align="right" src="https://app.bentonow.com/brand/logoanim.gif">

> [!TIP]
> Need help? Join our [Discord](https://discord.gg/ssXXFRmt5F) or email jesse@bentonow.com for personalized support.

The Bento Python SDK makes it quick and easy to build excellent email marketing and automation experiences in your Python applications. We provide powerful and customizable APIs that can be used out-of-the-box to manage subscribers, create custom fields and tags, send broadcasts, and more. We also expose low-level APIs so that you can build fully custom experiences.

Get started with our [📚 integration guides](https://docs.bentonow.com), or [📘 browse the SDK reference](https://docs.bentonow.com/subscribers).

Table of contents
=================

<!--ts-->
* [Features](#features)
* [Requirements](#requirements)
* [Getting started](#getting-started)
    * [Installation](#installation)
    * [Configuration](#configuration)
* [Modules](#modules)
* [Things to Know](#things-to-know)
* [Contributing](#contributing)
* [License](#license)
<!--te-->

## Features

* **Subscriber management**: Easily add, update, and retrieve subscriber information.
* **Custom fields and tags**: Create and manage custom fields and tags for advanced segmentation.
* **Batch operations**: Perform bulk imports of subscribers, events, and emails.
* **Broadcast management**: Create and retrieve broadcast information.
* **Advanced analytics**: Access site and segment statistics.
* **Experimental features**: Utilize cutting-edge features like email validation, content moderation, and geolocation.

## Requirements

The Bento Python SDK requires Python 3.x and the Requests library.
Bento Account for a valid **SITE_UUID**, **BENTO_PUBLISHABLE_KEY** & **BENTO_SECRET_KEY**.

## Getting started

### Installation

Install the Bento SDK using pip:

```bash
pip install git+https://github.com/bentonow/bento-python-sdk.git
```

### Configuration

Initialize the Bento client:

```python
from bento_api import BentoAPI
import os

bento = BentoAPI(
    site_uuid=os.getenv('BENTO_SITE_UUID'),
    username=os.getenv('BENTO_PUBLISHABLE_KEY'),
    password=os.getenv('BENTO_SECRET_KEY')
)
```

## Modules

### Subscribers

Manage subscribers in your Bento account.

#### Get Subscriber

```python
subscriber = bento.get_subscriber(email="user@example.com")
print(f"Subscriber: {subscriber}")
```

#### Create Subscriber

```python
new_subscriber = bento.create_subscriber(email="newuser@example.com")
print(f"New subscriber: {new_subscriber}")
```

### Batch Operations

Perform bulk operations efficiently.

#### Batch Create Subscribers

```python
subscribers = [
    {"email": "user1@example.com", "first_name": "User", "last_name": "One"},
    {"email": "user2@example.com", "first_name": "User", "last_name": "Two"}
]
result = bento.batch_create_subscribers(subscribers)
print(f"Batch create subscribers result: {result}")
```

### Broadcasts

Manage email broadcasts.

#### Get Broadcasts

```python
broadcasts = bento.get_broadcasts()
print(f"Broadcasts: {broadcasts}")
```

### Fields

Manage custom fields.

#### Create Field

```python
new_field = bento.create_field(key="favorite_color")
print(f"New field: {new_field}")
```

### Tags

Manage tags for subscriber segmentation.

#### Create Tag

```python
new_tag = bento.create_tag(name="new_customer")
print(f"New tag: {new_tag}")
```

### Commands

Execute various commands on subscribers.

#### Execute Commands

```python
commands = [
    {"command": "add_tag", "email": "user@example.com", "query": "new_tag"},
    {"command": "remove_tag", "email": "user@example.com", "query": "old_tag"}
]
result = bento.execute_commands(commands)
print(f"Execute commands result: {result}")
```

### Stats

Retrieve analytics data.

#### Get Site Stats

```python
site_stats = bento.get_site_stats()
print(f"Site stats: {site_stats}")
```

### Experimental Features

Access cutting-edge features.

#### Validate Email

```python
validation_result = bento.validate_email(
    email="user@example.com",
    name="John Doe",
    user_agent="Mozilla/5.0",
    ip="192.168.1.1"
)
print(f"Email validation result: {validation_result}")
```

## Things to Know

1. The SDK uses environment variables for authentication. Ensure these are set securely.
2. Batch operations allow for efficient handling of multiple subscribers or events.
3. Experimental features provide advanced capabilities but may be subject to changes.
4. The SDK supports both email and UUID-based subscriber lookups.
5. Always handle potential exceptions when making API calls.

## Contributing

We welcome contributions! Please see our [contributing guidelines](CODE_OF_CONDUCT.md) for details on how to submit pull requests, report issues, and suggest improvements.

## License

The Bento SDK for Python is available as open source under the terms of the [MIT License](LICENSE.md).
