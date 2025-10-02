~from pyautd3 import Segment, Static, transition_mode, WithSegment
WithSegment(
    inner=Static(),
    segment=Segment.S1,
    transition_mode=transition_mode.Immediate(),
)