~import numpy as np
~from pyautd3 import FociSTM, Hz
stm = FociSTM(
    foci=[np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0])],
    config=1.0 * Hz,
)
print(stm.sampling_config().freq())  # -> 2Hz