# use std::time::Duration;
# use autd3::prelude::*;
use autd3_emulator::*;

# fn main() -> Result<(), Box<dyn std::error::Error>> {
let emulator = Controller::builder([AUTD3::new(Point3::origin())]).into_emulator();

let record = emulator
    .record(|autd| {
        autd.send(Silencer::disable())?;
        autd.send((
            Static::with_intensity(0xFF),
            Uniform::new((Phase::new(0x40), EmitIntensity::new(0xFF))),
        ))?;
        autd.tick(Duration::from_millis(1))?;
        Ok(())
    })?;

let df = record.output_voltage();
dbg!(df);
#     Ok(())
# }