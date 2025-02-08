~from pyautd3 import Duration, Hz, SamplingConfig
SamplingConfig(4000 * Hz)
# or
SamplingConfig(Duration.from_micros(250))