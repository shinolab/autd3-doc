# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm = FociSTM::new(SamplingConfig::new(1 * Hz)?, [Vector3::zeros(), Vector3::zeros()]);
# Ok(())
# }