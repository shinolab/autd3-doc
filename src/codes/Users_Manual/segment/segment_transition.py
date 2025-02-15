~from pyautd3 import Segment, Static, TransitionMode, WithSegment
WithSegment(
    inner=Static(),
    segment=Segment.S1,
    transition_mode=TransitionMode.Immediate,
)