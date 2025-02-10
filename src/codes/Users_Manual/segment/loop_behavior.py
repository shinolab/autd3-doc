~from pyautd3 import Segment, Static, TransitionMode, LoopBehavior
~from pyautd3.driver.datagram.with_loop_behavior import WithLoopBehavior
WithLoopBehavior(
    inner=Static(),
    loop_behavior=LoopBehavior.Infinite,
    segment=Segment.S1,
    transition_mode=TransitionMode.Immediate,
)

WithLoopBehavior(
    inner=Static(),
    loop_behavior=LoopBehavior.Finite(10),
    segment=Segment.S1,
    transition_mode=TransitionMode.SyncIdx,
)