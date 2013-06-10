# implementation of card game - Memory
import simplegui
import random

def init():
    # nice hack, right? ;))
    global deck, exposed, state, moves
    deck = [_ for _ in range(8) * 2]
    exposed = [False for _ in range(16)]
    random.shuffle(deck)
    state, moves = 0, 0
    label.set_text("Moves = "+str(moves))    
    
# define event handlers
def mouseclick(pos):
    global state, in_track1, in_track2, moves
    if state == 0:
            state = 1
            exposed[pos[0] // 50] = True
            in_track1 = pos[0] // 50
            moves += 1
    elif state == 1:
        if exposed[pos[0] // 50] == False:
            state = 2
            exposed[pos[0] // 50] = True
            in_track2 = pos[0] // 50
    else:
        if exposed[pos[0] // 50] == False:
            exposed[pos[0] // 50] = True
            if deck[in_track1] != deck[in_track2]:
                exposed[in_track1], exposed[in_track2] = False, False
            state = 1
            in_track1 = pos[0] // 50
            moves += 1
    label.set_text("Moves = "+str(moves))

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    pos_num = [20, 60]
    pos_rectangle = [25,0]
    en = 0
    for num in deck:
        canvas.draw_text(str(num), pos_num, 44, "White")
        if exposed[en] == False:
            canvas.draw_line(pos_rectangle, [pos_rectangle[0], 100], 47, "Green")
        en += 1
        pos_num[0] += 50
        pos_rectangle[0] += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

init()

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

frame.start()