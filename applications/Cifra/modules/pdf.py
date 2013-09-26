#!/usr/bin/env python
# coding: utf8
from gluon import *
def make_pdf(name, nome_musica, letra):
    '''
    str -> none

    Takes in a string text and creates a pdf file named file_name
    containing the file.

    >>> make_pdf("Hello world!")

    '''
    from gluon.contrib.pyfpdf import FPDF, HTMLMixin

    # create a custom class with the required functionalities
    class MyFPDF(FPDF, HTMLMixin):
        def header(self): 
            "hook to draw custom page header (logo and title)"
            logo=os.path.join(request.env.web2py_path,"gluon","contrib","pyfpdf","tutorial","logo_pb.png")
            self.image(logo,10,8,33)
            self.set_font('Arial','B',15)
            self.cell(65) # padding
            self.cell(60,10,response.title,1,0,'C')
            self.ln(20)

        def footer(self):
            "hook to draw custom page footer (printing page numbers)"
            self.set_y(-15)
            self.set_font('Arial','I',8)
            txt = 'Page %s of %s' % (self.page_no(), self.alias_nb_pages())
            self.cell(0,10,txt,0,0,'C')

        response.title = name
        pdf=MyFPDF()
        # create a page and serialize/render HTML objects
        pdf.add_page()
        pdf.write_html(str(XML(letra, sanitize=False)))

        # prepare PDF to download:
        response.headers['Content-Type']='application/pdf'
        return pdf.output(dest='S')
