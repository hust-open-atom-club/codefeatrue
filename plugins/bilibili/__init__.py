"""BiliBili解析插件"""

from urllib.parse import urlparse
import json
import requests

def on_command(message_type: str,info: dict):
    """
    处理接收到的命令

    :param message_type: 消息类型
    :type message_type: str
    :param info: 信息
    :type info: dict
    """
    if message_type == "json":
        card_info = json.loads(str(info["message"][0]["data"]["data"]))
        if card_info["meta"]["detail_1"]["title"] == "哔哩哔哩":
            resp = requests.get(card_info["meta"]["detail_1"]["qqdocurl"], timeout=15)
            parsed_url = urlparse(str(resp.url))
            bv = parsed_url.path
            bv = bv.replace("/", "")
            bv = bv.replace("video", "")
            url = parsed_url.netloc + parsed_url.path
            message = f"""检测到Bilibili分享卡片！
    视频标题：{card_info["meta"]["detail_1"]["desc"]}
    BV号：{str(bv)}
    视频链接：{str(url)}
    分享人：{card_info["meta"]["detail_1"]["host"]["uin"]}"""
            return {"reply": message}
    else:
        return {}
