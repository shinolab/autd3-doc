# extern crate autd3;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let config = ConfigureSilencer::default();
let config = ConfigureSilencer::disable();
# Ok(())
# }