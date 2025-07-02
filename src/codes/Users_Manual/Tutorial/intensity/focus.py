~from pyautd3 import Intensity, Focus, FocusOption
~x = 1.0
~y = 0.0
~z = 0.0
Focus(
    pos=[x, y, z],
    option=FocusOption(
        intensity=Intensity(0x80),
    ),
)