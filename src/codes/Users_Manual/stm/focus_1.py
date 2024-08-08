~from pyautd3 import Hz, FociSTM, SamplingConfig
~import numpy as np
~foci = [np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0])]
stm = FociSTM(SamplingConfig(1 * Hz), foci)