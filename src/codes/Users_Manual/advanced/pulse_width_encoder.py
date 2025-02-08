~from pyautd3 import AUTD3, Controller, PulseWidthEncoder
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
autd.send(PulseWidthEncoder(lambda _dev: lambda _i: 0))