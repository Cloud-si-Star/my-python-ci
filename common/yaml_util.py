import yaml

# 定义yaml文件读取方法
def read_yaml(path):
    with open(path,"r",encoding="utf-8") as f:
        return yaml.safe_load(f)


# 读取yaml配置
def get_config():
    return read_yaml("../config/config.yaml")

# 获取env配置
def get_env_config():
    cfg=get_config()
    env=cfg["env"]
    return cfg[env]