# use autd3::prelude::*;
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::builder([AUTD3::new(Point3::origin())]).open(autd3::link::Nop::builder()).await?;
# let m = Static::new();
# let g = Null::new();
autd.send((m, g).with_parallel_threshold(Some(0))).await?;
# Ok(())
# }