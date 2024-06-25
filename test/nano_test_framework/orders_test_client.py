from json import dumps

from httpx import get, post, delete, Response
from assertpy import assert_that

from test.config import SERVICE_BASE_URL


class OrdersTestClient:
    """
    Test client provides wrappers for required CRUD ops.
    Abstracts repetitive boilerplate code form tests.
    """
    def __init__(self):
        self.service_base_url = SERVICE_BASE_URL

    @staticmethod
    def _verify_status_and_detail(response: Response, status_code: int, detail: str):
        # Verify expected status code
        assert_that(response).has_status_code(status_code)

        # Verify detail, ONLY FOR FAILED CALLS
        if detail:
            assert_that(response.json()).has_detail(detail)

    def get(self, path: str, status_code: int = 200, detail: str = None) -> dict:
        # Do call
        get_resp = get(self.service_base_url + path)

        # Verify expected status code & detail
        self._verify_status_and_detail(get_resp, status_code, detail)

        # Extract response body
        return get_resp.json()

    def post(self, path: str, body, status_code: int = 201, detail: str = None) -> dict:
        # Do call
        post_resp = post(self.service_base_url + path, data=dumps(body))

        # Verify expected status code & detail
        self._verify_status_and_detail(post_resp, status_code, detail)

        # Extract response body
        return post_resp.json()

    def delete(self, path: str, status_code: int = 204, detail: str = None) -> None:
        # Do call
        delete_resp = delete(self.service_base_url + path)

        # Verify expected status code & detail
        self._verify_status_and_detail(delete_resp, status_code, detail)
