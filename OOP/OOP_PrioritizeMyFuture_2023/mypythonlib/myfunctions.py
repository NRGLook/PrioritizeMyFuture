import json
import tomllib
import xml


def JSON_dump(self, file):
    return json.dump(self, file)


def JSON_dumps(self):
    return json.dumps(self)


@staticmethod
def JSON_load(self, file):
    return json.load(file)


@staticmethod
def JSON_loads(self, file):
    return json.loads(file)


@staticmethod
def TOML_load(self, file):
    return tomllib.load(file)


@staticmethod
def TOML_loads(self, file):
    return tomllib.loads(file)


def XML_PARSERS(self):
    return xml.parsers
