##
## A python API script that fetchs the lyrics and tabs from a given
## song from cifra.com.br web site and writes the fetched information
## in a created txt file, inside a folder cifras, that will be created if
## it does not exist.
## Uses Beatiful Soup to parse the website
##

##import library to do http requests:
import urllib

##import beautiful soup parser:
from bs4 import BeautifulSoup

## import os to create the folder if it does not exist
import os

## import module created for evernote
import evernote_song

def get_song(url):

    ## Testing address
    #url = "https://www.cifraclub.com.br/nayambing-blues/trem-do-amor/"

    ##download the file:    
    html = urllib.urlopen(url)

    ##convert to string:
    page = html.read()

    ##close file because we dont need it anymore:
    html.close()

    ##parse the file downloaded
    soup = BeautifulSoup(page)

    ## Isolating the lyrics and tabs section
    musica = soup.find(id="cifra_cnt")
    nome_musica = soup.find(id="ai_musica")

    ## Song title name and lyrics with tabs
    name = remove_cifra_club(soup.title.string).encode('utf-8')
    letra = musica.get_text().encode('utf-8')

    ## Creating file name, with the name of the music,
    ## and calling subs_name function to replace white spaces
    ## with underline
    nome_musica = subs_name(nome_musica.get_text())

    return name, nome_musica, letra


def salvar_txt(url):

    ## Calling function to get song
    ## cifra[0] = name; cifra[1] = nome_musica; cifra[2] = letra
    cifra = get_song(url)

    ## Checking if folder exists, if not creating
    directory = './Cifras'
    if not os.path.exists(directory):
        os.makedirs(directory)

    ##creating a file txt and writing the song in it
    arquivo = directory+"/"+cifra[1]+".txt"
    f=open(arquivo,'w+')
    f.write(cifra[0] + cifra[2])
    f.close()

    ## Printing the song name and the isolated
    ##section without the html references
    ##(used as I was developing, removed after started printing into txt)
    #print(name) 
    #print(letra)

    ##Checking if file was created
    if os.path.exists(arquivo):
        print ("\n"+cifra[1]+".txt foi criado!\n")
    else:
        print("\n Aconteceu alguma coisa! Nao deu certo")


def ever_note(url):

    cifra = get_song(url)

    ## Calling evernote module
    evernote_song.evernote_song(cifra[0], cifra[2])

    return ("Saved on evernote")

def subs_name(name):
    return name.replace(" ", "_")

def remove_cifra_club(name):

    name = name.split("(")[0]
    name = name.split("|")[1]

    return name
