# IMDb API using Flask
A simple demonstration of IMDb API using Flask.

## Installation

##### Requirements:
* Python 3
* Python PIP 3
* MySQL/SQLite3

For installing python package dependencies, run the following command:
```shell script
pip3 install -r requirements.txt
```

##### Setup SQLite 3 database
No change needed.


##### Setup MySQL database
Project contains `pandas-flask.sql` sql file. Import this file. Change the database credentials located in `app.py`  file.

```python
db = pymysql.connect(host="localhost",
                     user="root",
                     password="root",
                     db="movie_data",
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
```

Uncomment line 6 in `app.py` and comment line 8
```python
from DBOperation.db import select_query, add_record, update_rating, update_genre
...
# from DBOperation.db_sqlite3 import select_query, add_record, update_rating, update_genre
```

##### OMDb API key
Register for API key here: [OMDb](http://www.omdbapi.com/apikey.aspx)

Set API key on line 15 in `app.py`
```python
api_key = "API_KEY"
```


## Run the Project 
```shell script
python3 wsgi.py
```

## Deployment
Follow the following link: 
[Link](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)
