~import numpy as np
~from pyautd3 import AUTD3, Controller, FociSTM, Hz
~from pyautd3.link.audit import Audit
~
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
center = autd.center + np.array([0.0, 0.0, 150.0])
point_num = 200
radius = 30.0
stm = FociSTM(
    1.0 * Hz,
    (
        center + radius * np.array([np.cos(theta), np.sin(theta), 0])
        for theta in (2.0 * np.pi * i / point_num for i in range(point_num))
    ),
)