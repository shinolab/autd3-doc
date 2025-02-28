# use autd3::prelude::*;
# 
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let link = autd3::link::Nop::new();
# let _ =
Controller::open(
    [
        AUTD3 {
            pos: Point3::origin(),
            rot: UnitQuaternion::identity(),
        },
        AUTD3 {
            pos: Point3::new(0., 0., AUTD3::DEVICE_WIDTH),
            rot: EulerAngle::ZYZ(0. * rad, PI/2.0 * rad, 0. * rad).into(),
        },
    ],
    link,
)?;
#     Ok(())
# }