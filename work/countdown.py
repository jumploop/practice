#! python3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 60

while timeLeft > 0:
    print('\r', timeLeft, end='', flush=True)
    time.sleep(1)
    timeLeft = timeLeft - 1
print('Break time is over!')
# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)
