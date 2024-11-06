~from pyautd3 import AUTD3, Controller, PulseWidthEncoder
~from pyautd3.link.audit import Audit
~
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
autd.send(PulseWidthEncoder(lambda _dev: lambda _i: 0))