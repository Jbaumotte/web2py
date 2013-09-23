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
    response.title = session.name
    response.subtitles = session.banda
    return dict()

def evernote():
    import evernote_song
    evernote_song.evernote_song(session.name, session.banda, session.letra)
    response.flash='Gravado no Evernote!'
    return ("")

def to_pdf():
    import pdf
    pdf.make_pdf(session.name, nome_arquivo, session.letra)
    response.flash='PDF Gravado!'
    return ("")
