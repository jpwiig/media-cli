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
        timeplayed = "tp"
        timeInSong = music.timePlayed()
        #scr.addstr( 0, 0, f"currently playing {music.title()}")
     
        
        print(f"\033[92;1;52mcurrently playing:\033[0m \033[92;1;3m{music.title()} by {music.artist()}\033[0m")
        while True: 
            print(f"{timeInSong}", end="\r")
            continue

        userInput = input(f"\033[92;1;6m{prvbtn} {playbtn} {pausebtn} {nxtbtn}\033[0m \n\033[92;1;6mshuffle: {shuffle}, quit: {quit}, Time played:  {timeplayed}\033[0m\n")

        
        if userInput == "q" : 
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
        if userInput == timeplayed:
            print(music.timePlayed())
            continue
        
    
except Exception as e:
    print(f"{t.format_exc()}")
    exit()
   
