# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
# let x = 0.;
# let y = 0.;
# let z = 0.;
let g = Focus::new(Point3::new(x, y, z))
            .with_intensity(0xFF)
            .with_phase_offset(0x00);
# }