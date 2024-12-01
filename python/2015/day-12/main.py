import json

class Parser:
    def __init__(self):
        self.type_parser_map = {
            dict: self.parse_dict,
            list: self.parse_list,
            str: self.parse_str,
            int: self.parse_int,
        }
        self.total = 0

    def try_parse(self, data):
        _type = type(data)
        parser = self.type_parser_map.get(_type)
        if not parser:
            raise ValueError(f"Unknown type {_type}")
        parser(data)

    def parse_list(self, data):
        for x in data:
            self.try_parse(x)

    def parse_dict(self, data):
        if "red" in data.values():
            return
        for v in data.values():
            self.try_parse(v)

    def parse_str(self, _):
        pass

    def parse_int(self, data):
        self.total += data



with open("input.txt") as f:
    data = json.load(f)

p = Parser()
p.try_parse(data)
print(p.total)
