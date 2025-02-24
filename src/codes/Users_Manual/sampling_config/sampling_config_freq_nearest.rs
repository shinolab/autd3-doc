# use std::time::Duration;
# use autd3::prelude::*;
# fn main() {
# let _ = 
SamplingConfig::new(4000.0 * Hz).into_nearest();
// or
# let _ = 
SamplingConfig::new(Duration::from_micros(250)).into_nearest();
# }