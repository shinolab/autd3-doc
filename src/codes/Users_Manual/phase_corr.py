~from pyautd3 import AUTD3, Controller, Phase, PhaseCorrection
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
autd.send(PhaseCorrection(lambda _dev: lambda _tr: Phase.ZERO))