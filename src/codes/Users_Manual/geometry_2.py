~import numpy as np
~from pyautd3 import AUTD3, Controller, EulerAngles, Nop, rad
~link = Nop()
Controller.open(
    [
        AUTD3(pos=[0.0, 0.0, 0.0], rot=[1.0, 0.0, 0.0, 0.0]),
        AUTD3(
            pos=[AUTD3.DEVICE_WIDTH, 0.0, 0.0],
            rot=EulerAngles.ZYZ(0 * rad, np.pi / 2 * rad, 0 * rad),
        ),
    ],
    link,
)