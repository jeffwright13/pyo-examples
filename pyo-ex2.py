from pyo import *
s = Server().boot()
mod = Sine(freq=9, mul=50)
a = Sine(freq=mod + 660, mul= 0.1).out()
s.gui(locals())