# Write a Playlist class that stores a name and an array of songs with methods to add a song, remove a song, shuffle the songs into a random order, and display all the songs.
class Playlist
  attr_writer :name


  def initialize
    @song_array = []
  end

  def add_song(song)
    @song_array << song
  end

  def remove_song(song)
    @song_array.delete(song)
  end

  def shuffle_songs
    new_array = []
    temp_array = @song_array.dup
    while 0 < temp_array.length
      song_i = rand(temp_array.length)
      new_array << temp_array.delete_at(song_i)
    end
    new_array
  end

  def display_songs
    puts @song_array
  end
end

playlist = Playlist.new

playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")
pp playlist
pp playlist.shuffle_songs
playlist.display_songs
playlist.remove_song("Song B")
pp playlist