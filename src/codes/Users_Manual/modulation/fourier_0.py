~from pyautd3 import Hz, Sine, SineOption
from pyautd3.modulation import Fourier, FourierOption

Fourier(
    components=[
        Sine(freq=100 * Hz, option=SineOption()),
        Sine(freq=150 * Hz, option=SineOption()),
    ],
    option=FourierOption(
        scale_factor=None,
        clamp=False,
        offset=0x00,
    ),
)