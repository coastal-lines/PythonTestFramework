import json
import requests
from assertpy.assertpy import assert_that, soft_assertions
from cerberus import Validator

from core.utils.files import path_helper, json_helper
from resources.api.api_image_resources_data_class import ApiImageResourcesData


KARABURMA_BASE_URL = "http://127.0.0.1:8900/api/v1"

SCHEMA_SIMPLE_ELEMENT = {
                "id": {"type": "string", "required": True},
                "x": {"type": "integer", "required": True},
                "y": {"type": "integer", "required": True},
                "w": {"type": "integer", "required": True},
                "h": {"type": "integer", "required": True},
                "label": {"type": "string", "required": True},
                "prediction": {"type": "string", "required": True},
                "orig_img_base64": {"type": "string", "required": True},
                "text": {"type": "string", "required": True}
            }

SCHEMA_RESPONSE_FILE_MODE_BUTTON_ELEMENTS_ONLY = {
    "w": {"type": "integer", "required": True},
    "h": {"type": "integer", "required": True},
    "elements": {
        "type": "list",
        "schema": {
            "type": "dict",
            "schema": {
                "id": {"type": "string", "required": True},
                "x": {"type": "integer", "required": True},
                "y": {"type": "integer", "required": True},
                "w": {"type": "integer", "required": True},
                "h": {"type": "integer", "required": True},
                "label": {"type": "string", "required": True},
                "prediction": {"type": "string", "required": True},
                "orig_img_base64": {"type": "string", "required": True},
                "text": {"type": "string", "required": True}
            }
        }
    },
    "listbox_elements": {"type": "list"},
    "table_elements": {"type": "list"},
    "debug_screenshot": {"type": "string", "required": True}
}

