from Tkinter import *
import tkFont
import sys
import pyChuck
import time

# Prepare pyChuck
pyc = pyChuck.pyChuck()
time.sleep(1)
shred = 1
try:
    pyc.shred("scale.ck")
    shred += 1
except:
    print("shred scale.ck failed")
    print sys.exc_info()
active_shred_1 = 0
active_shred_2 = 0
active_shred_3 = 0

# Play function

def play(track, inst, vol, spd, octv, shft, scl):
    global shred
    global active_shred_1
    global active_shred_2
    global active_shred_3
    if track == 1:
        if active_shred_1 != 0:
            pyc.sndMsg(["unshred", str(active_shred_1)])
            active_shred_1 = 0
        message = "i_"+str(inst)+".ck:"+str(vol)+":"+str(spd)+":"+str(octv)+":"+str(shft)+":"+str(scl)
        pyc.shred(message)
        shred += 1
        active_shred_1 = shred
    if track == 2:
        if active_shred_2 != 0:
            pyc.sndMsg(["unshred", str(active_shred_2)])
            active_shred_2 = 0
        pyc.shred("i_"+str(inst)+".ck:"+str(vol)+":"+str(spd)+":"+str(octv)+":"+str(shft)+":"+str(scl))
        shred += 1
        active_shred_2 = shred
    if track == 3:
        if active_shred_3 != 0:
            pyc.sndMsg(["unshred", str(active_shred_3)])
            active_shred_3 = 0
        pyc.shred("i_"+str(inst)+".ck:"+str(vol)+":"+str(spd)+":"+str(octv)+":"+str(shft)+":"+str(scl))
        shred += 1
        active_shred_3 = shred

# Button functions

def play_1():
    if scale_1.get() == 'Major':
        scale = 0
    if scale_1.get() == 'Melodic':
        scale = 1
    if scale_1.get() == 'Harmonic':
        scale = 2
    play(1, instrument_1.get(), volume_1.get(), speed_1.get(), octave_1.get(), shift_1.get(), scale)
    if active_shred_2 != 0:
        if scale_2.get() == 'Major':
            scale = 0
        if scale_2.get() == 'Melodic':
            scale = 1
        if scale_2.get() == 'Harmonic':
            scale = 2
        play(2, instrument_2.get(), volume_2.get(), speed_2.get(), octave_2.get(), shift_2.get(), scale)
    if active_shred_3 != 0:
        if scale_3.get() == 'Major':
            scale = 0
        if scale_3.get() == 'Melodic':
            scale = 1
        if scale_3.get() == 'Harmonic':
            scale = 2
        play(3, instrument_3.get(), volume_3.get(), speed_3.get(), octave_3.get(), shift_3.get(), scale)
    return

def stop_1():
    global active_shred_1
    pyc.sndMsg(["unshred", str(active_shred_1)])
    active_shred_1 = 0
    return

def play_2():
    if scale_2.get() == 'Major':
        scale = 0
    if scale_2.get() == 'Melodic':
        scale = 1
    if scale_2.get() == 'Harmonic':
        scale = 2
    play(2, instrument_2.get(), volume_2.get(), speed_2.get(), octave_2.get(), shift_2.get(), scale)
    if active_shred_1 != 0:
        if scale_1.get() == 'Major':
            scale = 0
        if scale_1.get() == 'Melodic':
            scale = 1
        if scale_1.get() == 'Harmonic':
            scale = 2
        play(1, instrument_1.get(), volume_1.get(), speed_1.get(), octave_1.get(), shift_1.get(), scale)
    if active_shred_3 != 0:
        if scale_3.get() == 'Major':
            scale = 0
        if scale_3.get() == 'Melodic':
            scale = 1
        if scale_3.get() == 'Harmonic':
            scale = 2
        play(3, instrument_3.get(), volume_3.get(), speed_3.get(), octave_3.get(), shift_3.get(), scale)
    return

def stop_2():
    global active_shred_2
    pyc.sndMsg(["unshred", str(active_shred_2)])
    active_shred_2 = 0
    return

