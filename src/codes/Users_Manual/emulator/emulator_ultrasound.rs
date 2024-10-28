# use std::time::Duration;
# use autd3::prelude::*;
use autd3_emulator::*;

# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
let emulator = Controller::builder([AUTD3::new(Vector3::zeros())]).into_emulator();

let record = emulator
    .record(|mut autd| async {
        autd.send(Silencer::disable()).await?;
        autd.send((
            Static::with_intensity(0xFF),
            Uniform::new((Phase::new(0x40), EmitIntensity::new(0xFF))),
        ))
        .await?;
        autd.tick(Duration::from_millis(1))?;
        Ok(autd)
    })
    .await?;

let df = record.output_ultrasound();
dbg!(df);
#     Ok(())
# }