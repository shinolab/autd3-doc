# use autd3::prelude::*;
# use std::time::Duration;
# fn main() {
# let _ = 
Silencer {
    config: FixedCompletionTime {
        intensity: Duration::from_micros(250),
        phase: Duration::from_micros(250),
        strict: true,
    },
};
# }