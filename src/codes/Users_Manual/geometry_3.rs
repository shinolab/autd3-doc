# use autd3::prelude::*;
# 
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::builder([AUTD3::new(Point3::origin())])
#    .open(autd3::link::Nop::builder())?;
let num_dev = autd.num_devices();
let num_tr = autd.num_transducers();
let center = autd.center();
# Ok(())
# }