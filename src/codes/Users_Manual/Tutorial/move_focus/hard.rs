# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], Nop::new())?;
autd.send(Sine {
    freq: 150 * Hz,
    option: SineOption::default(),
})?;

let center = autd.center() + Vector3::new(0.0, 0.0, 150. * mm);
autd.send(FociSTM {
    foci: vec![
        center + Vector3::new(20. * mm, 0.0, 0.0),
        center - Vector3::new(20. * mm, 0.0, 0.0),
    ],
    config: 0.5 * Hz,
    // config: std::time::Duration::from_secs(2),
    // config: SamplingConfig::new(1.0 * Hz),
    // config: SamplingConfig::new(std::time::Duration::from_secs(1)),
})?;
#     Ok(())
# }