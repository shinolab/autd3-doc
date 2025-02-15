# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let m = Sine {
    freq: 150 * Hz,
    option: SineOption::default(),
};
dbg!(m.sampling_config()?.freq()); // -> 4kHz
#     Ok(())
# }
