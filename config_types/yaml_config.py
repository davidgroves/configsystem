import configurator
import yaml

class YamlConfig(configurator.BaseConfig):
    """
    Loads, and reloads, configuriaton from the
    """

    def __init__(self, name: str, source: str, register: bool = True):
        super().__init__(name=name, source=source, register=register)
        self.refresh()

    def set_source(self, source):
        if os.path.isfile(source) and os.access(source, os.R_OK):
            self.source = source
        else:
            raise ValueError(f"YAML File {source} doesn't exist or is not readable")

    def refresh(self):
        """
        Updates mappings based on this source.
        """

        with open(self.source, "r", encoding="utf8") as yamlfile:
            self.mapping = yaml.safe_load(yamlfile)
