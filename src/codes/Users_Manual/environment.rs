# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
autd.environment.sound_speed = 340e3;
autd.environment.set_sound_speed_from_temp(15.);
let wavelength = autd.environment.wavelength();
let wavenumber = autd.environment.wavenumber();
# Ok(())
# }