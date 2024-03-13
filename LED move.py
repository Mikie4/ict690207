# Write your code here :-)
"""This example turns on the little red LED when button A is pressed."""
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3
cp.pixels.fill((0,0,0))
cp.pixels[0] = (0,25,0)

cp.adjust_touch_threshold(1000)

pos = 0
a_pressed = False
b_pressed = False
held = False
toned = False
ticks = 0
direction = 1

def move_led():
    global held
    global ticks
    global pos
    global direction
    if not held:
        ticks = ticks + 1
        if ticks == 100:
            cp.pixels[pos] = (0,0,0)
            pos = int(pos + 1 * direction) % 10
            cp.pixels[pos] = (0,25,0)
            ticks = 0


while True:
    if cp.light > 10:
        if not toned:
            cp.start_tone(440,1)
            print("toned")
            toned = True
    if cp.light <= 10:
        cp.stop_tone()
        toned = False


    #print("Light:", cp.light)
    if cp.switch:
        if cp.button_a:
            if not a_pressed:
                cp.pixels[pos] = (0,0,0)
                pos = int(pos + 1) % 10
                cp.pixels[pos] = (0,25,0)
                a_pressed = True
        else:
            a_pressed = False

        if cp.button_b:
            if not b_pressed:
                cp.pixels[pos] = (0,0,0)
                pos = int(pos - 1) % 10
                cp.pixels[pos] = (0,25,0)
                b_pressed = True
        else:
            b_pressed = False




    else:
        if cp.touch_A1:
            print(pos)
            if pos == 6:
                held = True
            else:
                move_led()
        if cp.touch_A3:
            print(pos)
            if pos == 8:
                held = True
            else:
                move_led()
        if cp.touch_A5:
            print(pos)
            if pos == 1:
                held = True
            else:
                move_led()
        if cp.touch_A7:
            print(pos)
            if pos == 3:
                held = True
            else:
                move_led()
        else:
            if not (cp.touch_A1 or cp.touch_A3 or cp.touch_A5 or cp.touch_A7):
                if held:
                    held = False
                    direction = direction * -1
            move_led()


