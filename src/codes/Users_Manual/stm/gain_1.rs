# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm = GainSTM::new(SamplingConfig::new(1 * Hz)?, [Null::new(), Null::new()]);
# Ok(())
# }