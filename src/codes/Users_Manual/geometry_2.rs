# use autd3::prelude::*;
# 
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let _autd = 
Controller::builder([
        AUTD3::new(Point3::origin()),
        AUTD3::new(Point3::new(0., 0., AUTD3::DEVICE_WIDTH))
            .with_rotation(EulerAngle::ZYZ(0. * rad, PI/2.0 * rad, 0. * rad))
    ])
#    .open(autd3::link::Nop::builder())?;
# Ok(())
# }