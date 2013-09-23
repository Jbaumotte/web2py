#!/bin/bash

read -p "Choose a text to commit?" text
virtualenv venv --distribute
source venv/bin/activate
pip freeze > requirements.txt
echo "web: python web2py.py -a 'felipe' -i 0.0.0.0 -p $PORT" > Procfile
git init
git add .
git add Procfile
git commit -a -m "$text"
heroku create
git push heroku master
heroku addons:add heroku-postgresql:dev
heroku scale web=1
heroku open
