import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'certified_copy_reader'))

from dotenv import load_dotenv
from pdf_reader import PDFReader

load_dotenv()
pdf_path = os.getenv('PDF_PATH')

pdf_reader = PDFReader(pdf_path)
text = pdf_reader.read_pdf()

print(text)