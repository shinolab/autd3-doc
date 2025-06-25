# use autd3::prelude::*;
use autd3_emulator::*;
# use std::time::Duration;

# fn main() -> Result<(), Box<dyn std::error::Error>> {
let emulator = Emulator::new([AUTD3::default()]);

let record = emulator.record(|autd| {
    autd.send(Silencer::default())?;
    autd.send((
        Sine {
            freq: 200 * Hz,
            option: Default::default(),
        },
        Uniform {
            intensity: Intensity::MAX,
            phase: Phase::ZERO,
        },
    ))?;
    autd.tick(Duration::from_millis(10))?;
    Ok(())
})?;
let df = record.phase();
dbg!(df);

let df = record.pulse_width();
dbg!(df);
# Ok(())
# }