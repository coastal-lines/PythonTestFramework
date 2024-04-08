import karaburma.api.models.response_model
from karaburma.api.models.response_model import RootKaraburmaResponse


def get_element_centroid(element: karaburma.api.models.response_model.Element) -> tuple[int, int]:
    x = element.x + (element.w // 2)
    y = element.y + (element.h // 2)
    return x, y

def deserialize_karaburma_response_into_object(response: dict) -> RootKaraburmaResponse:
    return RootKaraburmaResponse(response["w"],
                                 response["h"],
                                 response["elements"],
                                 response["listbox_elements"],
                                 response["table_elements"],
                                 response["debug_screenshot"])