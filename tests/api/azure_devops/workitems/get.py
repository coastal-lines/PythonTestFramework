import pytest
from core.utils.config_manager import ConfigUtils


organization = ConfigUtils().get_config().azure_dev_ops.organization
basic_auth_full_access_token = ("any_user", ConfigUtils().get_config().azure_dev_ops.token_for_full_access)

@pytest.mark.parametrize('task_id', [1])
@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{organization}"}], indirect=True)
def test_get_workitems_task_response_has_cookie(api_client, task_id):
    response = api_client.get(url=f"/_apis/wit/workitems/{task_id}", basic_auth=basic_auth_full_access_token)
    assert response.cookies["VstsSession"] is not None

@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{organization}"}], indirect=True)
def test_get_workitems_task_response_headers_are_correct(api_client):

    response = api_client.get(url=f"/_apis/wit/workitems/{task_id}", basic_auth=basic_auth_full_access_token)
    assert response.headers["Content-Length"] == "936"
    assert response.headers["Content-Encoding"] == "gzip"
    assert response.headers["Cache-Control"] == "no-cache"
    assert response.headers["Access-Control-Expose-Headers"] == "Request-Context"
    assert "application/json" in response.headers["Content-Type"]