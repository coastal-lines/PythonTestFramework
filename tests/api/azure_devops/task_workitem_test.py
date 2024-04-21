import pytest

from core.utils.config_manager import ConfigUtils


@pytest.mark.parametrize('task_id', [1])
@pytest.mark.parametrize("api_client", [{"url": "https://dev.azure.com/coastallines"}], indirect=True)
def test_get_single_project_list(api_client, task_id):
    headers = {
        "Authorization": f"{ConfigUtils().get_config().azure_dev_ops.access_token_for_tests}"
    }

    response = api_client.get(url=f"/_apis/wit/workitems/{task_id}", payload=None, headers=headers)
    assert response.status_code == 200