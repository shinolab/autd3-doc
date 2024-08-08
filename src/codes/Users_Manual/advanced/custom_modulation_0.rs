use autd3::prelude::*;
use autd3::derive::*;

#[derive(Modulation)]
pub struct Burst {
    config: SamplingConfig,
    loop_behavior: LoopBehavior,
}

impl Burst {
    pub fn new() -> Self {
        Self { 
            config: (4000 * Hz).try_into().unwrap(),
            loop_behavior: LoopBehavior::infinite(),
        }
    }
}

impl Modulation for Burst {
    fn calc(&self) -> Result<Arc<Vec<u8>>, AUTDInternalError> {
        Ok(Arc::new((0..4000)
            .map(|i| if i == 3999 { u8::MAX } else { u8::MIN })
            .collect()))
    }
}
# #[allow(unused_variables)]
# fn main() { 
# }