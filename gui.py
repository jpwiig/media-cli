#import curses
from player import Player
import traceback as t 
music = Player()
#print("hello World!")
try:
    while True: 

        playbtn = "|>"
        pausebtn = "||"
        nxtbtn = ">>"
        prvbtn = "<<"
        shuffle = "s"
        quit = "q"
        seek = "seek"

        #scr.addstr( 0, 0, f"currently playing {music.title()}")
    
        print(f"currently playing: {music.title()} by {music.artist()}")
        userInput = input(f"{prvbtn} {playbtn} {pausebtn} {nxtbtn}, shuffle: {shuffle}, quit: {quit}, seek:  {seek}\n")


        if userInput == "q" : 
           # curses.endwin()
            exit()
        if userInput == "||":
            music.pause()
            continue
        if userInput == "|>":
            music.play()
            continue
        if userInput == str(">>"): 
            music.next()
            continue
        if userInput == "<<":
            music.prev()
            continue

except Exception as e:
    #curses.endwin()
    print(f"{t.format_exc()}")
    exit()
   