SCHEMA_RESPONSE_ALL_ELEMENTS = {
    "type": "object",
    "properties": {
        "w": {"type": "integer"},
        "h": {"type": "integer"},
        "elements": {
            "type": "array",
            "items": {
                "id": {"type": "string"},
                "x": {"type": "integer"},
                "y": {"type": "integer"},
                "w": {"type": "integer"},
                "h": {"type": "integer"},
                "label": {"type": "string"},
                "prediction": {"type": "string"},
                "orig_img_base64": {"type": "string"},
                "text": {"type": "string"}
            },
            "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "text"]
        },
        "listbox_elements": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "x": {"type": "integer"},
                    "y": {"type": "integer"},
                    "w": {"type": "integer"},
                    "h": {"type": "integer"},
                    "label": {"type": "string"},
                    "prediction": {"type": "string"},
                    "orig_img_base64": {"type": "string"},
                    "text": {"type": "string"},
                    "v_scroll": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "x": {"type": "integer"},
                            "y": {"type": "integer"},
                            "w": {"type": "integer"},
                            "h": {"type": "integer"},
                            "label": {"type": "string"},
                            "prediction": {"type": "string"},
                            "orig_img_base64": {"type": "string"},
                            "first_button": {
                                "type": "object",
                                "properties": {
                                    "centre_x": {"type": "integer"},
                                    "centre_y": {"type": "integer"}
                                },
                                "required": ["centre_x", "centre_y"]
                            },
                            "second_button": {
                                "type": "object",
                                "properties": {
                                    "centre_x": {"type": "integer"},
                                    "centre_y": {"type": "integer"}
                                },
                                "required": ["centre_x", "centre_y"]
                            }
                        },
                        "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "first_button",
                                     "second_button"]
                    },
                    "full_img_base64": {"type": "string"},
                    "full_listbox": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "x": {"type": "integer"},
                            "y": {"type": "integer"},
                            "w": {"type": "integer"},
                            "h": {"type": "integer"},
                            "label": {"type": "string"},
                            "prediction": {"type": "string"},
                            "orig_img_base64": {"type": "string"},
                            "text": {"type": "string"},
                            "full_img_base64": {"type": "string"}
                        },
                        "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "text", "full_img_base64"]
                    }
                },
                "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "text", "v_scroll", "full_listbox"]
            }
        },
        "table_elements": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "x": {"type": "integer"},
                    "y": {"type": "integer"},
                    "w": {"type": "integer"},
                    "h": {"type": "integer"},
                    "label": {"type": "string"},
                    "prediction": {"type": "string"},
                    "orig_img_base64": {"type": "string"},
                    "v_scroll": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "x": {"type": "integer"},
                            "y": {"type": "integer"},
                            "w": {"type": "integer"},
                            "h": {"type": "integer"},
                            "label": {"type": "string"},
                            "prediction": {"type": "string"},
                            "orig_img_base64": {"type": "string"},
                            "first_button": {
                                "type": "object",
                                "properties": {
                                    "centre_x": {"type": "integer"},
                                    "centre_y": {"type": "integer"}
                                },
                                "required": ["centre_x", "centre_y"]
                            },
                            "second_button": {
                                "type": "object",
                                "properties": {
                                    "centre_x": {"type": "integer"},
                                    "centre_y": {"type": "integer"}
                                },
                                "required": ["centre_x", "centre_y"]
                            }
                        },
                        "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "first_button",
                                     "second_button"]
                    },
                    "h_scroll": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "x": {"type": "integer"},
                            "y": {"type": "integer"},
                            "w": {"type": "integer"},
                            "h": {"type": "integer"},
                            "label": {"type": "string"},
                            "prediction": {"type": "string"},
                            "orig_img_base64": {"type": "string"},
                            "first_button": {
                                "type": "object",
                                "properties": {
                                    "centre_x": {"type": "integer"},
                                    "centre_y": {"type": "integer"}
                                },
                                "required": ["centre_x", "centre_y"]
                            },
                            "second_button": {
                                "type": "object",
                                "properties": {
                                    "centre_x": {"type": "integer"},
                                    "centre_y": {"type": "integer"}
                                },
                                "required": ["centre_x", "centre_y"]
                            }
                        },
                        "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "first_button",
                                     "second_button"]
                    },
                    "cells": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "centre_x": {"type": "integer"},
                                "centre_y": {"type": "integer"},
                                "text": {"type": "string"},
                                "address": {
                                    "type": "array",
                                    "items": {"type": "integer"}
                                }
                            },
                            "required": ["centre_x", "centre_y", "text", "address"]
                        }
                    },
                    "full_table": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "x": {"type": "integer"},
                            "y": {"type": "integer"},
                            "w": {"type": "integer"},
                            "h": {"type": "integer"},
                            "label": {"type": "string"},
                            "prediction": {"type": "string"},
                            "orig_img_base64": {"type": "string"},
                            "cells": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "centre_x": {"type": "integer"},
                                        "centre_y": {"type": "integer"},
                                        "text": {"type": "string"},
                                        "address": {
                                            "type": "array",
                                            "items": {"type": "integer"}
                                        }
                                    },
                                    "required": ["centre_x", "centre_y", "text", "address"]
                                }
                            }
                        },
                        "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "cells"]
                    }
                },
                "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "v_scroll", "h_scroll",
                             "cells", "full_table"]
            }
        },
        "debug_screenshot": "string"
    },
    "required": ["w", "h", "elements", "listbox_elements", "table_elements", "debug_screenshot"]
}

def test_karaburma_server_available():
    response = requests.get(url=KARABURMA_BASE_URL)
    assert response.status_code == requests.codes.ok


def test_image_file_contains_any_button(karaburma_file_mode_buttons_only_response):
    result = json.loads(karaburma_file_mode_buttons_only_response.text)

    with (soft_assertions()):
        assert_that(result["elements"], description="At least one button object should be detected.").is_not_empty().extracting("label").contains("button")

def test_image_file_validate_schema_response(karaburma_file_mode_buttons_only_response):
    response_json = json_helper.convert_text_into_json(karaburma_file_mode_buttons_only_response.text)

    validator = Validator(SCHEMA_RESPONSE_FILE_MODE_BUTTON_ELEMENTS_ONLY, require_all=True)
    is_valid = validator.validate(response_json)

    assert_that(is_valid, description=validator.errors).is_true()

def test_image_file_validate_schema_for_all_simple_elements(karaburma_file_mode_buttons_only_response):
    response_json = json_helper.convert_text_into_json(karaburma_file_mode_buttons_only_response.text)

    validator = Validator(SCHEMA_SIMPLE_ELEMENT, require_all=True)
    simple_elements = json_helper.parse_json_and_get_result(response_json, "$.elements[*]")

    with soft_assertions():
        for element in simple_elements:
            is_valid = validator.validate(element)
            assert_that(is_valid, description=validator.errors).is_true()