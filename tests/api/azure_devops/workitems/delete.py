import pytest
from api.azure_devops.azure_dto import AzureDTO


@pytest.mark.parametrize("workitem_id, comment_id", [("3", "12448840")])
@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{AzureDTO().organization}"}], indirect=True)
def test_put_comment_reaction(api_client, workitem_id, comment_id):
    response = api_client.delete(url=f"/{AzureDTO().project}/_apis/wit/workItems/{workitem_id}/comments/{comment_id}?api-version=7.0-preview", auth=AzureDTO().basic_authorization)
    assert response.status_code == 204
