import pytest
from common.assert_util import assert_status_code,assert_key_exists,assert_json_value,assert_http_code,assert_value_is_expected,assert_value_is_exits
from common.yaml_util import read_yaml

def test_get_user(api,login_token):
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

@pytest.mark.alone
def test_alone_get(api,login_token):
    resp=api.get("/users/1")
    assert_http_code(resp,200)
    assert_value_is_expected(resp,"name","Leanne Graham")
    assert_value_is_exits(resp,"email","@")


# 取数数据
post_data=read_yaml("data/param_data.yaml").get("post_case")
@pytest.mark.alone
@pytest.mark.parametrize(
    "case",
post_data,
    ids=[]
)
def test_alone_post(api,login_token,case):

    resp=api.post("/posts",json={
        "title":"pytest artical",
        "body":"This is pytest partical",
        "userId":10
    })
    print(resp.status_code)
    assert_http_code(resp,case["code"])
    assert_key_exists(resp,case["key_exits"])
    assert_value_is_expected(resp,"userId",case["userId"])
    assert_value_is_exits(resp,"title",case["text_exits"])