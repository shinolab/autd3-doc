# use autd3::prelude::*;
# 
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let _autd = 
Controller::builder([
        AUTD3::new(Vector3::zeros()),
        AUTD3::new(Vector3::new(0., 0., AUTD3::DEVICE_WIDTH))
            .with_rotation(EulerAngle::ZYZ(0. * rad, PI/2.0 * rad, 0. * rad))
    ])
#    .open(autd3::link::Nop::builder()).await?;
# Ok(())
# }