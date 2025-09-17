import curses
from player import Player
music = Player()
scr = curses.initscr()
#print("hello World!")
playbtn = "|>"
pausebtn = "||"
nxtbtn = ">>"
prvbtn = "<<"
scr.addstr( 0, 0, f"currently playing {music.title()}")
scr.addstr(1, 0 ,f"{prvbtn} {playbtn} {pausebtn} {nxtbtn}")
scr.refresh()
#scr.refresh()

