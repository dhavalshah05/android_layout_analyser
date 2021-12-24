import xml.etree.ElementTree as ET
import string


class LayoutParser:

    def __init__(self, file_path: string):
        self.counterDic = {}
        with open(file_path, mode="r") as xml_file:
            xml_data = xml_file.read()
            root = ET.XML(xml_data)

            self.__increment_counter(tag=root.tag)
            self.__parse(root)

    def __increment_counter(self, tag: string):
        content = tag.split(".")
        key = content[len(content) - 1]

        if key in self.counterDic.keys():
            self.counterDic[key] += 1
        else:
            self.counterDic[key] = 1

    def __parse(self, root: ET.Element):
        for item in root:
            self.__increment_counter(tag=item.tag)
            self.__parse(item)

    def get_counter(self) -> dict:
        return self.counterDic



