import configurator
import typing

class StaticConfig(configurator.BaseConfig):
    """
    A simple static dictionary for configuration you must manage yourself.
    """

    def refresh(self):
        raise NotImplementedError("You cannot refresh a static config")

    def set_source(self, source: str):
        raise NotImplementedError("Static configs have no source")

    def __init__(
        self, name: str, mapping: dict[str, typing.Any] = None, register: bool = True
    ):
        super().__init__(name=name, source="", register=register)
        if mapping:
            self.mapping = mapping
        else:
            self.mapping = {}

    def set(self, key, value):
        """
        Set a static config value
        """
        self.mapping[key] = value
