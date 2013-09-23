# -*- coding: utf-8 -*-

import os
#from gluon.contrib.heroku import get_db
#db = get_db(name=None, pool_size=10)
if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    try: db = DAL(os.environ.get('DATABASE_URL'))
    except: db = DAL('sqlite://storage.sqlite')

db.define_table('image',
   Field('title', unique=True),
   Field('file', 'upload'),
   format = '%(title)s')

db.define_table('post',
   Field('image_id', 'reference image'),
   Field('author'),
   Field('email'),
   Field('body', 'text'))

db.image.title.requires = IS_NOT_IN_DB(db, db.image.title)
db.post.image_id.requires = IS_IN_DB(db, db.image.id, '%(title)s')
db.post.author.requires = IS_NOT_EMPTY()
db.post.email.requires = IS_EMAIL()
db.post.body.requires = IS_NOT_EMPTY()

db.post.image_id.writable = db.post.image_id.readable = False

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)
