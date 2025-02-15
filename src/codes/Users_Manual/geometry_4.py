~from pyautd3 import AUTD3, Controller
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
dev = autd[0]
for _dev in autd:
    pass