# use std::time::Duration;
# use autd3::prelude::*;
use autd3_emulator::*;

# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
let emulator = Controller::builder([AUTD3::new(Vector3::zeros())]).into_emulator();

let focus = emulator.center() + Vector3::new(0., 0., 150. * mm);

let record = emulator
    .record(|mut autd| async {
        autd.send(Silencer::disable()).await?;
        autd.send((Static::with_intensity(0xFF), Focus::new(focus)))
            .await?;
        autd.tick(Duration::from_millis(1))?;
        Ok(autd)
    })
    .await?;

let mut sound_field = record
    .sound_field(
        RangeXY {
            x: focus.x - 20.0..=focus.x + 20.0,
            y: focus.y - 20.0..=focus.y + 20.0,
            z: focus.z,
            resolution: 1.,
        },
        InstantRecordOption {
            sound_speed: 340e3 * mm,
            time_step: Duration::from_micros(1),
            print_progress: true,
            memory_limits_hint_mb: 128,
            gpu: true,        
        },
    )
    .await?;

let df = sound_field.observe_points();
dbg!(df);

let df = sound_field
    .skip(Duration::from_micros(500))
    .await?
    .next(Duration::from_micros(500))
    .await?;
dbg!(df);
#     Ok(())
# }