~from pyautd3 import AUTD3, Controller
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
num_devices = autd.num_devices()
num_transducers = autd.num_transducers()
center = autd.center()