import allure
import pytest

from karaburma.api.models.response_model import RootKaraburmaResponse
from karaburma.main import Karaburma

from core.utils.config_manager import ConfigUtils
from core.utils.files import files_helper, path_helper


@allure.step("Karaburma debug image")
def attach_debug_image(request, karaburma_result: RootKaraburmaResponse):
    image_base64 = karaburma_result.debug_screenshot
    scr_path = path_helper.screenshot_path_for_logs(request.node, f"_debug_image")
    files_helper.save_base64_as_png_image(image_base64, scr_path)
    allure.attach.file(scr_path, attachment_type=allure.attachment_type.PNG)

@pytest.fixture()
def karaburma(request) -> Karaburma:
    karaburma = Karaburma(ConfigUtils().get_config().karaburma.config_path, "screenshot", "default", False)

    yield karaburma

    if (pytest.karaburma_result is not None):
        attach_debug_image(request, pytest.karaburma_result)


