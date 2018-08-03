from DBOperation.db import select_query

res = select_query("SELECT genre FROM Movie_Genres WHERE id='{0}'".format('tt0068646'))
print(res)
print(list(genre.values() for genre in res))
