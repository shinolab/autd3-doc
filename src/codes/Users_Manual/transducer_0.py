~from pyautd3 import Controller, AUTD3
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
tr = autd.geometry[0][0]
idx = tr.idx
dev_idx = tr.dev_idx
position = tr.position