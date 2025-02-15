# use std::num::NonZeroU16;
# use autd3::prelude::*;
# fn main() {
# let _ = 
WithLoopBehavior {
    inner: Static::default(),
    loop_behavior: LoopBehavior::Infinite,
    segment: Segment::S1,
    transition_mode: Some(TransitionMode::Immediate),
};

# let _ = 
WithLoopBehavior {
    inner: Static::default(),
    loop_behavior: LoopBehavior::Finite(NonZeroU16::new(1).unwrap()),
    segment: Segment::S1,
    transition_mode: Some(TransitionMode::SyncIdx),
};
# }