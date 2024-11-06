~from pyautd3 import AUTD3, Controller
~from pyautd3.link.audit import Audit
~
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
dev = autd[0]
for _dev in autd:
    pass