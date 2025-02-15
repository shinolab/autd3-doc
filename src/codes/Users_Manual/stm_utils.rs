# use autd3::prelude::*;
# fn main() {
# let start = Point3::origin();
# let end = Point3::origin();
# let center = Point3::origin();
# let radius = 30.0 * mm;
# let num_points = 50;
# let n = Vector3::z_axis();
# let intensity = EmitIntensity::MAX;
# let _ = 
FociSTM {
    foci: Line {
        start,
        end,
        num_points,
        intensity,
    },
    config: 1.0 * Hz,
};

# let _ = 
FociSTM {
    foci: Circle {
        center,
        radius,
        num_points,
        n, // normal vector to the plane where the circle is drawn
        intensity,
    },
    config: 1.0 * Hz,
};
# }