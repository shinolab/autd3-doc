# use autd3::prelude::*;
use autd3_emulator::*;
# use std::time::Duration;

# fn main() -> Result<(), Box<dyn std::error::Error>> {
let emulator = Emulator::new([AUTD3::default()]);

let record = emulator.record(|autd| {
    autd.send(Silencer::disable())?;
    autd.send((
        Static { intensity: 0xFF },
        Uniform {
            intensity: Intensity::MAX,
            phase: Phase(0x40),
        },
    ))?;
    autd.tick(Duration::from_millis(1))?;
    Ok(())
})?;

let df = record.output_voltage();
dbg!(df);
#     Ok(())
# }