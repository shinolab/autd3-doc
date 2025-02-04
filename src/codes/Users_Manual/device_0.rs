# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
let dev = &mut autd[0];
let idx = dev.idx();
dev.enable = false;
dev.sound_speed = 340e3;
dev.set_sound_speed_from_temp(15.);
let t = Vector3::new(1., 0., 0.);
let r = UnitQuaternion::from_quaternion(Quaternion::new(1., 0., 0., 0.));
dev.translate(t);
dev.rotate(r);
dev.affine(t, r);
let wavelength = dev.wavelength();
let wavenumber = dev.wavenumber();
let rotation = dev.rotation();
let x_dir = dev.x_direction();
let y_dir = dev.y_direction();
let axial_dir = dev.axial_direction();
# Ok(())
# }