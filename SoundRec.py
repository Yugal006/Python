import sounddevice as sd
from scipy.io.wavfile import write

ask = int(input("how many second you want to record sound?\n"))
print("if you get error or program get close please make sure your mic is on.\n")

fs = 44100
second = (ask)

print("recording:")
record_voice = sd.rec(int(second * fs), samplerate = fs, channels=1)
sd.wait()
write("C:\\Users\\Admin\\Desktop\\output.wav",fs,record_voice)
