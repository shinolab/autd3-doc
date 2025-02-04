# use autd3::prelude::*;
# use autd3::driver::datagram::WithSegment;
# fn main() {
# let _ = 
WithSegment {
    inner: Static::default(),
    segment: Segment::S1,
    transition_mode: Some(TransitionMode::Immediate),
};
# }