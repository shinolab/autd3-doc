# use autd3::prelude::*;
# 
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let _autd = 
Controller::builder([
        AUTD3::new(Point3::new(-AUTD3::DEVICE_WIDTH, 0., 0.)),
        AUTD3::new(Point3::origin())
    ])
#    .open(autd3::link::Nop::builder()).await?;
# Ok(())
# }
