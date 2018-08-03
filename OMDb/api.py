import re
import requests

from decimal import Decimal


class OMDB(object):
    """HTTP request client for OMDb API."""
    url = 'http://www.omdbapi.com'
    params_map = {
        's': 'search',
        't': 'title',
        'i': 'imdbid',
        'y': 'year',
        'apikey': 'apikey'
    }
    json_response = None

    def __init__(self, **defaults):
        self.default_params = defaults
        self.session = requests.Session()

    def set_default(self, key, default):
        """Set default request params."""
        self.default_params[key] = default

    def request(self, **params):
        """HTTP GET request to OMDb API.
        Raises exception for non-200 HTTP status codes.
        """
        params.setdefault('apikey', self.default_params.get('apikey'))

        res = self.session.get(self.url, params=params)

        # raise HTTP status code exception if status code != 200
        res.raise_for_status()

        return res

    def get(self, search=None, title=None, imdbid=None, year=None):
        """Make OMDb API GET request and return results."""

        params = {
            'search': search,
            'title': title,
            'imdbid': imdbid,
            'year': year
        }

        # remove incorrect params
        params = dict([(key, value) for key, value in iteritems(params)
                       if value or isinstance(value, (int, float, Decimal))])

        # set defaults
        for key in self.params_map.values():
            if key in self.default_params:
                params.setdefault(key, self.default_params[key])

        # convert function args to API query params
        params = self.format_params(params)

        data = self.request(**params).json()

        self.json_response = self.format_search_results(data, params)

        return self.json_response

    def format_params(self, params):
        """Format our custom named params to OMDb API param names."""
        return {api_param: params[param]
                for api_param, param in iteritems(self.params_map)
                if param in params}

    def format_search_results(self, data, params):
        """Format OMDb API search results into standard format."""
        if 's' in params:
            return self.format_search_list(data.get('Search', []))
        else:
            return self.format_search_item(data)

    def format_search_list(self, items):
        """Format each search item using :meth:`format_search_item`."""
        return [self.format_search_item(item) for item in items]

    def format_search_item(self, item):
        """Format search item by converting dict key case from camel case to
        underscore case.
        """
        if not isinstance(item, dict):
            return item

        if 'Error' in item:
            return {}

        return {camelcase_to_underscore(key): (self.format_search_list(value)
                                               if isinstance(value, list)
                                               else value)
                for key, value in iteritems(item)}

    def get_title(self):
        if self.json_response is not None:
            return self.json_response['title']
        else:
            return None

    def get_imdbid(self):
        if self.json_response is not None:
            return self.json_response['imdb_id']
        else:
            return None

    def get_imdb_rating(self):
        if self.json_response is not None:
            return float(self.json_response['imdb_rating'])
        else:
            return None

    def get_release_year(self):
        if self.json_response is not None:
            return int(self.json_response['year'])
        else:
            return None

    def get_genre(self):
        if self.json_response is not None:
            return [item for item in self.json_response['genre'].split(",")]
        else:
            return None


def camelcase_to_underscore(string):
    """Convert string from CamelCase to underscore_case."""
    return re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))').sub(r'_\1', string).lower()


def iterkeys(d): return iter(d.keys())


def itervalues(d): return iter(d.values())


def iteritems(d): return iter(d.items())
