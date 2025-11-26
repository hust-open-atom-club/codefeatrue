import json
import requests
from urllib.parse import urlparse

def on_command(message_type: str,info: dict):
    card_info = json.loads(str(info["message"][0]["data"]["data"]))
    if card_info["meta"]["detail_1"]["title"] == "哔哩哔哩":
        resp = requests.get(card_info["meta"]["detail_1"]["qqdocurl"])
        parsed_url = urlparse(str(resp.url))
        bv = parsed_url.path
        bv = bv.replace("/", "")
        message = f"""检测到Bilibili分享卡片！
视频标题：{card_info["meta"]["detail_1"]["desc"]}
视频链接：{str(bv)}
分享人：{card_info["meta"]["detail_1"]["host"]["uin"]}"""
        return {"reply": message}