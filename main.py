"""程序总入口"""

from contextlib import asynccontextmanager
import importlib
from fastapi import FastAPI
from plugins import github, oseddl, bilibili
import tomllib

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("CodeFeatrue-破晓之码 正在启动")
    with open("config.toml", "rb") as f:
        _config_data = tomllib.load(f)
    for plugin_name in _config_data["main"]["plugins"]:
        # 初始化插件
        plugin = importlib.import_module(plugin_name)
        try:
            plugin.on_enable(app)
        except AttributeError:
            pass
        except Exception as e:
            print(f"插件 {plugin_name} 启动失败: {e}")
        pass
    yield
    print("CodeFeatrue-破晓之码 正在退出")

@app.post("/")
def main(info: dict):
    """
    处理接收到的消息
    
    :param info: Onebot实现端传入的信息
    :type info: dict
    """
    if info["post_type"]=="message":
        message_type = info["message"][0]["type"]
        # 私聊/群 均传递
        if info["raw_message"].startswith("/oseddl"):
            return oseddl.on_command(message_type, info)
        if info["message_type"] == "group":
        # 仅群
            if info["raw_message"].startswith("/github"):
                return github.on_command(message_type, info)
            if info["message"][0]["type"] == "json":
                # Type == card
                return  bilibili.on_command(message_type, info)
    return {}