def play_3():
    if scale_3.get() == 'Major':
        scale = 0
    if scale_3.get() == 'Melodic':
        scale = 1
    if scale_3.get() == 'Harmonic':
        scale = 2
    play(3, instrument_3.get(), volume_3.get(), speed_3.get(), octave_3.get(), shift_3.get(), scale)
    if active_shred_1 != 0:
        if scale_1.get() == 'Major':
            scale = 0
        if scale_1.get() == 'Melodic':
            scale = 1
        if scale_1.get() == 'Harmonic':
            scale = 2
        play(1, instrument_1.get(), volume_1.get(), speed_1.get(), octave_1.get(), shift_1.get(), scale)
    if active_shred_2 != 0:
        if scale_2.get() == 'Major':
            scale = 0
        if scale_2.get() == 'Melodic':
            scale = 1
        if scale_2.get() == 'Harmonic':
            scale = 2
        play(2, instrument_2.get(), volume_2.get(), speed_2.get(), octave_2.get(), shift_2.get(), scale)
    return

def stop_3():
    global active_shred_3
    pyc.sndMsg(["unshred", str(active_shred_3)])
    active_shred_3 = 0
    return

def play_all():
    if scale_3.get() == 'Major':
        scale = 0
    if scale_3.get() == 'Melodic':
        scale = 1
    if scale_3.get() == 'Harmonic':
        scale = 2
    play(3, instrument_3.get(), volume_3.get(), speed_3.get(), octave_3.get(), shift_3.get(), scale)
    if scale_1.get() == 'Major':
        scale = 0
    if scale_1.get() == 'Melodic':
        scale = 1
    if scale_1.get() == 'Harmonic':
        scale = 2
    play(1, instrument_1.get(), volume_1.get(), speed_1.get(), octave_1.get(), shift_1.get(), scale)
    if scale_2.get() == 'Major':
        scale = 0
    if scale_2.get() == 'Melodic':
        scale = 1
    if scale_2.get() == 'Harmonic':
        scale = 2
    play(2, instrument_2.get(), volume_2.get(), speed_2.get(), octave_2.get(), shift_2.get(), scale)
    return

def stop_all():
    stop_1()
    stop_2()
    stop_3()
    return

master = Tk()
master.wm_title("Nonsense Music Player")

font_slider = tkFont.Font(family='Helvetica',
    size=10)
font_button = tkFont.Font(family='Helvetica',
    size=20)
font_button_big = tkFont.Font(family='Helvetica',
    size=25)

# 1st row

Button(master, text='Play 1', command=play_1, font=font_button).grid(row=0, column=0, sticky=N+S+E+W)
Button(master, text='Stop 1', command=stop_1, font=font_button).grid(row=0, column=1, sticky=N+S+E+W)

instrument_1 = StringVar(master)
instrument_1.set("BandedWG")
instrument_option_1 = OptionMenu(master, instrument_1,
                               "BandedWG", "BlowBotl", "BlowHole", "Bowed", "Brass", "Clarinet",
                               "Mandolin", "ModalBar", "Moog", "Saxofony", "Shakers", "Sitar",
                               "StifKarp", "VoicForm")
instrument_option_1.grid(row=0, column=2, sticky=N+S+E+W)

volume_1 = Scale(master, from_=1, to=80, label="Volume", orient=HORIZONTAL, font=font_slider)
volume_1.set(50)
volume_1.grid(row=0, column=3)

speed_1 = Scale(master, from_=1, to=10, label="Speed", orient=HORIZONTAL, font=font_slider)
speed_1.set(3)
speed_1.grid(row=0, column=4)

octave_1 = Scale(master, from_=0, to=10, label="Octave", orient=HORIZONTAL, font=font_slider)
octave_1.set(5)
octave_1.grid(row=0, column=5)

shift_1 = Scale(master, from_=0, to=12, label="Shift", orient=HORIZONTAL, font=font_slider)
shift_1.set(0)
shift_1.grid(row=0, column=6)

