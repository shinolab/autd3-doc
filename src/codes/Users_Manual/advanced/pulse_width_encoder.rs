# use autd3::prelude::*;
# fn main() {
# let _ =
PulseWidthEncoder::new(|_dev| |i| PulseWidth::from_duty(i.0 as f32 / 510.0).unwrap());
# }