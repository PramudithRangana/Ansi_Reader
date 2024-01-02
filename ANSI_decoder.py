import re
import zipfile
import xml.etree.ElementTree as Et
import html


class XmlProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.xml_content = self.extract_xml_content()

    def extract_xml_content(self):
        with zipfile.ZipFile(self.input_file, 'r') as zip_ref:
            return zip_ref.read('memo_content.xml').decode('utf-8', errors='replace')

    @staticmethod
    def remove_html_tags(text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '\n', text).replace('\n\n', '\n')

    @staticmethod
    def extract_plain_text(element):
        return element.text or ''

    def process_xml(self):
        root = Et.fromstring(self.xml_content)
        plain_text = ' '.join(self.extract_plain_text(elem) for elem in root.iter())
        return html.unescape(self.remove_html_tags(plain_text)).strip()


def main():
    input_file = input("Path to file: ")
    xml_processor = XmlProcessor(input_file)
    result = xml_processor.process_xml()
    print(result)


if __name__ == "__main__":
    main()


""" Progress in Successfully """
