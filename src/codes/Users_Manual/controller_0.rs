# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
autd.send(ReadsFPGAState::new(|_dev| true))?;

let info = autd.fpga_state()?;
# Ok(())
# }