import json
import requests

def on_command(info: dict):
    card_info = json.loads(str(info["message"][0]["data"]["data"]))
    if card_info["meta"]["detail_1"]["title"] == "哔哩哔哩":
        resp = requests.get(card_info["meta"]["detail_1"]["qqdocurl"])
        message = f"""检测到Bilibili分享卡片！
视频标题：{card_info["meta"]["detail_1"]["desc"]}
视频链接：{str(resp.url)}
分享人：{card_info["meta"]["detail_1"]["host"]["uin"]}"""
        return {"reply": message}