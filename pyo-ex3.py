from pyo import *
s = Server().boot()
f = Adsr(attack=1, decay = 0.2, sustain = 0.5, release = 3, dur = 5, mul = 0.5)
a = Sine(mul= f).out()
f.play()
s.gui(locals())