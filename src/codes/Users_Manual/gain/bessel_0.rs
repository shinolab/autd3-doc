# use autd3::prelude::*;
# fn main() {
# let x = 0.;
# let y = 0.;
# let z = 0.;
# let nx = 0.;
# let ny = 0.;
# let nz = 0.;
# let theta = 0. * rad;
# let _ = 
Bessel {
    apex: Point3::new(x, y, z),
    dir: UnitVector3::new_normalize(Vector3::new(nx, ny, nz)),
    theta,
    option: BesselOption {
        intensity: Intensity::MAX,
        phase_offset: Phase::ZERO,
    },
};
# }