import tomllib

with open("config.toml", "rb") as f:
	data = tomllib.load(f)

def get(plugin, path):
	"""
	获取配置文件数据
	
	:param plugin: 插件名称
	:param path: 配置项名称
	"""
	if plugin == "main":
		return ""
	return data[plugin][path]
