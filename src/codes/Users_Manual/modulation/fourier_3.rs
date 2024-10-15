# use autd3::modulation::Fourier;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
    let m = Fourier::new([Sine::new(100 * Hz), Sine::new(150 * Hz)])?
        .with_scale_factor(Some(1.))
        .with_offset(0)
        .with_clamp(true);
#     Ok(())
# }