import pytest
from common.request_util import RequestUtil

@pytest.fixture(scope="session")
def api():
    return RequestUtil()

@pytest.fixture(scope="session")
def login_token(api):
    resp=api.post("/posts",json={"username":"admin","password":"123"})
    token = resp.json().get("id")
    assert token is not None
    return token