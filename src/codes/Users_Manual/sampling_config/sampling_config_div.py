~from pyautd3 import SamplingConfig, Sine, Hz
m = Sine(150 * Hz).with_sampling_config(SamplingConfig(10))