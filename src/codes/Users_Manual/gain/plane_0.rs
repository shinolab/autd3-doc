# use autd3::prelude::*;
# fn main() {
# let nx = 0.;
# let ny = 0.;
# let nz = 0.;
# let _ = 
Plane {
    dir: UnitVector3::new_normalize(Vector3::new(nx, ny, nz)),
    option: PlaneOption {
        intensity: EmitIntensity::MAX,
        phase_offset: Phase::ZERO,
    },
};
# }