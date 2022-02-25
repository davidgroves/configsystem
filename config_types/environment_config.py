import configurator
import os

class EnvironmentConfig(configurator.BaseConfig):
    """
    Loads, and reloads, configuriaton from the
    """

    def __init__(self, name: str, source: str, register: bool = True):
        super().__init__(name=name, source=source, register=register)
        self.set_source(source)
        self.refresh()

    def set_source(self, source):
        """
        For Environments, the source is the prefix used for the environment variables.
        For exmaple, if you have environment variables called :-
         MYPREFIX_CODEA
         MYPREFIX_CODEB

        And you want to be able to access these as CODEA and CODEB,
        then your prefix needs to be "MYPREFIX_"

        :param source: The environment variable prefix
        :return: None
        """
        self.source = source

    def refresh(self):
        """
        Updates mappings based on this source.
        """

        mapping = {}

        for key, value in os.environ.items():
            if key.startswith(self.source):
                mapping[key.removeprefix(self.source)] = value

        self.mapping = mapping
