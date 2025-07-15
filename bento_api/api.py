import requests
from typing import List, Dict, Optional, Any, TypedDict
from .exceptions import BentoAPIError

BASE_URL = 'https://app.bentonow.com/api/v1'


class BentoAPI:
    def __init__(self, site_uuid: str, username: str, password: str):
        """
        Initialize the BentoAPI client.

        Args:
            site_uuid: The UUID of the Bento site.
            username: The username for authentication.
            password: The password for authentication.
        """
        self.site_uuid = site_uuid
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': f'bento-python-{site_uuid}'
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        Internal method to send an HTTP request to the Bento API.

        Args:
            method: HTTP method (GET, POST, etc.).
            endpoint: API endpoint path.
            **kwargs: Additional arguments for requests.Session.request.

        Returns:
            Dict[str, Any]: Parsed JSON response from the API.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        url = f"{BASE_URL}{endpoint}"
        params = kwargs.get('params', {})
        params['site_uuid'] = self.site_uuid
        kwargs['params'] = params

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise BentoAPIError(f"API request failed: {str(e)}")

    # Subscribers
    def get_subscriber(self, email: Optional[str] = None, uuid: Optional[str] = None) -> SubscriberAttributes:
        """
        Retrieve a subscriber by email or UUID.

        Args:
            email (Optional[str]): The subscriber's email address.
            uuid (Optional[str]): The subscriber's UUID.
                At least one of `email` or `uuid` must be provided.

        Returns:
            SubscriberAttributes: Subscriber attributes.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        params = {}
        if email:
            params['email'] = email
        if uuid:
            params['uuid'] = uuid
        response = self._request('GET', '/fetch/subscribers', params=params)
        return response['data']['attributes']

    def create_subscriber(self, email: str) -> SubscriberAttributes:
        """
        Create a new subscriber with the given email address.

        Args:
            email: The subscriber's email address.

        Returns:
            SubscriberAttributes: Created subscriber attributes.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        response = self._request('POST', '/fetch/subscribers', json={'subscriber': {'email': email}})
        return response['data']['attributes']

    # Batch operations
    def batch_create_subscribers(self, subscribers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create multiple subscribers in a single batch request.

        Args:
            subscribers: List of subscriber data dictionaries.

        Returns:
            Dict[str, Any]: API response from the server, which may include success/failure info for each item.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        return self._request('POST', '/batch/subscribers', json={'subscribers': subscribers})

    def batch_create_emails(self, emails: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create multiple emails in a single batch request.

        Args:
            emails: List of email data dictionaries.

        Returns:
            Dict[str, Any]: API response from the server, which may include success/failure info for each item.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        return self._request('POST', '/batch/emails', json={'emails': emails})

    def batch_create_events(self, events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create multiple events in a single batch request.

        Args:
            events: List of event data dictionaries.

        Returns:
            Dict[str, Any]: API response from the server, which may include success/failure info for each item.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        return self._request('POST', '/batch/events', json={'events': events})

    def batch_create_broadcasts(self, broadcasts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create multiple broadcasts in a single batch request.

        Args:
            broadcasts: List of broadcast data dictionaries.

        Returns:
            Dict[str, Any]: API response from the server, which may include success/failure info for each item.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        return self._request('POST', '/batch/broadcasts', json={'broadcasts': broadcasts})

    # Broadcasts
    def get_broadcasts(self) -> List[BroadcastAttributes]:
        """
        Retrieve all broadcasts for the site.

        Returns:
            List[BroadcastAttributes]: List of broadcast attribute dictionaries.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        response = self._request('GET', '/fetch/broadcasts')
        return [broadcast['attributes'] for broadcast in response['data']]

    # Fields
    def get_fields(self) -> List[FieldAttributes]:
        """
        Retrieve all custom fields for the site.

        Returns:
            List[FieldAttributes]: List of field attribute dictionaries.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        response = self._request('GET', '/fetch/fields')
        return [field['attributes'] for field in response['data']]

    def create_field(self, key: str) -> FieldAttributes:
        """
        Create a new custom field.

        Args:
            key: The key/name of the field.

        Returns:
            FieldAttributes: Created field attributes.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        response = self._request('POST', '/fetch/fields', json={'field': {'key': key}})
        return response['data']['attributes']

    # Tags
    def get_tags(self) -> List[TagAttributes]:
        """
        Retrieve all tags for the site.

        Returns:
            List[TagAttributes]: List of tag attribute dictionaries.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        response = self._request('GET', '/fetch/tags')
        return [tag['attributes'] for tag in response['data']]

    def create_tag(self, name: str) -> TagAttributes:
        """
        Create a new tag.

        Args:
            name: The name of the tag.

        Returns:
            TagAttributes: Created tag attributes.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        response = self._request('POST', '/fetch/tags', json={'tag': {'name': name}})
        return response['data']['attributes']

    # Commands
    def execute_commands(self, commands: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Execute a list of commands on the site.

        Args:
            commands: List of command dictionaries.

        Returns:
            Dict[str, Any]: API response.

        Raises:
            BentoAPIError: If the request fails or returns an error.

        Note:
            The payload uses the key 'commands' (plural) to send the list of commands.
        """
        return self._request('POST', '/fetch/commands', json={'commands': commands})

    # Stats
    def get_site_stats(self) -> Dict[str, Any]:
        """
        Retrieve statistics for the site.

        Returns:
            Dict[str, Any]: Site statistics.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        return self._request('GET', '/stats/site')

    def get_segment_stats(self, segment_id: str) -> Dict[str, Any]:
        """
        Retrieve statistics for a specific segment.

        Args:
            segment_id: The ID of the segment.

        Returns:
            Dict[str, Any]: Segment statistics.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        return self._request('GET', '/stats/segment', params={'segment_id': segment_id})

    # Experimental
    def check_blacklist(self, domain: Optional[str] = None, ip: Optional[str] = None) -> Dict[str, Any]:
        """
        Check if a domain or IP address is blacklisted.

        Args:
            domain: The domain to check.
            ip: The IP address to check.

        Returns:
            Dict[str, Any]: Blacklist check result.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        params = {}
        if domain:
            params['domain'] = domain
        if ip:
            params['ip'] = ip
        return self._request('GET', '/experimental/blacklist.json', params=params)

    def validate_email(self, email: str, name: Optional[str] = None, user_agent: Optional[str] = None, ip: Optional[str] = None) -> Dict[str, Any]:
        """
        Validate an email address with optional additional context.

        Args:
            email: The email address to validate.
            name: The name associated with the email.
            user_agent: The user agent string.
            ip: The IP address.

        Returns:
            Dict[str, Any]: Email validation result.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        params = {'email': email}
        if name:
            params['name'] = name
        if user_agent:
            params['user_agent'] = user_agent
        if ip:
            params['ip'] = ip
        return self._request('POST', '/experimental/validation', params=params)

    def moderate_content(self, content: str) -> Dict[str, Any]:
        """
        Moderate a piece of content for policy violations.

        Args:
            content: The content to moderate.

        Returns:
            Dict[str, Any]: Content moderation result.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        return self._request('POST', '/experimental/content_moderation', params={'content': content})

    def guess_gender(self, name: str) -> Dict[str, Any]:
        """
        Guess the gender based on a given name.

        Args:
            name: The name to analyze.

        Returns:
            Dict[str, Any]: Gender guess result.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        return self._request('POST', '/experimental/gender', params={'name': name})

    def geolocate_ip(self, ip: str) -> Dict[str, Any]:
        """
        Geolocate an IP address.

        Args:
            ip: The IP address to geolocate.

        Returns:
            Dict[str, Any]: Geolocation result.

        Raises:
            BentoAPIError: If the request fails or returns an error.
        """
        return self._request('GET', '/experimental/geolocation', params={'ip': ip})
