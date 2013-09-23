#
# Copied from Evernote API demo script that creates a note with
# the song title as note title and song lyrics as note body
#

import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

def evernote_song(title, band, song):

    # Authenticate with a developer token 
    auth_token = "S=s1:U=7631e:E=14876be762a:C=1411f0d4a2d:P=1cd:A=en-devtoken:V=2:H=905f02804c904b17ff6446a221343374"

    if auth_token == "your developer token":
        print "Please fill in your developer token"
        print "To get a developer token, visit " \
            "https://sandbox.evernote.com/api/DeveloperToken.action"
        exit(1)

    # Initial development is performed on our sandbox server. To use the production
    # service, change sandbox=False and replace your
    client = EvernoteClient(token=auth_token, sandbox=True)

    user_store = client.get_user_store()

    version_ok = user_store.checkVersion(
        "Evernote EDAMTest (Python)",
        UserStoreConstants.EDAM_VERSION_MAJOR,
        UserStoreConstants.EDAM_VERSION_MINOR
    )

    note_store = client.get_note_store()

    # To create a new note, simply create a new Note object and fill in
    # attributes such as the note's title.
    title = str(title)
    note = Types.Note()
    note.title = title.strip()+' - '+band.strip()

    ## The content of an Evernote note is represented using Evernote Markup Language
    ## (ENML). The full ENML specification can be found in the Evernote API Overview
    ## at http://dev.evernote.com/documentation/cloud/chapters/ENML.php
    note.content = '<?xml version="1.0" encoding="UTF-8"?>'
    note.content += '<!DOCTYPE en-note SYSTEM ' \
        '"http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>'
    note.content += title+"<br></br>"
    note.content += band+"<br></br>"
    note.content += song.replace("\n", "\n <br></br>")
    note.content += '</en-note>'

    # Finally, send the new note to Evernote using the createNote method
    # The new Note object that is returned will contain server-generated
    # attributes such as the new note's unique GUID.
    created_note = note_store.createNote(note)
