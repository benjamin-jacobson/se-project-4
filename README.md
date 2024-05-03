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