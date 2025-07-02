~import time
~import numpy as np
~from pyautd3 import AUTD3, Controller, Focus, FocusOption, Hz, Sine, SineOption
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3(pos=[0.0, 0.0, 0.0], rot=[1, 0, 0, 0])], Nop())
autd.send(
    Sine(
        freq=150 * Hz,
        option=SineOption(),
    )
)

center = autd.center() + np.array([0.0, 0.0, 150.0])
while True:
    autd.send(
        Focus(
            pos=center + np.array([20.0, 0.0, 0.0]),
            option=FocusOption(),
        ),
    )

    time.sleep(1)

    autd.send(
        Focus(
            pos=center - np.array([20.0, 0.0, 0.0]),
            option=FocusOption(),
        ),
    )

    time.sleep(1)