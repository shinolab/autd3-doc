~from pyautd3 import Hz
~from pyautd3.modulation import Sine, SineOption
m = Sine(freq=150 * Hz, option=SineOption())
print(m.sampling_config().freq())  # -> 4kHz