import logging
import os
import traceback
import sqlite3


module_directory = os.path.dirname(__file__)
db = sqlite3.connect(module_directory + '/../movie_data.db')


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def select_query(sql):
    """Select Operation."""
    try:
        db.row_factory = dict_factory
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print(sql)
        return result

    except Exception as e:
        logging.error("Failed select query: %s", e)
        return False


def add_record(data):
    """Insert Operation."""
    try:
        db.execute("INSERT INTO movie_details (id, title, released_year, rating) VALUES (?, ?, ?, ?)",
                       (data.get_imdbid(),
                        data.get_title(),
                        data.get_release_year(),
                        data.get_imdb_rating()))
        db.commit()

        for genre in list(data.get_genre()):
            db.execute("INSERT INTO movie_genres (id, genre) VALUES (?, ?)", (data.get_imdbid(), str(genre)))
            db.commit()

        return True

    except Exception as e:
        traceback.print_exc()
        logging.error("Failed insert query: %s", e)
        db.rollback()
        return False


def update_rating(id, data):
    """Update Operation."""
    try:
        db.execute("UPDATE movie_details SET rating=? WHERE id=?", (data, id))
        db.commit()
        return True

    except Exception as e:
        logging.error("Failed update query: %s", e)
        db.rollback()
        return False


def update_genre(id, data):
    """Update Operation."""
    try:
        db.execute("DELETE FROM movie_genres WHERE id=?", id)
        db.commit()

        for genre in data.split(","):
            db.execute("INSERT INTO movie_genres (id, genre) VALUES (?, ?)", (id, str(genre)))
            db.commit()
        return True

    except Exception as e:
        logging.error("Failed update query: %s", e)
        db.rollback()
        return False
