~import numpy as np
~from pyautd3 import AUTD3, Controller, Focus, GainSTM, Hz
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(
~    Audit.builder()
~)
center = autd.center + np.array([0.0, 0.0, 150.0])
point_num = 200
radius = 30.0
stm = GainSTM(
    1.0 * Hz,
    map(
        lambda theta: Focus(
            center + radius * np.array([np.cos(theta), np.sin(theta), 0])
        ),
        map(lambda i: 2.0 * np.pi * i / point_num, range(point_num)),
    ),
)