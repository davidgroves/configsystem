from configurator import ConfigRegistry as ConfigRegistry
from config_types import JsonConfig

json_config = JsonConfig(name="basic_json_config", register=True, source="files/example.json")

assert ConfigRegistry.get_item("basic_json_config", "Sky") == "Blue"
