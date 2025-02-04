# use autd3::prelude::*;
# fn main() {
#     let _ = 
Sine {
    freq: 150. * Hz,
    option: SineOption {
        intensity: u8::MAX,
        offset: 0x80,
        phase: 0. * rad,
        clamp: false,
        sampling_config: SamplingConfig::FREQ_4K,
    },
}
.into_nearest();
# }