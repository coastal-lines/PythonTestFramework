import pytest
from api.azure_devops.azure_dto import AzureDTO
from core.models.api.azure_devops.response_put_comment_reaction import ResponsePutCommentReaction


@pytest.mark.parametrize("reaction", ["heart"])
@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{AzureDTO().organization}"}], indirect=True)
def test_put_comment_reaction(api_client, reaction):
    response = api_client.put(url=f"/{AzureDTO().project}/_apis/wit/workItems/1/comments/12437227/reactions/{reaction}?api-version=7.0-preview",
                   auth=AzureDTO().basic_authorization)

    response.response_model = ResponsePutCommentReaction.from_dict(response.as_dict)

    assert response.status_code == 200
    assert response.response_model.type == reaction
    assert response.response_model.count == 1
    assert response.response_model.isCurrentUserEngaged is True
    assert response.response_model.commentId > 0