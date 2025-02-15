~from pyautd3 import Controller, AUTD3, ReadsFPGAState
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
autd.send(ReadsFPGAState(lambda _: True))

info = autd.fpga_state()