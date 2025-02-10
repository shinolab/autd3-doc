~from pyautd3 import ForceFan, Controller, AUTD3
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
autd.send(ForceFan(lambda _: True))