# use autd3::prelude::*;
# 
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let link = autd3::link::Nop::new();
# let _ =
Controller::open(
    [
        AUTD3 {
            pos: Point3::new(-AUTD3::DEVICE_WIDTH, 0., 0.),
            rot: UnitQuaternion::identity(),
        },
        AUTD3 {
            pos: Point3::origin(),
            rot: UnitQuaternion::identity(),
        },
    ],
    link,
)?;
#     Ok(())
# }