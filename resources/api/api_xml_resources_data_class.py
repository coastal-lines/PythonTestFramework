from dataclasses import dataclass
from lxml import etree

from core.utils.files import xml_helper, path_helper


class LazyLoadKaraburmaMockXml:
    """
    This class is a descriptor for 'ApiXmlResourceData.karaburma_xml_response' field.
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.root_xml: etree._Element = None

    def __get__(self, instance, owner) -> etree._Element:
        if self.root_xml is None:
            self.root_xml = xml_helper.load_xml_from_file(self.filename)
        return self.root_xml

@dataclass
class ApiXmlResourceData:
    """
    Get xml by python descriptor.
    Descriptors allow to control accessing to class attributes.
    It means that descriptors can control and modify logic for attributes accessing.
    """
    karaburma_xml_response: LazyLoadKaraburmaMockXml = LazyLoadKaraburmaMockXml(
        path_helper.get_resource_path("resources/api/xml/karaburma_response_xml.xml")
    )