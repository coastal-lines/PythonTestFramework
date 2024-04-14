import json

import pytest
import requests
from assertpy.assertpy import assert_that, soft_assertions
from cerberus import Validator

from core.utils.files import json_helper
from resources.api.json.schema_karaburma_data_class import SchemaKaraburmaResponseDataClass


@pytest.mark.api
def test_karaburma_server_available(karaburma_client):
    response = karaburma_client.request.get()
    assert response.status_code == requests.codes.ok

@pytest.mark.api
def test_image_file_contains_any_button(karaburma_file_mode_buttons_only_response):
    result = json.loads(karaburma_file_mode_buttons_only_response.text)

    with (soft_assertions()):
        assert_that(result["elements"], description="At least one button object should be detected.").is_not_empty().extracting("label").contains("button")

@pytest.mark.api
@pytest.mark.xdist_group(name="non")
def test_image_file_validate_schema_response(karaburma_file_mode_buttons_only_response):
    response_json = json_helper.convert_text_into_json(karaburma_file_mode_buttons_only_response.text)

    validator = Validator(SchemaKaraburmaResponseDataClass.button_elements_only, require_all=True)
    is_valid = validator.validate(response_json)

    assert_that(is_valid, description=validator.errors).is_true()

@pytest.mark.api
@pytest.mark.xdist_group(name="non")
def test_image_file_validate_schema_for_all_simple_elements(karaburma_file_mode_buttons_only_response):
    response_json = json_helper.convert_text_into_json(karaburma_file_mode_buttons_only_response.text)

    validator = Validator(SchemaKaraburmaResponseDataClass.simple_element, require_all=True)
    simple_elements = json_helper.parse_json_and_get_result(response_json, "$.elements[*]")

    with soft_assertions():
        for element in simple_elements:
            is_valid = validator.validate(element)
            assert_that(is_valid, description=validator.errors).is_true()