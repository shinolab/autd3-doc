use autd3::gain::IntoBoxedGain;
use autd3::prelude::*;
# use std::collections::HashMap;

# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let x = 0.;
# let y = 0.;
# let z = 0.;
# let _ =
Group {
    key_map: |_dev| {
        |tr| match tr.idx() {
            0..=100 => Some("null"),
            _ => Some("focus"),
        }
    },
    gain_map: HashMap::from([
        ("null", Null {}.into_boxed()),
        (
            "focus",
            Focus {
                pos: Point3::new(x, y, z),
                option: Default::default(),
            }
            .into_boxed(),
        ),
    ]),
};
# Ok(())
# }