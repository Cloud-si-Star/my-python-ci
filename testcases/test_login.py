import pytest
from common.assert_util import assert_status_code
from common.yaml_util import read_yaml

login_data = read_yaml("data/login_data.yaml")

@pytest.mark.parametrize("case",login_data,ids=[c["case_name"] for c in login_data])
def test_login(api,case):
    resp=api.post("/posts",json={
        "username":case["username"],
        "password":case["password"]
    })
    assert_status_code(resp,case["expected_status"])


