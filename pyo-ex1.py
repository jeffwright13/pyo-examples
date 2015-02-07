from pyo import *
s = Server().boot()
s.start()
m = 0.10
ph=0
f=1100
a = Sine(freq=f, mul=m, phase=ph).out()
s.gui(locals())
