# use autd3::prelude::*;
use autd3_gain_holo::{EmissionConstraint, Pa, Greedy, GreedyOption, Sphere};
# use std::num::NonZeroU8;

# fn main() {
# let x1 = 0.;
# let y1 = 0.;
# let z1 = 0.;
# let x2 = 0.;
# let y2 = 0.;
# let z2 = 0.;
# let _ = 
Greedy::<Sphere> {
    foci: vec![
        (Point3::new(x1, y1, z1), 5e3 * Pa),
        (Point3::new(x2, y2, z2), 5e3 * Pa),
    ],
    option: GreedyOption {
        phase_div: NonZeroU8::new(16).unwrap(),
        constraint: EmissionConstraint::Uniform(EmitIntensity::MAX),
        ..Default::default()
    },
};
# }
