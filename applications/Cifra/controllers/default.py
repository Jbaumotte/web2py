def user():
    return dict(form=auth())

def index():
    import cifra_club

    form = SQLFORM.factory(Field('url',
                                 label=T('Insert the URL '),
                                 requires=IS_MATCH('http://www.cifraclub.com.br/', error_message='Desculpa, por enquanto, so Cifra Club')))

    if form.process().accepted:

        cifra = cifra_club.get_song(form.vars.url)
        ## cifra[0] = name; cifra[1] = nome_musica; cifra[2] = letra
        session.name = cifra[0].title().split("-")[0]
        session.banda = cifra[0].split("-")[1]
        session.nome_musica = cifra[1]
        session.letra = cifra[2].strip()
        redirect(URL('cifra'))
    return dict(form=form)


def cifra():
    response.title = "Minhas Cifras"
    response.subtitles = session.name+"-"+session.banda
    return dict()

def evernote():
    import evernote_song
    evernote_song.evernote_song(session.name, session.banda, session.letra)
    response.flash='Gravado no Evernote!'
    return ("")



def get_me_a_pdf():

    from reportlab.platypus import *
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.rl_config import defaultPageSize
    from reportlab.lib.units import inch, mm
    from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
    from reportlab.lib import colors
    from uuid import uuid4
    from cgi import escape
    import os

    title = session.name.replace("\r", "").replace("\t", "")
    heading = session.banda
    text = session.letra


    styles = getSampleStyleSheet()
    tmpfilename=os.path.join(request.folder,'private',str(uuid4()))
    doc = SimpleDocTemplate(tmpfilename)
    story = []
    story.append(Paragraph(escape(title),styles["Heading1"]))
    story.append(Paragraph(escape(heading),styles["Heading3"]))
    story.append(Preformatted(escape(text), styles["Normal"]))
    story.append(Spacer(1,2*inch))
    doc.build(story)
    data = open(tmpfilename,"rb").read()
    os.unlink(tmpfilename)
    response.headers['Content-Type']='application/pdf'
    return data