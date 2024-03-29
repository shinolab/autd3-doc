# extern crate autd3;
# extern crate tokio;
# extern crate autd3_driver;
use autd3::prelude::*;
use autd3_driver::derive::*;

#[derive(Modulation)]
pub struct Burst {
    config: SamplingConfiguration,
    loop_behavior: LoopBehavior,
}

impl Burst {
    pub fn new() -> Self {
        Self { 
            config: SamplingConfiguration::from_frequency(4e3).unwrap(),
            loop_behavior: LoopBehavior::Infinite,
        }
    }
}

impl Modulation for Burst {
    fn calc(&self) -> Result<Vec<EmitIntensity>, AUTDInternalError> {
        Ok((0..4000)
            .map(|i| if i == 3999 { EmitIntensity::MAX } else { EmitIntensity::MIN })
            .collect())
    }
}
# fn main() { 
# }