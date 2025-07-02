# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], Nop::new())?;
autd.send(Silencer::disable())?;

let center = autd.center() + Vector3::new(0.0, 0.0, 150. * mm);
let point_num = 20;
let radius = 30.0 * mm;
autd.send(FociSTM {
    foci: (0..point_num)
        .map(|i| {
            let theta = 2.0 * PI * i as f32 / point_num as f32;
            let p = radius * Vector3::new(theta.cos(), theta.sin(), 0.0);
            center + p
        })
        .collect::<Vec<_>>(),
    config: 50.0 * Hz,
})?;
# Ok(())
# }