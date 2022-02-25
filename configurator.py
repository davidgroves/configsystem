"""
Manages configuration from Environment Variables, JSON or YAML sources
"""

from __future__ import annotations

import abc
import logging
import os
import signal
import typing

import duplicatefilter

logger = logging.getLogger(__name__)


class ConfigRegistry:
    """
    A registry for configuration sources
    """

    sources: typing.Dict[str, BaseConfig] = {}

    @classmethod
    def register_source(cls, source_name: str, source: BaseConfig):
        """
        Register a source of configuration
        """
        cls.sources[source_name] = source

    @classmethod
    def get_item(cls, source_name: str, key: str) -> typing.Optional[str]:
        """
        Fetch a config item, given a config source name and key
        """
        return cls.sources[source_name].get_value(key)

    @classmethod
    def refresh_all(cls):
        """
        Refresh all dynamically updatable configs
        """

        for config_source in cls.sources.values():
            if config_source.dynamic_reload:
                config_source.refresh()


class BaseConfig(abc.ABC):
    """
    Base class for configuration sources
    """

    def __init__(self, source: str, name: str, dynamic_reload: bool = False, register: bool = False):
        self.mapping: dict[str, str] = {}
        self.source = source
        self.dynamic_reload = dynamic_reload
        self.register = register
        super().__init__()

        if self.register:
            ConfigRegistry.register_source(name, self)

        if self.dynamic_reload and os.name != "posix":
            with duplicatefilter.DuplicateFilter(logger=logger):
                logger.warning(
                    "Cannot support dynamic reloading on non-POSIX platforms"
                )

    @abc.abstractmethod
    def set_source(self, source: str):
        """
        Set the name of a source. Dependant on source type for meaning.
        """

    @abc.abstractmethod
    def refresh(self):
        """
        Loads or reloads the data from the source. Exact behaviour source specific.
        """

    def get_value(self, key: str) -> typing.Union[str, None]:
        """
        Looks up the key in the current config, and return it if present. Will return None if
        the key doesn't exist.
        """
        return self.mapping.get(key)


def refresh_configs():
    """
    Called when SIGHUP is handled.
    """

    logging.info("Handling SIGHUP. Reloading configs")
    ConfigRegistry.refresh_all()


if os.name == "posix":
    signal.signal(signal.SIGHUP, refresh_configs)  # type: ignore
