import datetime
import logging

from flask import Flask, jsonify, request

# from DBOperation.db import select_query, add_record, update_rating, update_genre
from DBOperation import logs
from DBOperation.db_sqlite3 import select_query, add_record, update_rating, update_genre
from OMDb.api import OMDB

logs.initialize_logger("movie")

app = Flask(__name__)

api_key = "73d0cdbe"


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


@app.route('/')
def index():
    logging.debug("index")
    return jsonify({'message': 'Welcome To Movie Data API'})


# endpoint to update
@app.route("/movie/<id>", methods=["PATCH"])
def update_data(id):
    key = request.form['key']
    value = request.form['value']

    db_result = {'data': select_query("SELECT * FROM Movie_Details WHERE id='{0}' limit 1".format(id))}
    if not db_result:
        return jsonify({'message': 'No data found!'}), 404

    if key != "rating" and key != "genre" or value == "":
        return jsonify({'message': 'Bad Input!'}), 400

    if key == "rating":
        if not isfloat(value):
            return jsonify({'message': 'Bad Input!'}), 400
        update_rating(id, value)

    if key == "genre":
        update_genre(id, value)

    db_result = {'data': select_query("SELECT * FROM Movie_Details WHERE id='{0}' limit 1".format(id))}
    genre_result = select_query("SELECT genre FROM Movie_Genres WHERE id='{0}'".format(id))
    db_result['data'][0]['genres'] = list(genre['genre'] for genre in genre_result)
    db_result['time'] = datetime.datetime.now()
    return jsonify(db_result)


# endpoint to get detail by title
@app.route("/movie/title", methods=["GET"])
def movie_detail_by_title():
    title = request.args['title']
    db_result = {'data': select_query("SELECT * FROM Movie_Details WHERE title LIKE'{0}' limit 1".format(title))}
    if not db_result['data']:
        obj = OMDB(apikey=api_key)
        obj.get(title=title)
        add_record(obj)
        db_result = {'data': select_query("SELECT * FROM Movie_Details WHERE title LIKE'{0}' limit 1".format(title))}
        if not db_result:
            return jsonify({'message': 'No data found!'}), 404

    print(db_result)
    genre_result = select_query("SELECT genre FROM Movie_Genres WHERE id='{0}'".format(db_result['data'][0]['id']))
    print(genre_result)
    db_result['data'][0]['genres'] = list(genre['genre'] for genre in genre_result)
    db_result['time'] = datetime.datetime.now()
    return jsonify(db_result)


# endpoint to get detail by id
@app.route("/movie/<id>", methods=["GET"])
def movie_detail_by_id(id):
    db_result = {'data': select_query("SELECT * FROM Movie_Details WHERE id='{0}' limit 1".format(id))}
    if not db_result['data']:
        return jsonify({'message': 'No data found in local!'}), 404

    genre_result = select_query("SELECT genre FROM Movie_Genres WHERE id='{0}'".format(id))
    db_result['data'][0]['genres'] = list(genre['genre'] for genre in genre_result)
    db_result['time'] = datetime.datetime.now()
    return jsonify(db_result)


# endpoint to get movies by filter
@app.route("/movie/filter/", methods=["GET"])
def movies_by_filter():
    logging.debug("filter")
    action = request.args['action']

    if action == "year":
        year = request.args['value']
        db_result = {'data': select_query("SELECT id, title, released_year FROM Movie_Details WHERE released_year={0}"
                                          .format(year))}
        if not db_result:
            return jsonify({'message': 'No data found in local!'}), 404

    elif action == "year_range":
        start_year = request.args['start_year']
        end_year = request.args['end_year']
        db_result = {'data': select_query("SELECT id, title, released_year FROM Movie_Details WHERE released_year "
                                          "BETWEEN {0} AND {1}".format(start_year, end_year))}
        if not db_result:
            return jsonify({'message': 'No data found in local!'}), 404

    elif action == "higher_rating":
        value = request.args['value']
        db_result = {'data': select_query("SELECT id, title, rating FROM Movie_Details WHERE rating > {0}"
                                          .format(value))}
        if not db_result:
            return jsonify({'message': 'No data found in local!'}), 404

    elif action == "lower_rating":
        value = request.args['value']
        db_result = {'data': select_query("SELECT id, title, rating FROM Movie_Details WHERE rating < {0}"
                                          .format(value))}
        if not db_result:
            return jsonify({'message': 'No data found in local!'}), 404

    elif action == "genre":
        value = request.args['value']
        db_result = {'data': select_query("SELECT id FROM Movie_Genres WHERE genre = '{0}'".format(value))}
        if not db_result:
            return jsonify({'message': 'No data found in local!'}), 404

    else:
        db_result = {'message': 'No filter selected!'}

    db_result['time'] = datetime.datetime.now()
    return jsonify(db_result)


if __name__ == '__main__':
    logging.debug("App starts")
    app.run(host='0.0.0.0')
