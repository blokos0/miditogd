# https://wyliemaster.github.io/gddocs
# https://gdcolon.com/gmd_tools
# https://flowvix.github.io/gd-info-explorer/props
import mido
from mido import MidiFile
bpm = 100
basebpm = 156 # dont ask
mid = MidiFile(input("input midi file (with extension): "))
time = 0
blocks = ""
inst = "392,592,408,105" # sfx settings
# bright piano 392,592,408,105
# kick 392,3884
# snare 392,3916
transpose = 0
volume = 1
for i, track in enumerate(mid.tracks):
    time = 0
    for msg in track:
        if msg.type == "set_tempo":
            bpm = mido.tempo2bpm(msg.tempo)
        if msg.time > 0:
            time += (msg.time) / 24 * (basebpm / bpm) * 30
        if msg.type == "note_on":
            pitch = msg.note + transpose - 60
            badpitch = 0
            if abs(pitch) > 12:
                if pitch > 0: # too lazy to make a sign function
                    badpitch = pitch - 12
                    pitch = 12
                elif pitch < 0:
                    badpitch = pitch + 12
                    pitch = -12
            if abs(badpitch) > 12:
                print("eeeyikes!")
            blocks += f"1,3602,2,{time},3,{(pitch + 60 + badpitch) * 30},404,{pitch},405,{badpitch},36,1,406,{volume},{inst};"
print("\n" + blocks + "\n")
