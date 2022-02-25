import sounddevice as sd
import numpy as np
count = 0
def print_sound(indata, frames, time, status):
    global count
    count += 1
    # print("frame: ",frames)
    # print("time: ",time)
    # print("status: ",status)
    volume_norm = np.linalg.norm(indata)*10
    print(int(volume_norm),"|" * int(volume_norm))

with sd.InputStream(callback=print_sound):
    sd.sleep(-1)

# print(count)