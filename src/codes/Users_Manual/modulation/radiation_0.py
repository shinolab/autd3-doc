~from pyautd3 import Hz, Sine, SineOption
from pyautd3.modulation import RadiationPressure

RadiationPressure(target=Sine(freq=150 * Hz, option=SineOption()))