# use std::time::Duration;
# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let _ = 
SamplingConfig::new(4000 * Hz)?;
// or
# let _ = 
SamplingConfig::new(Duration::from_micros(250))?;
# Ok(())
# }