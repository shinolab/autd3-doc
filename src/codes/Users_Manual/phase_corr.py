~from pyautd3 import PhaseCorrection, Phase
~from pyautd3 import Controller, AUTD3
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
autd.send(PhaseCorrection(lambda _dev: lambda _tr: Phase(0x00)))