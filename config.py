import tomllib

with open("config.toml", "rb") as f:
   data = tomllib.load(f)

def get(plugin, path):
   if plugin == "main":
      return ""
   return data[plugin][path]