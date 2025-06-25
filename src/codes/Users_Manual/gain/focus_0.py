~from pyautd3 import Intensity, Focus, FocusOption, Phase
~
~x = 1.0
~y = 0.0
~z = 0.0
Focus(
    pos=[x, y, z],
    option=FocusOption(
        intensity=Intensity.MAX,
        phase_offset=Phase.ZERO,
    ),
)