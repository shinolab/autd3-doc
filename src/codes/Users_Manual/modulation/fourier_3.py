~from pyautd3 import Hz, Sine
~from pyautd3.modulation import Fourier
~
m = (
    Fourier([Sine(100 * Hz), Sine(150 * Hz)])
    .with_scale_factor(1.0)
    .with_offset(0)
    .with_clamp(True)
)