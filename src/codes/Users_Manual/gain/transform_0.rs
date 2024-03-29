# extern crate autd3;
use autd3::prelude::*;

# #[allow(unused_variables)]
# fn main() {
let g = Uniform::new(EmitIntensity::MAX).with_transform(|dev, tr, d| Drive::new(
    Phase::from_rad(d.phase().radian() + PI),
    EmitIntensity::new(d.intensity().value() / 2),
));
# }