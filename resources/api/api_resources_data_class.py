from dataclasses import dataclass

from core.utils import xml_helper


@dataclass
class ApiResourcesData:
    karaburma_main_image: str = "resources/api/images/all_elements.png"
    karaburma_xml_response: str = None

    def __load_karaburma_xml_response(self):
        if self.karaburma_xml_response is None:
            with open("resources/api/xml/karaburma_response_xml.xml") as file:
                self.karaburma_xml_response = xml_helper.convert_text_into_xml(file.read())

    def get_karaburma_xml_response():
        self.__load_karaburma_xml_response()
        return self.karaburma_xml_response