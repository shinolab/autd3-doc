# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm = GainSTM::new(1.0 * Hz, [Null::new(), Null::new()])?
    .with_mode(GainSTMMode::PhaseFull);
# Ok(())
# }