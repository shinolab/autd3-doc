# use autd3::prelude::*;
use autd3_gain_holo::{EmissionConstraint, NalgebraBackend, Pa, LM, LMOption};
# use std::num::NonZeroUsize;
# use std::sync::Arc;

# fn main() {
# let x1 = 0.;
# let y1 = 0.;
# let z1 = 0.;
# let x2 = 0.;
# let y2 = 0.;
# let z2 = 0.;
let backend = Arc::new(NalgebraBackend::default());
# let _ = 
LM {
    foci: vec![
        (Point3::new(x1, y1, z1), 5e3 * Pa),
        (Point3::new(x2, y2, z2), 5e3 * Pa),
    ],
    option: LMOption {
        eps_1: 1e-8,
        eps_2: 1e-8,
        tau: 1e-3,
        k_max: NonZeroUsize::new(5).unwrap(),
        initial: vec![],
        constraint: EmissionConstraint::Clamp(EmitIntensity::MIN, EmitIntensity::MAX),
        ..Default::default()
    },
    backend,
};
# }
