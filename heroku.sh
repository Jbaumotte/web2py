#!/bin/bash

virtualenv venv --distribute
source venv/bin/activate
pip freeze > requirements.txt
echo "web: python web2py.py -a 'felipe' -i 0.0.0.0 -p $PORT" > Procfile
git add .
git add Procfile
git commit -a -m "Submit"
git push heroku master
heroku addons:add heroku-postgresql:dev
heroku scale web=1
heroku open
