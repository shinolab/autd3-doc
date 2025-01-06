# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let start = Point3::origin();
# let end = Point3::origin();
# let center = Point3::origin();
# let radius = 30.0 * mm;
# let num_points = 50;
# let n = Vector3::z_axis();
# let intensity = EmitIntensity::MAX;
let stm = FociSTM::new(
    1.0 * Hz,
    Line {
        start,
        end,
        num_points,
        intensity,
    },
)?;

let stm = FociSTM::new(
    1.0 * Hz,
    Circle {
        center,
        radius,
        num_points,
        n, // normal vector to the plane where the circle is drawn
        intensity,
    },
)?;
# Ok(())
# }