# use std::num::NonZeroU16;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let config = Silencer::new(
    FixedUpdateRate {
        intensity: NonZeroU16::new(1).unwrap(),
        phase: NonZeroU16::new(1).unwrap(),
    }
);
# Ok(())
# }