use autd3::gain::Custom;
# use autd3::prelude::*;

# fn main() {
let _ = Custom::new(|_dev| {
    |_tr| Drive {
        phase: Phase::ZERO,
        intensity: EmitIntensity::MIN,
    }
});
# }