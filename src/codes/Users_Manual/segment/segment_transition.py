~from pyautd3 import Segment, Static, TransitionMode
~from pyautd3.driver.datagram.with_segment import WithSegment
WithSegment(
    inner=Static(),
    segment=Segment.S1,
    transition_mode=TransitionMode.Immediate,
)