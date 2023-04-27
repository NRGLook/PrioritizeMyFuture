import json
import tomllib
import xml


class JSON:
    def JSON_dump(self, file):
        return json.dump(self, file)

    def JSON_dumps(self):
        return json.dumps(self)

    def JSON_load(self, file):
        return json.load(file)

    def JSON_loads(self, file):
        return json.loads(file)


class TOML:
    def TOML_load(self, file):
        return tomllib.load(file)

    def TOML_loads(self, file):
        return tomllib.loads(file)


class XML:
    def XML_PARSERS(self):
        return xml.parsers
