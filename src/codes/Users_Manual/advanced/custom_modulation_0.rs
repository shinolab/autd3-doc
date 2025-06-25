# use autd3::prelude::*;
use autd3::core::derive::*;

#[derive(Modulation, Debug)]
pub struct Burst {
    config: SamplingConfig,
}

impl Burst {
    pub fn new() -> Self {
        Self { 
            config: SamplingConfig::FREQ_4K,
        }
    }
}

impl Modulation for Burst {
    fn calc(self, _: &FirmwareLimits) -> Result<Vec<u8>, ModulationError> {
        Ok((0..4000)
            .map(|i| if i == 3999 { u8::MAX } else { u8::MIN })
            .collect())
    }

    fn sampling_config(&self) -> SamplingConfig {
        self.config
    }
}
# fn main() { 
# }