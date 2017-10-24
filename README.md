# Fitness Tracker
project for study purposes

### Requirements
- npm 5.4.2
- python 3.4
- webpack 3.0.0
- react 0.16.0

### Install
Create virtualenv (recommended) and run:  
`pip install -r requirements.txt`

Create file `config.py` and fill it like in the example `configExample.py`

Run migrations:  
`python manage.py db migrate`  
`python manage.py db upgrade`

Bundle js:  
`npm run build`

### Usage 
`python manage.py runserver`
