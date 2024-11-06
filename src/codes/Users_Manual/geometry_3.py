~from pyautd3 import AUTD3, Controller
~from pyautd3.link.audit import Audit
~
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
num_devices = autd.num_devices
num_transducers = autd.num_transducers
center = autd.center