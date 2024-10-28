# use std::time::Duration;
# use autd3::prelude::*;
use autd3_emulator::*;

# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
let emulator = Controller::builder([AUTD3::new(Vector3::zeros())]).into_emulator();

let record = emulator
    .record(|mut autd| async {
        autd.send(Silencer::default()).await?;
        autd.send((Sine::new(200. * Hz), Uniform::new(EmitIntensity::new(0xFF))))
            .await?;
        autd.tick(Duration::from_millis(10))?;
        Ok(autd)
    })
    .await?;

let df = record.drive();
dbg!(df);
#     Ok(())
# }