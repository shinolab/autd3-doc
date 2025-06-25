# use autd3::prelude::*;
# fn main() {
# let _ =
// For firmware v11 or later
PulseWidthEncoder::new(|_dev| |i| PulseWidth::<9, u16>::from_duty(i.0 as f32 / 510.0).unwrap());
# let _ =
// For firmware v10
PulseWidthEncoder::new(|_dev| |i| PulseWidth::<8, u8>::from_duty(i.0 as f32 / 510.0).unwrap());
# }