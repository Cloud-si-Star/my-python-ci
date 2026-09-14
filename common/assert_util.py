# 断言封装
def assert_status_code(resp,expected):
    assert resp.status_code==expected,f"状态码错误：期望：{expected}，实际：{resp.status_code}"

def assert_json_value(resp,key,expected):
    actual=resp.json().get(key)
    assert actual==expected,f"字段{key}错误，期望{expected}，实际{actual}"


def assert_key_exists(resp,key):
    assert key in resp.json(),f"响应中不存在字段{key}"


# 断言封装-验证状态码
def assert_http_code(resp,expected):
    assert resp.status_code==expected,f"状态码错误，期望：{expected}|实际：{resp.status_code}"

# 断言封装-判定某个值是否相等
def assert_value_is_expected(resp,key,expected):
    acvalue=resp.json().get(key)
    assert acvalue==expected,f"对应值错误，期望：{expected}|实际：{acvalue}"

def assert_value_is_exits(resp,key,extis):
    acvalue=resp.json().get(key)
    assert extis in acvalue,f"{key}对应value值中不存在{extis}"