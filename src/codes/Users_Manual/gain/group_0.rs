# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let x = 0.;
# let y = 0.;
# let z = 0.;
let g = Group::new(|_dev| |tr| match tr.idx() {
                0..=100 => Some("null"),
                _ => Some("focus"),
            })
            .set("null", Null::new())?
            .set("focus", Focus::new(Point3::new(x, y, z)))?;
# Ok(())
# }