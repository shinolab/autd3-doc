# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm = FociSTM::new(SamplingConfig::new(1 * Hz)?, [Point3::origin(), Point3::origin()]);
# Ok(())
# }