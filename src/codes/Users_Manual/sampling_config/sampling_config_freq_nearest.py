~from pyautd3 import SamplingConfig, Hz
~from datetime import timedelta
SamplingConfig.nearest(4000.0 * Hz)
# or
SamplingConfig.nearest(timedelta(microseconds=250))