scale_1 = StringVar(master)
scale_1.set("Major")
scale_option_1 = OptionMenu(master, scale_1, "Major", "Melodic", "Harmonic")
scale_option_1.grid(row=0, column=7, sticky=N+S+E+W)

# 2nd row

Button(master, text='Play 2', command=play_2, font=font_button).grid(row=1, column=0, sticky=N+S+E+W)
Button(master, text='Stop 2', command=stop_2, font=font_button).grid(row=1, column=1, sticky=N+S+E+W)

instrument_2 = StringVar(master)
instrument_2.set("BandedWG")
instrument_option_2 = OptionMenu(master, instrument_2,
                               "BandedWG", "BlowBotl", "BlowHole", "Bowed", "Brass", "Clarinet",
                               "Mandolin", "ModalBar", "Moog", "Saxofony", "Shakers", "Sitar",
                               "StifKarp", "VoicForm")
instrument_option_2.grid(row=1, column=2, sticky=N+S+E+W)

volume_2 = Scale(master, from_=1, to=80, label="Volume", orient=HORIZONTAL, font=font_slider)
volume_2.set(50)
volume_2.grid(row=1, column=3)

speed_2 = Scale(master, from_=1, to=10, label="Speed", orient=HORIZONTAL, font=font_slider)
speed_2.set(3)
speed_2.grid(row=1, column=4)

octave_2 = Scale(master, from_=0, to=10, label="Octave", orient=HORIZONTAL, font=font_slider)
octave_2.set(5)
octave_2.grid(row=1, column=5)

shift_2 = Scale(master, from_=0, to=12, label="Shift", orient=HORIZONTAL, font=font_slider)
shift_2.set(0)
shift_2.grid(row=1, column=6)

scale_2 = StringVar(master)
scale_2.set("Major")
scale_option_2 = OptionMenu(master, scale_2, "Major", "Melodic", "Harmonic")
scale_option_2.grid(row=1, column=7, sticky=N+S+E+W)

# 3rd row

Button(master, text='Play 3', command=play_3, font=font_button).grid(row=2, column=0, sticky=N+S+E+W)
Button(master, text='Stop 3', command=stop_3, font=font_button).grid(row=2, column=1, sticky=N+S+E+W)

instrument_3 = StringVar(master)
instrument_3.set("BandedWG")
instrument_option_3 = OptionMenu(master, instrument_3,
                               "BandedWG", "BlowBotl", "BlowHole", "Bowed", "Brass", "Clarinet",
                               "Mandolin", "ModalBar", "Moog", "Saxofony", "Shakers", "Sitar",
                               "StifKarp", "VoicForm")
instrument_option_3.grid(row=2, column=2, sticky=N+S+E+W)

volume_3 = Scale(master, from_=1, to=80, label="Volume", orient=HORIZONTAL, font=font_slider)
volume_3.set(50)
volume_3.grid(row=2, column=3)

speed_3 = Scale(master, from_=1, to=10, label="Speed", orient=HORIZONTAL, font=font_slider)
speed_3.set(3)
speed_3.grid(row=2, column=4)

octave_3 = Scale(master, from_=0, to=10, label="Octave", orient=HORIZONTAL, font=font_slider)
octave_3.set(5)
octave_3.grid(row=2, column=5)

shift_3 = Scale(master, from_=0, to=12, label="Shift", orient=HORIZONTAL, font=font_slider)
shift_3.set(0)
shift_3.grid(row=2, column=6)

scale_3 = StringVar(master)
scale_3.set("Major")
scale_option_3 = OptionMenu(master, scale_3, "Major", "Melodic", "Harmonic")
scale_option_3.grid(row=2, column=7, sticky=N+S+E+W)

# Play all / Stop all

Button(master, text='Play All', command=play_all, font=font_button_big).grid(row=3, column=0,
    columnspan=4, rowspan=1, sticky=W+E+N+S)
Button(master, text='Stop All', command=stop_all, font=font_button_big).grid(row=3, column=4,
    columnspan=4, rowspan=1, sticky=W+E+N+S)

mainloop()

# Cleanup

print sys.exc_info()
pyc.cleanup()
