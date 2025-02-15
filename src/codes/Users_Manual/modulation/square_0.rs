# use autd3::prelude::*;
# fn main() {
# let _ = 
Square {
    freq: 150 * Hz,
    option: SquareOption {
        low: u8::MIN,
        high: u8::MAX,
        duty: 0.5,
        sampling_config: SamplingConfig::FREQ_4K,
    },
};
# }