from json import dumps

from httpx import get, post, delete, Response
from assertpy import assert_that

from test.nano_test_framework.response_util import readable_json


class OrdersTestClient:
    """
    Test client provides wrappers for required CRUD ops.
    Abstracts repetitive boilerplate code form tests.
    """
    def __init__(self):
        # todo: Move to config
        self.service_base_url = 'http://orders-api-container:80'

    @staticmethod
    def _verify_status_and_description(response: Response, status_code: int, description: str):
        # Verify expected status code
        assert_that(response).has_status_code(status_code)

        # Verify description, ONLY FOR FAILED CALLS
        if description:
            assert_that(response).has_description(description)

    def get(self, path: str, status_code: int = 200, description: str = None) -> dict:
        # Do call
        get_resp = get(self.service_base_url + path)

        # Verify expected status code & description
        self._verify_status_and_description(get_resp, status_code, description)

        # Extract response body
        return get_resp.json()

    def post(self, path: str, body, status_code: int = 201, description: str = None) -> dict:
        # Do call
        post_resp = post(self.service_base_url + path, data=dumps(body))

        # Verify expected status code & description
        self._verify_status_and_description(post_resp, status_code, description)

        # Extract response body
        return post_resp.json()

    def delete(self, path: str, status_code: int = 204, description: str = None) -> None:
        # Do call
        delete_resp = delete(self.service_base_url + path)

        # Verify expected status code & description
        self._verify_status_and_description(delete_resp, status_code, description)