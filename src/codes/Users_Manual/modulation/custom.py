~from pyautd3 import Hz
~import numpy as np
from pyautd3.modulation import Custom

Custom(
    buffer=np.array([0xFF, 0x00]),
    sampling_config=4000.0 * Hz,
)