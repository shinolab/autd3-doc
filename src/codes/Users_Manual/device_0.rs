# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
let dev = &mut autd[0];
let idx = dev.idx();
let rotation = dev.rotation();
let x_dir = dev.x_direction();
let y_dir = dev.y_direction();
let axial_dir = dev.axial_direction();
# Ok(())
# }