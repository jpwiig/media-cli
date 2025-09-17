import dbus
import math
#from . import Track
class Track: 

     def __init__(self, *args, title, artist, album, length, id):
        self.title = str(title)
        self.artist = str(artist)
        self.album = str(album)
        self.length = str(length)
        self.id = str(id)
class Player: 
    def __init__(self):
      self.bus  = dbus.SessionBus()
      self.spotify = self.bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
      self.spotifyInterface = dbus.Interface(self.spotify, dbus_interface="org.mpris.MediaPlayer2.Player")
      self.spotifyProps = dbus.Interface( self.spotify, dbus_interface="org.freedesktop.DBus.Properties")


    def __repr__(self):
        return f"Spotify(track={repr(self.track)},state={self.state})"

    def _get_all_props(self) -> dbus.Dictionary:
       return self.spotifyProps.GetAll("org.mpris.MediaPlayer2.Player")
    def play(self):
       
       print(f"starting: {self.track().title} by {self.track().artist} with a length of {self.microsectolength()} minutes")
       #self.microsectolength()
       self.spotifyInterface.Play()

    def pause(self):
       print("pause")
       self.spotifyInterface.PlayPause()
    def next(self):
       self.spotifyInterface.Next()
   #todo: fix minutes convertion.
    def microsectolength(self): 
       seconds = int(self.track().length) // 1000000 
       minutes = seconds // 60
       rest = seconds % 60
       formatted = f"{minutes}:{rest:02d}"
       return formatted
    def title(self):
       return self.track().title()
    

    def track(self) -> Track:
       meta = self._get_all_props()["Metadata"]
       return Track ( title=meta['xesam:title'], artist=meta['xesam:artist'][0], album=meta['xesam:album'],length=meta['mpris:length'],id=['xesam:id'] )
