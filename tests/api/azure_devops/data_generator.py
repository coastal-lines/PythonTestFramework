from api.azure_devops.azure_dto import AzureDTO
from core.utils.config_manager import ConfigUtils
from core.wrappers.api.api_requests_wrapper import ApiRequestsWrapper
from core.utils.files import path_helper
from core.utils.files import json_helper
from models.api.azure_devops.response_post_attachment import ResponsePostAttachment
from models.api.azure_devops.response_patch_attachment import ResponsePatchWorkitemAttachment
from models.api.azure_devops.response_post_workitem import ResponsePostWorkitem
from resources.desktop.desktop_image_resources_data_class import DesktopImageResourcesData


def upload_attachment_to_project():
    api_client = ApiRequestsWrapper(f"https://dev.azure.com/{AzureDTO().organization}/")

    files = {
        "file": open(path_helper.get_resource_path(DesktopImageResourcesData.free_quiz_image_1), 'rb')
    }

    headers = {
        "Content-Type": "application/octet-stream"
    }

    response = api_client.post("_apis/wit/attachments?fileName=free_quiz_image_1.png&uploadType=Simple&api-version=7.0",
                               auth=AzureDTO().basic_authorization,
                               headers=headers,
                               files=files,
                               response_model=ResponsePostAttachment)

    #response_post_attachment = ResponsePostAttachment.from_dict(response.as_dict)
    return response

def add_attachment_to_workitem(attachment_url: str, workitem_id: str):
    api_client = ApiRequestsWrapper(f"https://dev.azure.com/{AzureDTO().organization}/")

    payload = json_helper.convert_object_into_text([
        {
            "op": "add",
            "path": "/relations/-",
            "value": {
                "rel": "AttachedFile",
                "url": attachment_url
            }
        }
    ])

    headers = {
        "Content-Type": "application/json-patch+json"
    }

    response = api_client.patch(url=f"/{AzureDTO().project}/_apis/wit/workitems/{workitem_id}?api-version=7.0",
                                auth=AzureDTO().basic_authorization,
                                payload=payload,
                                headers=headers)

    response = ResponsePatchWorkitemAttachment.from_dict(response.as_dict)
    return response

def add_comment_to_workitem(workitem_id: str, comment_text="comment_text"):
    api_client = ApiRequestsWrapper(f"https://dev.azure.com/{AzureDTO().organization}")

    payload = json_helper.convert_object_into_text([
        {
            "op": "add",
            "path": "/fields/System.History",
            "value": comment_text
        }
    ])

    headers = {
        "Content-Type": "application/json-patch+json"
    }

    response = api_client.patch(url=f"/{AzureDTO().project}/_apis/wit/workitems/{workitem_id}?api-version=7.0",
                                auth=AzureDTO().basic_authorization,
                                payload=payload,
                                headers=headers)

    main_response = ResponsePostWorkitem.from_dict(response.as_dict)
    return main_response

def create_new_task_with_attach_and_comment(add_comment=False, add_attach=False):
    api_client = ApiRequestsWrapper(f"https://dev.azure.com/{AzureDTO().organization}/")

    payload = json_helper.convert_object_into_text([
        {
            "op": "add",
            "path": "/fields/System.Title",
            "value": "New Task"
        },
        {
            "op": "add",
            "path": "/fields/System.Description",
            "value": "Description of the task"
        },
        {
            "op": "add",
            "path": "/fields/System.AssignedTo",
            "value": ConfigUtils().get_config().azure_dev_ops.default_user_for_assign
        },
        {
            "op": "add",
            "path": "/fields/System.AreaPath",
            "value": ConfigUtils().get_config().azure_dev_ops.project
        },
        {
            "op": "add",
            "path": "/fields/System.IterationPath",
            "value": ConfigUtils().get_config().azure_dev_ops.project
        },
        {
            "op": "add",
            "path": "/fields/System.Tags",
            "value": "tag1;tag2"
        }
    ])

    headers = {
        "Content-Type": "application/json-patch+json"
    }

    response = api_client.post(url=f"/{AzureDTO().project}/_apis/wit/workitems/$Task?api-version=7.0",
                            auth=AzureDTO().basic_authorization,
                            payload=payload,
                            headers=headers)

    response_post_workitem = ResponsePostWorkitem.from_dict(response.as_dict)

    if add_comment:
        add_comment_to_workitem(response_post_workitem.id)

    if add_attach:
        upload_response = upload_attachment_to_project()
        add_attachment_to_workitem(upload_response.url, response_post_workitem.id)
        response_post_workitem = api_client.get(url=f"/{AzureDTO().project}/_apis/wit/workitems/{response_post_workitem.id}?api-version=7.0", auth=AzureDTO().basic_authorization)

    return response_post_workitem
