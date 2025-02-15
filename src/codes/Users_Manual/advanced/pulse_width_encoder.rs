# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
autd.send(PulseWidthEncoder::new(|_dev| |_i| 0u8))?;
# Ok(())
# }