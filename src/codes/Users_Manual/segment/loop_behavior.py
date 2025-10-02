~from pyautd3 import Segment, Static, transition_mode, WithFiniteLoop

WithFiniteLoop(
    inner=Static(),
    loop_count=1,
    segment=Segment.S1,
    transition_mode=transition_mode.SyncIdx(),
)