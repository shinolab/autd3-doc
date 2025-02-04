# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm = FociSTM {
    foci: vec![Point3::origin(), Point3::origin()],
    config: 1.0 * Hz,
};
dbg!(stm.sampling_config()?.freq()); // -> 2Hz
# Ok(())
# }