def on_command(message_type: str,info: dict):
    """
    处理接收到的命令
    
    :param message_type: 消息类型
    :type message_type: str
    :param info: 信息
    :type info: dict
    """
    sub_command = info["raw_message"].replace("/github ","")
    if sub_command.startswith("add"):

        return {
            "reply":"已绑定仓库"+sub_command.replace("add ", "")+"到 "+info["group_name"]+" 群号"+str(info["group_id"])
            }
    