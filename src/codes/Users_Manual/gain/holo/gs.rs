# use autd3::prelude::*;
use autd3_gain_holo::{EmissionConstraint, Pa, GS, GSOption};
# use std::num::NonZeroUsize;

# fn main() {
# let x1 = 0.;
# let y1 = 0.;
# let z1 = 0.;
# let x2 = 0.;
# let y2 = 0.;
# let z2 = 0.;
# let _ = 
GS::new(
    vec![
        (Point3::new(x1, y1, z1), 5e3 * Pa),
        (Point3::new(x2, y2, z2), 5e3 * Pa),
    ],
    GSOption {
        repeat: NonZeroUsize::new(100).unwrap(),
        constraint: EmissionConstraint::Clamp(Intensity::MIN, Intensity::MAX),
    },
);
# }
