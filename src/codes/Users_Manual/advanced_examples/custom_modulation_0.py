import numpy as np
from pyautd3 import EmitIntensity, SamplingConfig
from pyautd3.modulation import Modulation


class Burst(Modulation):
    _length: int

    def __init__(self, length: int = 4000):
        super().__init__(SamplingConfig.freq(4000))
        self._length = length

    def calc(self):
        buf = np.array([EmitIntensity.minimum()] * self._length)
        buf[0] = EmitIntensity.maximum()
        return buf
