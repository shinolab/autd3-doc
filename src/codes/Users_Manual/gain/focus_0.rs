# use autd3::prelude::*;
# fn main() {
# let x = 0.;
# let y = 0.;
# let z = 0.;
# let _ = 
Focus {
    pos: Point3::new(x, y, z),
    option: FocusOption {
        intensity: EmitIntensity::MAX,
        phase_offset: Phase::ZERO,
    },
};
# }