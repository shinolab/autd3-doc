# use autd3::prelude::*;

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
            BoxedDatagram::new(Focus {
                pos: Point3::new(x, y, z),
                option: Default::default(),
            }),
        ),
        ("null", BoxedDatagram::new(Null {})),
    ]),
);
# }