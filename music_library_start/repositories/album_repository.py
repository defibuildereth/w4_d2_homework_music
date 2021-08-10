from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    # id = results[0]
    # album.id = id
    return results

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def select(id):
    pass


def delete(id):
    pass

def select_all():
    pass

def update(album):
    pass
