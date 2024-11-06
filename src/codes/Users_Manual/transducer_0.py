~from pyautd3 import AUTD3, Controller
~from pyautd3.link.audit import Audit
~
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
tr = autd[0][0]
idx = tr.idx
dev_idx = tr.dev_idx
position = tr.position