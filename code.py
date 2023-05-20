import time
import board
import touchio
from adafruit_circuitplayground import cp
from adafruit_circuitplayground.bluefruit import cpb

cpb.pixels.brightness = 0.01


bpm = 120

# Make the input capacitive touchpads
cap_pins = (board.A1, board.A2, board.A3, board.A4, board.A5, board.A6, board.TX)

touch_pad = []
for i in range(7):
    touch_pad.append(touchio.TouchIn(cap_pins[i]))

pixels_div = [(5, 7), (7, 9), (8, 10), (0, 2), (1, 3), (2, 4), (3, 5)]
# The seven files assigned to the touchpads
audiofiles = [
    "audio/miau.mp3",
    "audio/woof.mp3",
    "audio/meah.mp3",
    "audio/moo.mp3",
    "audio/psst.mp3",
    "audio/miau.mp3",
    "audio/miau.mp3",
]


def play_file(filename, i):
    print("playing file: " + filename + " from touchPad: " + str(i))
    cpb.pixels[pixels_div[i][0] : pixels_div[i][1]] = [(255, 0, 0)] * 2
    cp.play_mp3(filename)
    time.sleep(bpm / 960)  # Sixteenth note delay


while True:
    for i in range(7):
        cpb.pixels.fill((0, 0, 0))
        if touch_pad[i].value:
            play_file(audiofiles[i], i)
