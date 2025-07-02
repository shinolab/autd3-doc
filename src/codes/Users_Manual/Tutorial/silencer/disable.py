~import numpy as np
~from pyautd3 import AUTD3, Controller, Hz, FociSTM, Silencer
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3(pos=[0.0, 0.0, 0.0], rot=[1, 0, 0, 0])], Nop())
autd.send(Silencer.disable())

center = autd.center() + np.array([0.0, 0.0, 150.0])
point_num = 20
radius = 30.0
autd.send(
    FociSTM(
        foci=(
            center + radius * np.array([np.cos(theta), np.sin(theta), 0])
            for theta in (2.0 * np.pi * i / point_num for i in range(point_num))
        ),
        config=50.0 * Hz,
    )
)