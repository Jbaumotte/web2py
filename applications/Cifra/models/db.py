#import os
#if not request.env.web2py_runtime_gae:
#    try: db = DAL(os.environ.get('DATABASE_URL'))
#    except: db = DAL('postgres://username:password@localhost/test')
#from gluon.tools import Auth
#auth = Auth(db)
#auth.define_tables(username=True)
##################################################################

# -*- coding: utf-8 -*-
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    #from gluon.contrib.heroku import *
    #try: db = DAL(os.environ.get('DATABASE_URL'))
    #except: db = get_db(name=None, pool_size=10)
    db = DAL('sqlite://storage.db')
else:
    db = DAL('google:datastore')
    session.connect(request, response, db=db)


from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)

db.define_table('musica',
   Field('user'),
   Field('musica'),
   Field('banda'),
   Field('created_on', 'datetime', default=request.now),
   Field('editado', default='false'))

db.musica.musica.requires=IS_NOT_IN_DB(db(db.musica.user==request.vars.user), 'musica.musica')
