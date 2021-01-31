class Song:

  def __init__(self, title):
      self.__title = str(title).title()
      self.__next_song = None
  
  #Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return f"{self.__title}"


  #  Using the __repr__ dunder method, return a string formatted as the following:
  # 'Song Title -> Next Song Title'
  def __repr__(self):
    return f'{self.__title} -> {self.__next_song}'


  #Create a getter method for the title attribute, called get_title
  def get_title(self):
    return self.__title
  
  
  # Create a setter method for the next_song attribute, called set_title. 
  # Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    self.__title = str(title).title()


  #  Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self.__next_song


  #  Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    self.__next_song = next_title


  
if __name__ == "__main__":
    
  song_one = Song("Lemon Grove Avenue")
  print('=========SONG ONE============')
  print(str(song_one))
  # print('=================GET NEXT==============')
  # print(song_one.get_next_song())
  # print('===================SET NEXT SONG==============')
  # print(song_one.set_next_song('California'))
  # print('=============STR METHOD================')
  # print(song_one.__str__())
  # print('===========REPR===================')
  # print(song_one.__repr__())