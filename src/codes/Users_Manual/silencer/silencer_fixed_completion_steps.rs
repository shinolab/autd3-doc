# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
let config = Silencer::new(
    FixedCompletionTime {
        intensity: std::time::Duration::from_micros(250),
        phase: std::time::Duration::from_micros(250),
    }
);
# }