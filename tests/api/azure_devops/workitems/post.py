from api.azure_devops import data_generator


def test_post_attachment():
    response_post_attachment = data_generator.upload_attachment_to_project()
    assert response_post_attachment.status_code == 201
    assert response_post_attachment.response_model.id is not None
    assert response_post_attachment.response_model.url != ""