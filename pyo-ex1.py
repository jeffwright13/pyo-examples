from pyo import *
s = Server().boot()
s.start()
a = Sine(mul=0.05).out()
s.gui(locals())
