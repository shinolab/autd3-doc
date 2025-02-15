# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
let num_dev = autd.num_devices();
let num_tr = autd.num_transducers();
let center = autd.center();
# Ok(())
# }