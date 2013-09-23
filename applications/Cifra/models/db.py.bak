import os
#from gluon.contrib.heroku import get_db
# Conecta com a sqlite
#db = get_db(name=None, pool_size=10)
if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    try: db = DAL(os.environ.get('DATABASE_URL'))
    except: db = DAL('sqlite://storage.sqlite')

# Tabela que guarda qual música o usuário buscou
db.define_table('cadastro',
   Field('login'),
   Field('Music', 'text'))

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)
