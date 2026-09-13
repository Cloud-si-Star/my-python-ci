import pytest
from common.assert_util import assert_status_code,assert_key_exists,assert_json_value

def test_get_user(api,login):
    resp=api.get("/posts/1")
    assert_status_code(resp,200)
    assert_key_exists(resp,"id")
    assert_json_value(resp,"id",1)


def test_create_post(api,login_token):
    resp=api.post("/posts",json={
        "title":"foo",
        "body":"bar",
        "userId":1
    })
    assert_status_code(resp,200)
    assert_key_exists(resp,"id")