import re
import shutil
import zipfile
import xml.etree.ElementTree as Et
import html


class XmlProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.xml_content = self.extract_xml_content()

    def extract_xml_content(self):
        try:
            with zipfile.ZipFile(self.input_file, 'r') as zip_ref:
                return zip_ref.read('memo_content.xml').decode('utf-8', errors='replace')

        except FileNotFoundError as _fnf:
            print(f"{self.input_file} - FILE NOT FOUND !\n")

        except Exception as _e:
            print("Error :", _e)

    @staticmethod
    def remove_html_tags(text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '\n', text).replace('\n\n', '\n')

    @staticmethod
    def extract_plain_text(element):
        return element.text or ''

    def process_xml(self):
        try:
            root = Et.fromstring(self.xml_content)
            plain_text = ' '.join(self.extract_plain_text(elem) for elem in root.iter())
            return html.unescape(self.remove_html_tags(plain_text)).strip()
        except TypeError:
            pass
        except Exception as _e:
            print("Error :", _e)


def notice():
    msg = " The END "
    padding, _ = shutil.get_terminal_size()
    print(msg.center(padding, '+'), '\n')


def main():
    try:
        input_file = input("Path to file: ")

        if input_file == "exit":
            print("Program Ended !")
            exit()
        else:
            xml_processor = XmlProcessor(input_file)
            result = xml_processor.process_xml()

            if result is not None:
                print(result)
                notice()

            main()
    except KeyboardInterrupt as _ke:
        notice()
        print("Program Stopped Manually.")
        pass


if __name__ == "__main__":
    main()

""" Progress in Successfully """
# C:\Users\Pramudith Rangana\Desktop\New folder (5)\Memo_files (14).memo
