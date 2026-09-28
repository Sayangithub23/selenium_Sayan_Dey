import requests
from config.config import BASE_URL, HEADERS, TIMEOUT


class APIClient:
    """Reusable wrapper around Python Requests."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.token = None

    def _request(self, method, endpoint, **kwargs):
        url = f"{BASE_URL}{endpoint}"
        kwargs.setdefault("timeout", TIMEOUT)

        response = self.session.request(method, url, **kwargs)
        return response

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self._request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

    def create_token(self, username, password):
        response = self.post(
            "/auth",
            json={"username": username, "password": password},
        )

        if response.ok:
            self.token = response.json().get("token")
            if self.token:
                self.session.cookies.set("token", self.token)

        return response
