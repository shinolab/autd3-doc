~from pyautd3 import Hz, Duration
~from pyautd3.modulation import Sine
m = Sine(150 * Hz).with_sampling_config(4000 * Hz)
# or
m = Sine(150 * Hz).with_sampling_config(Duration.from_micros(250))