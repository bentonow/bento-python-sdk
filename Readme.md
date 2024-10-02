# Bento API Python SDK

This package provides a Python SDK for interacting with the Bento API. It uses the `requests` library for HTTP requests.

## Installation

You can install the Bento API SDK using pip:

```
pip install bento-api
```

## Usage

Here's a quick example of how to use the Bento API SDK:

```python
from bento_api import BentoAPI
import os

api = BentoAPI(
    site_uuid=os.getenv('BENTO_SITE_UUID'),
    username=os.getenv('BENTO_USERNAME'),
    password=os.getenv('BENTO_PASSWORD')
)

# Get subscriber information
subscriber = api.get_subscriber(email="example@example.com")
print(f"Subscriber email: {subscriber['email']}")

# Create a new tag
new_tag = api.create_tag(name="new_customer")
print(f"New tag: {new_tag['name']}")

# Use an experimental feature
gender_guess = api.guess_gender(name="Alex Smith")
print(f"Gender guess: {gender_guess}")
```

For more detailed usage instructions and API documentation, please refer to the [official Bento API documentation](https://docs.bentonow.com/).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.