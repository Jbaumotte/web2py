from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm, mm, inch, pica
import cifra_club.py

def make_pdf(name, nome_musica, letra):
    '''
    str -> none

    Takes in a string text and creates a pdf file named file_name
    containing the file.

    >>> make_pdf("Hello world!")
    >>>
    >>>a = "Meu coracao nao sei porque, bate feliz quando te ve"
    >>>make_pdf(a)
    >>>

    '''
    
    pdf = Canvas(nome_musica+".pdf")
 
    pdf.setFillColorRGB(1, 0, 0)
    pdf.setStrokeColorRGB(1, 0, 0)
    
    ## An important thing to note here is that when specifying coordinates,the 
    ## origin  is in the lower left hand corner of the page, rather than the
    ## top left. The default unit of measurement is a point, equal to one
    ## seventy-second of an inch.
    pdf.setFont("Courier", 45)
    pdf.drawString(cm * 5, cm * 25, name)
    
    pdf.setFont("Courier", 30)
    text = pdf.beginText(cm * 5, cm * 20)
 
    for each in range(letra.count("\n")):
        text.textLine(letra.split("\n")[each])

    pdf.drawText(text)
    

    ## Close the page. The showPage method closes the current page.
    ## Any further drawing will occur on the next page

    pdf.showPage()

    ## The ReportLab Toolkit saves our page
    pdf.save()

def cifra_to_pdf(url):
    '''
    str -> none

    Takes a string URL from a music from cifraclub.com.br and
    returns a pdf file, named after the music

    >>>cifra_to_pdf(a)
    >>>

    '''

    cifra = get_song(url)

    make_pdf(cifra[0], cifra[1], cifra[2])


a = "http://www.cifraclub.com.br/banda-eva/miragem/"
