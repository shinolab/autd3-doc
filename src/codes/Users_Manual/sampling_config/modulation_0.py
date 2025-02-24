~from pyautd3 import Duration, Hz, SamplingConfig
SamplingConfig(10)
# or
SamplingConfig(4000.0 * Hz)
# or
SamplingConfig(Duration.from_micros(250))