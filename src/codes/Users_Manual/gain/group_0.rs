use autd3::prelude::*;
# use std::collections::HashMap;

# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let x = 0.;
# let y = 0.;
# let z = 0.;
# let _ =
GainGroup {
    key_map: |_dev| {
        |tr| match tr.idx() {
            0..=100 => Some("null"),
            _ => Some("focus"),
        }
    },
    gain_map: HashMap::from([
        ("null", BoxedGain::new(Null {})),
        (
            "focus",
            BoxedGain::new(Focus {
                pos: Point3::new(x, y, z),
                option: Default::default(),
            }),
        ),
    ]),
};
# Ok(())
# }