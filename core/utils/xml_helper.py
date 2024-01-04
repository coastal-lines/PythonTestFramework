from lxml import etree

def convert_text_into_xml(text: str):
    try:
        xml_tree = etree.fromstring(text)
        return xml_tree
    except etree.XMLSyntaxError as e:
        print(f"Error during text converting into xml object: {e}")
        return None

def find_element_by_xpath(user_xml, user_xpath, element_number=0):
    return user_xml.xpath(user_xpath)[element_number]