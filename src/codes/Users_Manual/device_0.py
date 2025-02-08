~import numpy as np
~from pyautd3 import AUTD3, Controller
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
dev = autd[0]
idx = dev.idx()
dev.enable = False
dev.sound_speed = 340e3
dev.set_sound_speed_from_temp(15.0)
t = np.array([1.0, 0.0, 0.0])
r = np.array([1.0, 0.0, 0.0, 0.0])
dev.translate(t)
dev.rotate(r)
dev.affine(t, r)
wavelength = dev.wavelength()
wavenumber = dev.wavenumber()
rotation = dev.rotation()
x_dir = dev.x_direction()
y_dir = dev.y_direction()
axial_dir = dev.axial_direction()