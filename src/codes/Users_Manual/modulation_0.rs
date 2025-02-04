# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let _ = 
autd3::modulation::Sine {
    freq: 150 * Hz,
    option: SineOption {
        sampling_config: SamplingConfig::new(4000 * Hz)?,
        ..Default::default()
    }
}
# ;
# Ok(())
# }