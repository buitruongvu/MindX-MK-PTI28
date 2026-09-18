import json


class AnimeItem:
  def __init__(self, id, title, release_date, image = None, rating = None, link = None):
    self.id = id
    self.title = title
    self.release_date = release_date
    self.image = image
    self.rating = rating
    self.link = link
  
anime1 = AnimeItem(1, "One Piece", "01/01/2001", None, 0, None)  
anime2 = AnimeItem(2, "Conan", "01/01/1999", None, 0, None)  
anime3 = AnimeItem(3, "Naruto", "01/01/1980")  

anime = [anime1, anime2, anime3]

animes = [ane.__dict__ for ane in anime]
with open("data.json", "w") as file:
  json.dump(animes, file, indent=4)