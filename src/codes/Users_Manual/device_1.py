~from pyautd3 import AUTD3, Controller
~from pyautd3.link.audit import Audit
~
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
tr = autd[0][0]
for _tr in autd[0]:
    pass