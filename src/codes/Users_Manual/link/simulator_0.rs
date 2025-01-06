# use autd3::prelude::*;
use autd3_link_simulator::Simulator;

# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::builder([AUTD3::new(Point3::origin())])
#             .open(
Simulator::builder("127.0.0.1:8080".parse()?)
# ).await?;
# Ok(())
# }