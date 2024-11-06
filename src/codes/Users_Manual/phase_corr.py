~from pyautd3 import AUTD3, Controller, Phase, PhaseCorrection
~from pyautd3.link.audit import Audit
~
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
autd.send(PhaseCorrection(lambda _dev: lambda _tr: Phase(0x00)))