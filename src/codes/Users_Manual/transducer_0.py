~from pyautd3 import AUTD3, Controller
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
tr = autd[0][0]
idx = tr.idx()
dev_idx = tr.dev_idx()
position = tr.position()