# use autd3::prelude::*;
# use autd3_link_simulator::Simulator;
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::builder([AUTD3::new(Vector3::zeros())])
#             .open(Simulator::builder(8080)).await?;
autd.link.update_geometry(&autd.geometry).await?;
# Ok(())
# }