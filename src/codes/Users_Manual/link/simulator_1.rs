# use autd3::prelude::*;
# use autd3_link_simulator::Simulator;
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::builder([AUTD3::new(Vector3::zeros())])
#             .open(
Simulator::builder(8080).with_server_ip([127, 0, 0, 1])
# ).await?;
# Ok(())
# }