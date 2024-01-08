import json
from jsonpath_ng import jsonpath, parse


"""
json.load()  - load from file
json.loads() - load from string
"""

def convert_text_into_json(text):
    return json.loads(text)

def read_json_from_file(file_path):
    """
    Access mode:
    -r:  read only
    -rb: read only in binary format
    """

    with open(file_path, mode="r") as file:
        return json.load(file)

def parse_json_and_get_result(json_object, expression):
    """
    $.[*] - full document
    $._key_[*] - get all objects by key from the root
    $._key_[*]._key_ - get all values of all objects from the root (ex: "$.elements[*].label")
    """

    jsonpath_expr = parse(expression)
    return [match.value for match in jsonpath_expr.find(json_object)]