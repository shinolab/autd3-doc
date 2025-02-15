~from pyautd3 import AUTD3, Controller
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
tr = autd[0][0]
for _tr in autd[0]:
    pass