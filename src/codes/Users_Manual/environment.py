~from pyautd3 import AUTD3, Controller
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
autd.environment.sound_speed = 340e3
autd.environment.set_sound_speed_from_temp(15.0)
wavelength = autd.environment.wavelength()
wavenumber = autd.environment.wavenumber()