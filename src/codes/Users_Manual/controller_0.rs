# use autd3::prelude::*;
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::builder([AUTD3::new(Point3::origin())]).open(autd3::link::Nop::builder()).await?;
autd.send(ReadsFPGAState::new(|_dev| true)).await?;

let info = autd.fpga_state().await?;
# Ok(())
# }