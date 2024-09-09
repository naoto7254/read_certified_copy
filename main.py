import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'certified_copy_reader'))

from dotenv import load_dotenv
from pdf_reader import PDFReader
from text_processor import TextProcessor
import certified_copy_reader.utilities as utilities


load_dotenv()
pdf_path = os.getenv('PDF_PATH')

pdf_reader = PDFReader(pdf_path)
text = pdf_reader.read_pdf()

text_processor = TextProcessor(text)
cleaned_text = text_processor.clean_text()
text_list = text_processor.to_list(cleaned_text)
text_processor.remove_value_from_array(text_list, '')

print(text_list)