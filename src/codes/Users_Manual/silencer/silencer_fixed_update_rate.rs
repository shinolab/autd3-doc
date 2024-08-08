# use std::num::NonZeroU8;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let update_rate_intensity = NonZeroU8::new(1).unwrap();
let update_rate_phase = NonZeroU8::new(1).unwrap();
let config = Silencer::from_update_rate(update_rate_intensity, update_rate_phase);
# Ok(())
# }