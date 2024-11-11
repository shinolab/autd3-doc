~from pyautd3 import Duration, Hz, SamplingConfig
SamplingConfig.nearest(4000.0 * Hz)
# or
SamplingConfig.nearest(Duration.from_micros(250))