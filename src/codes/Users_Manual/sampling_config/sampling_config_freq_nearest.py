~from pyautd3 import Duration, Hz, SamplingConfig
SamplingConfig(4000.0 * Hz).into_nearest()
# or
SamplingConfig(Duration.from_micros(250)).into_nearest()