import pytest
from api.azure_devops.azure_dto import AzureDTO


@pytest.mark.parametrize('task_id', [1])
@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{AzureDTO().organization}"}], indirect=True)
def test_get_workitems_task_response_has_cookie(api_client, task_id):
    response = api_client.get(url=f"/_apis/wit/workitems/{task_id}", auth=AzureDTO().basic_authorization)
    assert response.cookies["VstsSession"] is not None

@pytest.mark.parametrize('task_id', [1])
@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{AzureDTO().organization}"}], indirect=True)
def test_get_workitems_task_response_headers_are_correct(api_client, task_id):
    response = api_client.get(url=f"/_apis/wit/workitems/{task_id}", auth=AzureDTO().basic_authorization)
    assert response.headers["Content-Length"] == "983"
    assert response.headers["Content-Encoding"] == "gzip"
    assert response.headers["Cache-Control"] == "no-cache, no-store, must-revalidate"
    assert response.headers["Access-Control-Expose-Headers"] == "Request-Context"
    assert "application/json" in response.headers["Content-Type"]


