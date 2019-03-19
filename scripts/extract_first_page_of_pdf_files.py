import os
import PyPDF2


papers = [x for x in os.listdir() if x.endswith('pdf')]

if not os.path.exists('first_pages'):
    print('create')
    os.mkdir('first_pages')

for paper in papers:
    try:
        with open(paper, 'rb') as f:
            print('extract {} ...'.format(paper))
            pdf_reader = PyPDF2.PdfFileReader(f)
            first_page = pdf_reader.getPage(0)
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(first_page)
            pdf_writer.write(open(os.path.join("first_pages", paper), 'wb'))
    except Exception as err:
        print(err)
            
            
input('Finished...press any key to exit.')
