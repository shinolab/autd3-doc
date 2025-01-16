# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::builder([AUTD3::new(Point3::origin())]).open(autd3::link::Nop::builder())?;
let center = autd.center() + Vector3::new(0., 0., 150.0 * mm);
let point_num = 200;
let radius = 30.0 * mm;
let stm = FociSTM::new(
    1.0 * Hz,
    (0..point_num).map(|i| {
        let theta = 2.0 * PI * i as f32 / point_num as f32;
        let p = radius * Vector3::new(theta.cos(), theta.sin(), 0.0);
        center + p
    }),
)?;
# Ok(())
# }