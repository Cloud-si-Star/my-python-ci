import requests
from common.logger import logger
from common.yaml_util import get_env_config

class RequestUtil:
    def __init__(self):
        cfg=get_env_config()
        self.base_url=cfg["base_url"]
        self.timeout=cfg["timeout"]
        self.session=requests.Session()

    def request(self,method,path,**kwargs):
        url=self.base_url+path
        kwargs.setdefault("timeout",self.timeout)
        logger.info(f"请求{method.upper()}{url}|参数：{kwargs}")
        resp=self.session(method,url,**kwargs)
        logger.info(f"响应{resp.status_code}|{resp.text[:200]}")
        return resp

    def get(self,path,**kwargs):
        return self.request("GET",path,**kwargs)

    def post(self,path,**kwargs):
        return self.request("POST",path,**kwargs)

    def put(self,path,**kwargs):
        return self.request("PUT", path, **kwargs)

    def delete(self,path,**kwargs):
        return self.request("DELETE", path, **kwargs)