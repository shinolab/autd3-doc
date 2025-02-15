~import numpy as np
~from pyautd3 import FociSTM, Hz
center = np.array([0.0, 0.0, 150.0])
point_num = 200
radius = 30.0
FociSTM(
    foci=(
        center + radius * np.array([np.cos(theta), np.sin(theta), 0])
        for theta in (2.0 * np.pi * i / point_num for i in range(point_num))
    ),
    config=1.0 * Hz,
)