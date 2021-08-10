import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Super Cool Band Yeah")
album1 = Album("Trilbies and Glasses of White Wine", "Weekend Rockstars", artist1)

artist_repository.save(artist1)
album_repository.save(album1)



# for album in album_repository.select_all():
#     print(album.__dict__)



pdb.set_trace()
