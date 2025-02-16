~from pyautd3 import Segment, Static, TransitionMode, LoopBehavior, WithLoopBehavior
WithLoopBehavior(
    inner=Static(),
    loop_behavior=LoopBehavior.Infinite,
    segment=Segment.S1,
    transition_mode=TransitionMode.Immediate,
)

WithLoopBehavior(
    inner=Static(),
    loop_behavior=LoopBehavior.Finite(1),
    segment=Segment.S1,
    transition_mode=TransitionMode.SyncIdx,
)