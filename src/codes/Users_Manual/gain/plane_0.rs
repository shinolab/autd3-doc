# use autd3::prelude::*;
# use autd3::driver::geometry::UnitVector3;
# #[allow(unused_variables)]
# fn main() {
# let x = 0.;
# let y = 0.;
# let z = 0.;
# let nx = 0.;
# let ny = 0.;
# let nz = 0.;
# let theta = 0.;
let g = Plane::new(UnitVector3::new_normalize(Vector3::new(nx, ny, nz)));
# }