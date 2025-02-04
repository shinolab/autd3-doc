# use autd3::prelude::*;
# use std::num::NonZeroU16;
# fn main() {
# let _ = 
Silencer {
    config: FixedUpdateRate {
        intensity: NonZeroU16::MIN,
        phase: NonZeroU16::MIN,
    },
    target: SilencerTarget::Intensity,
};
# }