from lxml import etree

def convert_text_file_into_xml(text: bytes):
    try:
        xml_root = etree.fromstring(text)
        return xml_root
    except ValueError as ex:
        print(f"Text object should has 'bytes' type. Please check type of your text object. \n {ex}")
    except etree.XMLSyntaxError as ex:
        print(f"Error during text converting into xml object: {ex}")

def find_element_by_xpath(user_xml, user_xpath, element_number=0):
    return user_xml.xpath(user_xpath)[element_number]