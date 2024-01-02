# XML Processor in Python

## Overview
This Python script defines a class called `XmlProcessor` that is designed to process XML content from a specified file. The program reads a ZIP file containing an XML file named 'memo_content.xml', extracts the XML content, and processes it to obtain plain text without HTML tags.

## Code Explanation

### XmlProcessor Class
- **Constructor (`__init__`):**
  - Initializes the `XmlProcessor` object with the path to the input file.
  - Calls the `extract_xml_content` method to read and decode the XML content from the specified ZIP file.

- **`extract_xml_content` Method:**
  - Uses the `zipfile` module to open the input file as a ZIP archive.
  - Reads the content of the 'memo_content.xml' file from the ZIP archive.
  - Decodes the content as UTF-8 and returns it.

- **`remove_html_tags` Method:**
  - Removes HTML tags from the provided text using regular expressions.
  - Replaces HTML tags with newline characters and then cleans up consecutive newlines.

- **`extract_plain_text` Method:**
  - Extracts plain text from an XML element.
  - Returns the text of the element if available, or an empty string otherwise.

- **`process_xml` Method:**
  - Parses the XML content using the `ElementTree` module.
  - Extracts plain text from all XML elements and concatenates them into a single string.
  - Uses `html.unescape` to convert HTML escape sequences to their corresponding characters.
  - Strips leading and trailing whitespaces from the resulting plain text.

### Main Function (`main`):
- Prompts the user for the path to the input file.
- Creates an instance of the `XmlProcessor` class with the provided input file.
- Calls the `process_xml` method to obtain the processed XML content.
- Prints the resulting plain text.

### Program Execution (`__main__`):
- Calls the `main` function if the script is executed as the main module.

## How to Use
1. Run the script.
2. Enter the path to the ZIP file containing 'memo_content.xml' when prompted.
3. The script will output the processed plain text without HTML tags.

This program is particularly useful for extracting and processing text content from XML files within ZIP archives.
