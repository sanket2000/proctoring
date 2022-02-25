import sounddevice as sd
import numpy as np

# PROCCESSED INPUTS
VOLUME_NORM = 0
x = 0
y = 0

# SOUND THRESHOLD
PER_SEC_UPDATE = 38
SUS_FREQ = 2
SOUND_THRESHOLD = 20

FRAMES_COUNT = int(PER_SEC_UPDATE/SUS_FREQ)
AMP_LIST = list([0]*FRAMES_COUNT)
SUS_COUNT = 0
count = 0

def print_sound(indata, outdata, frames, time, status):
    avg_amp = 0
    global VOLUME_NORM, SUS_COUNT, count, SOUND_THRESHOLD
    vnorm = int(np.linalg.norm(indata)*10)
    AMP_LIST.append(vnorm)
    count += 1
    AMP_LIST.pop(0)
    if count == FRAMES_COUNT:
        avg_amp = sum(AMP_LIST)/FRAMES_COUNT
        VOLUME_NORM = avg_amp
        if SUS_COUNT >= 2:
            print("!!!!!!!!!!!! FBI OPEN UP !!!!!!!!!!!!")
            SUS_COUNT = 0
        if avg_amp > SOUND_THRESHOLD:
            SUS_COUNT += 1
            print("Sus...", SUS_COUNT)
        else:
            SUS_COUNT = 0
        count = 0

def sound():
    with sd.InputStream(callback=print_sound):
        sd.sleep(-1)

def sound_analysis():
    global AMP_LIST, FRAMES_COUNT, VOLUME_NORM
    while True:
        AMP_LIST.append(VOLUME_NORM)
        AMP_LIST.pop(0)

        avg_amp = sum(AMP_LIST)/FRAMES_COUNT

        if avg_amp > 10:
            print("Sus...")

if __name__ == "__main__":
    sound()