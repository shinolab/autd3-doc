# use autd3::prelude::*;
use autd3::gain::IntoBoxedGain;

# use std::collections::HashMap;
# fn main() {
#     let x = 0.;
#     let y = 0.;
#     let z = 0.;
#     let _ = 
Group::new(
    |dev| match dev.idx() {
        0 => Some("focus"),
        1 => Some("null"),
        _ => None,
    },
    HashMap::from([
        (
            "focus",
            Focus {
                pos: Point3::new(x, y, z),
                option: Default::default(),
            }
            .into_boxed(),
        ),
        ("null", Null {}.into_boxed()),
    ]),
);
# }