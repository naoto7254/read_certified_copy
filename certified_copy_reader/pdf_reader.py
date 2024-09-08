import PyPDF2

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_pdf(self):
        with open(self.file_path, 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)
            num_pages = reader.getNumPages()
            text = ''.join([reader.getPage(i).extractText() for i in range(num_pages)])
        return text