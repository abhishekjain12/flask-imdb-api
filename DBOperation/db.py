import logging
import traceback

import pymysql.cursors


# Open database connection
db = pymysql.connect(host="localhost",
                     user="root",
                     password="root",
                     db="movie_data",
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

# prepare a cursor object using cursor() method
cursor = db.cursor()


def select_query(sql):
    """Select Operation."""
    try:
        cursor.execute(sql)
        return cursor.fetchall()

    except Exception as e:
        logging.error("Failed select query: %s", e)
        return False


def add_record(data):
    """Insert Operation."""
    try:
        cursor.execute("INSERT INTO movie_details (id, title, released_year, rating) VALUES (%s, %s, %s, %s)",
                       (data.get_imdbid(),
                        data.get_title(),
                        data.get_release_year(),
                        data.get_imdb_rating()))
        db.commit()

        for genre in list(data.get_genre()):
            cursor.execute("INSERT INTO movie_genres (id, genre) VALUES (%s, %s)", (data.get_imdbid(), str(genre)))
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
        cursor.execute("UPDATE movie_details SET rating=%s WHERE id=%s", (data, id))
        db.commit()
        return True

    except Exception as e:
        logging.error("Failed update query: %s", e)
        db.rollback()
        return False


def update_genre(id, data):
    """Update Operation."""
    try:
        cursor.execute("DELETE FROM movie_genres WHERE id=%s", id)
        db.commit()

        for genre in data.split(","):
            cursor.execute("INSERT INTO movie_genres (id, genre) VALUES (%s, %s)", (id, str(genre)))
            db.commit()
        return True

    except Exception as e:
        logging.error("Failed update query: %s", e)
        db.rollback()
        return False
