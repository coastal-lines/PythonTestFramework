import pytest
from api.azure_devops.azure_dto import AzureDTO
from core.utils.files import json_helper
from core.models.api.azure_devops.response_patch_comment import ResponsePatchWorkitemComment


@pytest.mark.parametrize('comment_text', ["patch_add_workitems_comment_test"])
@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{AzureDTO().organization}"}], indirect=True)
def test_patch_add_workitems_comment(api_client, comment_text):
    payload = json_helper.convert_object_into_text([{
        "op": "add",
        "path": "/fields/System.History",
        "value": comment_text
    }])

    headers = {
        "Content-Type": "application/json-patch+json"
    }

    response = api_client.patch(url=f"/_apis/wit/workitems/1?api-version=7.0",
                                auth=AzureDTO().basic_authorization,
                                payload=payload,
                                headers=headers,
                                response_model=ResponsePatchWorkitemComment)

    assert response.status_code == 200
    assert response.response_model.fields.System_History == "patch_add_workitems_comment_test"