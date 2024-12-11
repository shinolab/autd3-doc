# use std::num::NonZeroUsize;
# use autd3::prelude::*;
# use autd3::modulation::resampler::{SincInterpolation, Blackman};
# use autd3_modulation_audio_file::Wav;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let path = "path/to/foo.wav";
let m = Wav::new_with_resample(
    path,
    4 * kHz,
    SincInterpolation {
        window: Blackman {
            size: NonZeroUsize::new(32).unwrap(),
        },
    },
)?;
# Ok(())
# }