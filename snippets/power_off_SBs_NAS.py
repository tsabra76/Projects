__author__ = 'Tarek'


from pylms.server import Server
from pylms.player import Player

def Play():
      sc = Server(hostname="192.168.0.25", port='9090')
      sc.connect()

      sqPCroom = sc.get_player("00:04:20:2a:70:77") #computer room SB
      sqBedroom = sc.get_player("00:04:20:2a:6f:ac") #bedroom SB	


      if sqPCroom.get_power_state() == True:
          sqPCroom.set_power_state(False)
      
      if sqBedroom.get_power_state() == True:
          sqBedroom.set_power_state(False)
          

def main():
      Play()



if __name__ == "__main__": main()



