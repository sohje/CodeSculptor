# "Stopwatch: The Game"
import simplegui
timer_active = False
stopwatch_time = 0
stop_success = 0
stop_total = 0

def convert(time):
    global d_str
    a_str = time // 600
    if a_str > 60:
        reset_sw()
        print "Get some rest, please!"
    b_str = time // 10 % 60 // 10
    c_str = time // 10 % 60 % 10
    d_str = time % 10
    return str(a_str) + ':' + str(b_str) + str(c_str) + '.' + str(d_str)

def reflex():
    global stop_success, stop_total
    return str(stop_success) + '/' + str(stop_total)

def start_sw():
    global timer_active
    timer.start()
    timer_active = True

def stop_sw():
    global d_str, stop_success, stop_total, timer_active
    timer.stop()
    if timer_active:
        stop_total += 1
        if d_str == 0:
            stop_success += 1
    timer_active = False


def reset_sw():
    global stopwatch_time, stop_success, stop_total
    timer.stop()
    stopwatch_time = 0
    stop_success = 0
    stop_total = 0
    
def timer_sw():
    global stopwatch_time
    stopwatch_time += 1
        
def draw(canvas):
    canvas.draw_text(convert(stopwatch_time), [75,170], 48, "White")
    canvas.draw_text(reflex(), [250,25], 24, "Blue")
    
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)
frame.add_button("Start", start_sw, 100)
frame.add_button("Stop", stop_sw, 100)
frame.add_button("Reset", reset_sw, 100)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, timer_sw)
frame.start()