# extern crate autd3;
# extern crate tokio;
# use autd3::prelude::*;
# 
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::builder()
#     .add_device(AUTD3::new(Vector3::zeros()))
#    .open(autd3::link::Nop::builder()).await?;
let dev = &autd.geometry[0];
for dev in &autd.geometry {
    // do something
}
# Ok(())
# }