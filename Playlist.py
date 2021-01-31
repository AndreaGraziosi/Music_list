from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None
    self.__count = 0

  # Create a method called add_song that creates a Song object and adds it to the playlist. 
  # This method has one parameter called title.

  def add_song(self, title):
    #instantiate a new Song() class with title given
    new_song = Song(title) 
    new_song.set_next_song(self.__first_song) 
    #print("next reference ", new_song.get_next_song())
    self.__first_song = new_song
    #print("head ", self.__first_song)
    self.__count += 1

  #  Create a method called find_song that searches for whether a song exits in the playlist and returns its index. 
  # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current_index = 0
    current_song = self.__first_song
    while current_song.get_next_song():
      current_song = current_song.get_next_song()
      current_index += 1
      if current_song.get_title() == title:
        return current_index


  # Create a method called remove_song that removes a song from the playlist. 
  # This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    #current = self.__first_song
    # previous = None
    # while current.get_next_song() is not None:
    #   previous = current
    #   current = current.get_next_song()
    # if previous is None:
    #   self.head = current.get_next_song()
    # else:
    #   previous = current.get_next_song()
    title = str(title).title()
    song = self.__first_song
    #base condition to check to see if the song is the head.
    if title == song.get_title():
      self.__first_song = song.get_next_song()
      self.__count-= 1
      #print(self.__first_song)
      return 
    while song.get_next_song() is not None:
      next_song = song.get_next_song()
     
      if next_song.get_title() == title:
        print(next_song)
        #if songs next song is  = to the one we want to delete, set the songs, next song to next,next song
        song.set_next_song(next_song.get_next_song())
        self.__count -= 1
        break
      song = next_song



  #  Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    # counter = 0 
    # current_song = self.__first_song
    # while current_song is not None:
    #   counter = counter + 1
    #   current_song = current_song.get_next_song()
    # return counter
    return self.__count

  #  Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current = self.__first_song
    while current != None:
      print(current.get_title())
      current = current.get_next_song()

if __name__ == "__main__":
 playlist_one = Playlist()
 print("============ADD SONGS ===================")
 playlist_one.add_song("halo")
 playlist_one.add_song("Sunrise")
#  playlist_one.add_song("Tomorrow")
#  playlist_one.add_song("Mountain")
#  playlist_one.add_song("California")
#  print('=============FIND SONG ======================')
#  print(playlist_one.find_song("halo"))
#  print('===============REMOVE SONG===================')
#  print(playlist_one.remove_song("halo"))
 print('====================PLAYLIST LENTGH==========')
 print(playlist_one.length())
 
 
 playlist_one.remove_song("halo")
 print(playlist_one.length())
 
#  print('====================PRINT SONGS================')
#  print(playlist_one.print_songs())