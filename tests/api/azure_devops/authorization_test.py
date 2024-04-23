import pytest
from core.utils.config_manager import ConfigUtils


organization = ConfigUtils().get_config().azure_dev_ops.organization

@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{organization}"}], indirect=True)
def test_validate_authorization_200(api_client):
    response = api_client.get(url=f"/_apis/projects?api-version=7.0",
                              auth=("any_user", ConfigUtils().get_config().azure_dev_ops.token_for_full_access))
    assert response.status_code == 200

@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{organization}"}], indirect=True)
def test_validate_authorization_empty_token_401(api_client):
    response = api_client.get(url=f"/_apis/projects?api-version=7.0",
                              auth=("any_user", ""))
    assert response.status_code == 401

@pytest.mark.parametrize("api_client", [{"url": f"https://dev.azure.com/{organization}"}], indirect=True)
def test_validate_authorization_no_access_token_401(api_client):
    response = api_client.get(url=f"/_apis/projects?api-version=7.0",
                              auth=("any_user", ConfigUtils().get_config().azure_dev_ops.token_for_agents_pool_only))
    assert response.status_code == 401