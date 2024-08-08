# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm = FociSTM::new(1.0 * Hz, [Vector3::zeros(), Vector3::zeros()])?;
let f = stm.freq();                    // -> 1Hz
let p = stm.period();                  // -> 1s
let fs = stm.sampling_config().freq(); // -> 2Hz
# Ok(())
# }