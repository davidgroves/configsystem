from unittest import mock
import os
from config_types import EnvironmentConfig, JsonConfig, StaticConfig, YamlConfig

def test_static_config():
    static = StaticConfig(name="static", mapping={"Sky": "Blue", "Grass": "Green"})

@mock.patch.dict(os.environ, {"TESTPREFIX_TESTKEY": "TESTDATA"})
def test_dynamicenv_get_single_entry():
    dynenv = EnvironmentConfig(name="dynenv", source="TESTPREFIX_")
    assert dynenv.get_value("TESTKEY") == "TESTDATA"


@mock.patch.dict(
    os.environ, {"TESTPREFIX_TESTKEY1": "TESTDATA1", "TESTPREFIX_TESTKEY2": "TESTDATA2"}
)
def test_dynamicenv_get_double_entry():
    dynenv = EnvironmentConfig(name="dynenv", source="TESTPREFIX_")
    assert dynenv.get_value("TESTKEY1") == "TESTDATA1"
    assert dynenv.get_value("TESTKEY2") == "TESTDATA2"


@mock.patch.dict(
    os.environ, {"TESTPREFIX_TESTKEY1": "TESTDATA1", "TESTPREFIX_TESTKEY2": "TESTDATA2"}
)
def test_dynamicenv_get_missing_entry():
    dynenv = EnvironmentConfig(name="dynenv", source="TESTPREFIX_")
    assert dynenv.get_value("DOES_NOT_EXIST") is None


def test_single_key_json():
    json = JsonConfig(name="json", source="tests/test.json")
    assert json.get_value("TESTKEY") == "TESTVALUE"


def test_double_key_json():
    json = JsonConfig(name="json", source="tests/double_test.json")
    assert json.get_value("TESTKEY1") == "TESTVALUE1"
    assert json.get_value("TESTKEY2") == "TESTVALUE2"


def test_missing_key_json():
    json = JsonConfig(name="json", source="tests/double_test.json")
    assert json.get_value("TESTKEY3") is None


def test_single_key_yaml():
    yaml = YamlConfig(name="yaml", source="tests/test.yaml")
    assert yaml.get_value("TESTKEY") == "TESTVALUE"


def test_double_key_yaml():
    yaml = YamlConfig(name="yaml", source="tests/double_test.yaml")
    assert yaml.get_value("TESTKEY1") == "TESTVALUE1"
    assert yaml.get_value("TESTKEY2") == "TESTVALUE2"


def test_missing_key_yaml():
    yaml = YamlConfig(name="yaml", source="tests/double_test.yaml")
    assert yaml.get_value("TESTKEY3") is None

import pathlib
