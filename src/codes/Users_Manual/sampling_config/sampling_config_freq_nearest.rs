# use std::time::Duration;
# use autd3::prelude::*;
# fn main() {
# let _ = 
SamplingConfig::new_nearest(4000.0 * Hz);
// or
# let _ = 
SamplingConfig::new_nearest(Duration::from_micros(250));
# }