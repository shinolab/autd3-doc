# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::open([AUTD3::default()], Nop::new())?;
let center = autd.center() + Vector3::new(0., 0., 150.0 * mm);
let point_num = 200;
let radius = 30.0 * mm;
# let _ = 
FociSTM {
    foci: (0..point_num)
        .map(|i| {
            let theta = 2.0 * PI * i as f32 / point_num as f32;
            let p = radius * Vector3::new(theta.cos(), theta.sin(), 0.0);
            ControlPoints {
                points: [
                    ControlPoint {
                        point: center + p,
                        phase_offset: Phase::ZERO,
                    },
                    ControlPoint {
                        point: center - p,
                        phase_offset: Phase::ZERO,
                    },
                ],
                intensity: Intensity::MAX,
            }
        })
        .collect::<Vec<_>>(),
    config: 1.0 * Hz,
};
# Ok(())
# }