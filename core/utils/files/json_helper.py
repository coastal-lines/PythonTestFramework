import json
from typing import Dict, Any

from jsonpath_ng import jsonpath, parse


"""
json.load()  - load from file
json.loads() - load from string

"""

def convert_text_into_dictonary(text: str) -> Dict[str, Any]:
    """
    Deserialize into object
    """

    return json.loads(text)

def convert_text_from_file_into_dictonary(file_path: str) -> Dict[str, Any]:
    """
    Deserialize from file

    Access mode:
    -r:  read only
    -rb: read only in binary format
    """

    try:
        with open(file_path, mode="r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError as ex:
        print(f"File '{file_path}' not found.")
        raise ex
    except json.JSONDecodeError as ex:
        print(f"Error decoding JSON in file '{file_path}'.")
        raise ex

def convert_object_into_text(data: Any) -> str:
    """
    Serialize into text
    """

    return json.dumps(data)

def convert_object_from_file_into_text(file_path: str, data: Dict[str, Any]):
    """
    Serialize into file
    """

    with open(file_path, "w") as write_file:
        json.dump(data, write_file)

def parse_json_and_get_result(json_object, expression) -> list:
    """
    $.[*] - full document
    $._key_[*] - get all objects by key from the root
    $._key_[*]._key_ - get all values of all objects from the root (ex: "$.elements[*].label")
    """

    jsonpath_expr = parse(expression)
    return [match.value for match in jsonpath_expr.find(json_object)]
