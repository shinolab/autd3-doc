~from pyautd3 import AUTD3, Controller
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
dev = autd[0]
idx = dev.idx()
rotation = dev.rotation()
x_dir = dev.x_direction()
y_dir = dev.y_direction()
axial_dir = dev.axial_direction()