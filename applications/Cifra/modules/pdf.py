def make_pdf(name, nome_musica, letra):
    '''
    str -> none

    Takes in a string text and creates a pdf file named file_name
    containing the file.

    >>> make_pdf("Hello world!")

    '''
    from reportlab.platypus import *
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.rl_config import defaultPageSize
    from reportlab.lib.units import inch, mm
    from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
    from reportlab.lib import colors
    from uuid import uuid4
    from cgi import escape
    import os

    letra = letra.replace("\r", "").replace("\t", "")


    name = "Hello"
    styles = getSampleStyleSheet()
    tmpfilename=os.path.join(request.folder,'private',str(uuid4()))
    doc = SimpleDocTemplate(tmpfilename)
    story = []
    story.append(Paragraph(escape(title),styles["Title"]))
    story.append(Paragraph(escape(heading),styles["Heading2"]))
    story.append(Paragraph(escape(text),styles["Normal"]))
    story.append(Spacer(1,2*inch))
    doc.build(story)
    data = open(tmpfilename,"rb").read()
    os.unlink(tmpfilename)
    response.headers['Content-Type']='application/pdf'
    return data
