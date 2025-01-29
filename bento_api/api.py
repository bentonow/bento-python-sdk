import requests
from typing import List, Dict, Optional
from .exceptions import BentoAPIError

BASE_URL = 'https://app.bentonow.com/api/v1'

class BentoAPI:
    def __init__(self, site_uuid: str, username: str, password: str):
        self.site_uuid = site_uuid
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': f'bento-python-{site_uuid}'
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
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
    def get_subscriber(self, email: str = None, uuid: str = None) -> Dict:
        params = {}
        if email:
            params['email'] = email
        if uuid:
            params['uuid'] = uuid
        response = self._request('GET', '/fetch/subscribers', params=params)
        return response['data']['attributes']

    def create_subscriber(self, email: str) -> Dict:
        response = self._request('POST', '/fetch/subscribers', json={'subscriber': {'email': email}})
        return response['data']['attributes']

    # Batch operations
    def batch_create_subscribers(self, subscribers: List[Dict]) -> Dict:
        return self._request('POST', '/batch/subscribers', json={'subscribers': subscribers})

    def batch_create_emails(self, emails: List[Dict]) -> Dict:
        return self._request('POST', '/batch/emails', json={'emails': emails})

    def batch_create_events(self, events: List[Dict]) -> Dict:
        return self._request('POST', '/batch/events', json={'events': events})

    def batch_create_broadcasts(self, broadcasts: List[Dict]) -> Dict:
        return self._request('POST', '/batch/broadcasts', json={'broadcasts': broadcasts})

    # Broadcasts
    def get_broadcasts(self) -> List[Dict]:
        response = self._request('GET', '/fetch/broadcasts')
        return [broadcast['attributes'] for broadcast in response['data']]

    # Fields
    def get_fields(self) -> List[Dict]:
        response = self._request('GET', '/fetch/fields')
        return [field['attributes'] for field in response['data']]

    def create_field(self, key: str) -> Dict:
        response = self._request('POST', '/fetch/fields', json={'field': {'key': key}})
        return response['data']['attributes']

    # Tags
    def get_tags(self) -> List[Dict]:
        response = self._request('GET', '/fetch/tags')
        return [tag['attributes'] for tag in response['data']]

    def create_tag(self, name: str) -> Dict:
        response = self._request('POST', '/fetch/tags', json={'tag': {'name': name}})
        return response['data']['attributes']

    # Commands
    def execute_commands(self, commands: List[Dict]) -> Dict:
        return self._request('POST', '/fetch/commands', json={'command': commands})

    # Stats
    def get_site_stats(self) -> Dict:
        return self._request('GET', '/stats/site')

    def get_segment_stats(self, segment_id: str) -> Dict:
        return self._request('GET', '/stats/segment', params={'segment_id': segment_id})

    # Experimental
    def check_blacklist(self, domain: str = None, ip: str = None) -> Dict:
        params = {}
        if domain:
            params['domain'] = domain
        if ip:
            params['ip'] = ip
        return self._request('GET', '/experimental/blacklist.json', params=params)

    def validate_email(self, email: str, name: str = None, user_agent: str = None, ip: str = None) -> Dict:
        params = {'email': email}
        if name:
            params['name'] = name
        if user_agent:
            params['user_agent'] = user_agent
        if ip:
            params['ip'] = ip
        return self._request('POST', '/experimental/validation', params=params)

    def moderate_content(self, content: str) -> Dict:
        return self._request('POST', '/experimental/content_moderation', params={'content': content})

    def guess_gender(self, name: str) -> Dict:
        return self._request('POST', '/experimental/gender', params={'name': name})

    def geolocate_ip(self, ip: str) -> Dict:
        return self._request('GET', '/experimental/geolocation', params={'ip': ip})
