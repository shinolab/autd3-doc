# use autd3::prelude::*;
use autd3_emulator::*;
# use std::time::Duration;

# fn main() -> Result<(), Box<dyn std::error::Error>> {
let emulator = Emulator::new([AUTD3::default()]);

let focus = emulator.center() + Vector3::new(0., 0., 150. * mm);

let record = emulator.record(|autd| {
    autd.send(Silencer::disable())?;
    autd.send((
        Static { intensity: 0xFF },
        Focus {
            pos: focus,
            option: Default::default(),
        },
    ))?;
    autd.tick(Duration::from_micros(25))?;
    Ok(())
})?;

let mut sound_field = record.sound_field(
    RangeXY {
        x: focus.x - 20.0..=focus.x + 20.0,
        y: focus.y - 20.0..=focus.y + 20.0,
        z: focus.z,
        resolution: 1.,
    },
    RmsRecordOption {
        sound_speed: 340e3 * mm,
        print_progress: true,
        gpu: true,
    },
)?;

let df = sound_field.observe_points();
dbg!(df);

let df = sound_field.next(Duration::from_micros(25))?;
dbg!(df);
#     Ok(())
# }