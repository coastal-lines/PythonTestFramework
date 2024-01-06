from dataclasses import dataclass

from core.utils import xml_helper, path_helper
from resources.api.api_image_resources_data_class import ApiImageResourcesData


# Descriptor for 'ApiXmlResourceData.karaburma_xml_response' field.
class LazyLoadKaraburmaMockXml:
    def __init__(self, filename: str):
        self.filename = filename
        self.root_xml = None

    def __get__(self, instance, owner):
        if self.root_xml is None:
            with open(self.filename, 'rb') as file:
                self.root_xml = xml_helper.convert_text_file_into_xml(file.read())
        return self.root_xml

@dataclass
class ApiXmlResourceData:
    # Get xml by python descriptor.
    # Descriptors allow to control accessing to class attributes.
    # It means that descriptors can control and modify logic for attributes accessing.
    karaburma_xml_response: LazyLoadKaraburmaMockXml = LazyLoadKaraburmaMockXml(path_helper.get_resource_path("resources/api/xml/karaburma_response_xml.xml"))