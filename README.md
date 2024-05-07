# Readme

# Initial Terminal History Dump Showcasing Pure Lazizness

# Overall Project and Backend Setup
cd Development/code/phase-4/
 2002  mkdir project-4
 2003  cd $_
 2004  pipenv install Flask gunicorn psycopg2-binary Flask-SQLAlchemy Flask-Migrate SQLAlchemy-Serializer Flask-RESTful
 2005  ls
 2006  pipenv requirements > requirements.txt
 2007  ls
 2008  cat requirements.txt
 2009  python --version
 2010  mkdir server
 2011  touch server/app.py
 2012  code .
 2013  touch server/models.py
 2014  touch README.md

 # Client setup
 At root: npx create-react-app client

 Starting the local server at root: npm start --prefix client

 - now with honco pip install honcho
 to run locally honcho start -f Procfile.dev

 - To run on build production version of app (npm run build --prefix client)
 gunicorn --chdir server app:app

 # Resources and Reference Materials
 - https://learning.flatironschool.com/courses/6551/pages/deploying-a-flask-api-to-render?module_item_id=558508

 - https://github.com/learn-co-curriculum/python-p4-deploying-flask-react-app-to-render


 Updating python pipenv (can't just pip install, need pipenv install)
  2155  pipenv install python-dotenv
 2156  pipenv requirements > requirements.txt

 # Nested routes 
 https://github.com/learn-co-curriculum/react-hooks-react-router-nested-routes-v6