~from pyautd3 import Intensity, Focus, FocusOption, WithSegment, Segment, transition_mode
~x = 1.0
~y = 0.0
~z = 0.0
WithSegment(
    inner=Focus(
        pos=[x, y, z],
        option=FocusOption(
            intensity=Intensity(0x80),
        ),
    ),
    segment=Segment.S1,
    transition_mode=transition_mode.Immediate(),
)