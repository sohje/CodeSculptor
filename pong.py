# Implementation of classic arcade game Pong
import simplegui
import random
""" initialize globals - pos and vel encode vertical info for paddles """
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(120, 240)/60,random.randrange(60, 180)/60]
    if right:
        ball_vel[1] = -ball_vel[1]
    elif not right:
        ball_vel[1] = -ball_vel[1]
        ball_vel[0] = -ball_vel[0]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1, score2 = 0, 0
    paddle1_pos,paddle2_pos = 200, 200#[160, 240], [160, 240] # center...
    paddle1_vel,paddle2_vel = 0, 0
    ball_init(True)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    """ update paddle's vertical position, keep paddle on the screen """
    if HALF_PAD_HEIGHT < paddle1_pos+paddle1_vel < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if HALF_PAD_HEIGHT < paddle2_pos+paddle2_vel < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
        
    """ draw mid line and gutters """
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    """ draw paddles """
    c.draw_line([WIDTH - HALF_PAD_WIDTH,paddle2_pos-40],[WIDTH - HALF_PAD_WIDTH, paddle2_pos+40], PAD_WIDTH, "White")
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos-40],[HALF_PAD_WIDTH, paddle1_pos+40], PAD_WIDTH, "White")
    
    """ update ball """
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= (HEIGHT-1-BALL_RADIUS)):
        ball_vel[1] = -ball_vel[1]
    # if paddle meet ball
    elif (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS) and (paddle1_pos - 40 <= ball_pos[1] <= paddle1_pos + 40)) \
    or (ball_pos[0] >= (WIDTH -1 - PAD_WIDTH - BALL_RADIUS) and (paddle2_pos - 40 <= ball_pos[1] <= paddle2_pos + 40)):
        ball_vel[0] = -(ball_vel[0] + ball_vel[0] * 0.1)
    elif (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)):
        score2 += 1
        ball_init(True)
    elif (ball_pos[0] >= (WIDTH -1 - BALL_RADIUS- PAD_WIDTH)):
        score1 += 1
        ball_init(False)
        
    """ draw ball and scores """
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White") 
    c.draw_text(str(score2), (WIDTH / 2 + 15, 50), 48, "White")    
    c.draw_text(str(score1), (WIDTH / 2 - 50, 50), 48, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 4
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 4
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 4
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['s'] or key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game, 100)

new_game()
# start frame
frame.start()