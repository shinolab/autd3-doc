# use std::time::Duration;
# use autd3::prelude::*;
use autd3_emulator::*;

# fn main() -> Result<(), Box<dyn std::error::Error>> {
let emulator = Controller::builder([AUTD3::new(Point3::origin())]).into_emulator();

let record = emulator
    .record(|autd| {
        autd.send(Silencer::default())?;
        autd.send((Sine::new(200. * Hz), Uniform::new(EmitIntensity::new(0xFF))))?;
        autd.tick(Duration::from_millis(10))?;
        Ok(())
    })?;
# {
let df = record.phase();
dbg!(df);
# }

# {
let df = record.pulse_width();
dbg!(df);
# }

#     Ok(())
# }