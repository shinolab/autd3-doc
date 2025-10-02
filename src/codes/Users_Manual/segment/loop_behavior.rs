# use std::num::NonZeroU16;
# use autd3::prelude::*;
# fn main() {
# let _ = 
WithFiniteLoop {
    inner: Static::default(),
    loop_count: NonZeroU16::new(1).unwrap(),
    segment: Segment::S1,
    transition_mode: transition_mode::SyncIdx,
};
# }