
import PyPDF2

pdf_files = ['1.pdf', '2.pdf', 'item.pdf']
merger = PyPDF2.PdfMerger()
for filename in pdf_files:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(filename)

pdfFile.close()
merger.write('merged.pdf')





