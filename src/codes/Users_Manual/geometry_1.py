~from pyautd3 import AUTD3, Controller
~from pyautd3.link.nop import Nop
~link = Nop()
Controller.open(
    [
        AUTD3(pos=[-AUTD3.DEVICE_WIDTH, 0.0, 0.0], rot=[1, 0, 0, 0]),
        AUTD3(pos=[0.0, 0.0, 0.0], rot=[1, 0, 0, 0]),
    ],
    link,
)