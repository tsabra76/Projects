__author__ = 'Tarek'

from pylms.server import Server
from pylms.player import Player

def Play():
      sc = Server(hostname="192.168.0.25", port='9090')
      sc.connect()

      sqLVroom = sc.get_player("00:04:20:2a:70:77") #computer room SB
      sqBedroom = sc.get_player("00:04:20:2a:6f:ac") #bedroom SB


      if sqLVroom.get_power_state() == True:
          sqLVroom.play()
      else:
          sqLVroom.set_power_state(True)
          sqLVroom.play()

      if sqBedroom.get_power_state() == True:
          sqBedroom.play()
      else:
          sqBedroom.set_power_state(True)
          sqBedroom.play()
      sqBedroom.playlist_clear()
#      sqBedroom.playlist_add('pandora://110990368869609075.mp3') # Pandora 80s
      sqBedroom.playlist_add('pandora://586054090140053107.mp3') # Pandora Classics and Indy
#      sqLVroom.playlist_add('pandora://1901820254732316275.mp3') # Pandora Dethklok radio
      sqLVroom.play()
      

   




def main():
	Play()	

if __name__ == "__main__": main()




