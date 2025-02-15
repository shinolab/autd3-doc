use autd3::modulation::{Fourier, FourierOption};
# use autd3::prelude::*;

# fn main() {
# let _ = 
Fourier {
    components: vec![
        Sine {
            freq: 100 * Hz,
            option: Default::default(),
        },
        Sine {
            freq: 150 * Hz,
            option: Default::default(),
        },
    ],
    option: FourierOption {
        scale_factor: None,
        clamp: false,
        offset: 0x00,
    },
};
# }