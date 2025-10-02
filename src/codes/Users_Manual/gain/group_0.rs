use autd3::prelude::*;
# use std::collections::HashMap;

# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let x = 0.;
# let y = 0.;
# let z = 0.;
# let _ =
GainGroup::new(
    |_dev| {
        |tr| match tr.idx() {
            0..=100 => Some("null"),
            _ => Some("focus"),
        }
    },
    HashMap::from([
        ("null", BoxedGain::new(Null {})),
        (
            "focus",
            BoxedGain::new(Focus {
                pos: Point3::new(x, y, z),
                option: Default::default(),
            }),
        ),
    ]),
);
# Ok(())
# }