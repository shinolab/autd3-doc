# use autd3::prelude::*;
# use autd3::gain::IntoBoxedGain;
# use std::collections::HashMap;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
#     let mut autd = Controller::open(
#         [AUTD3::default(), AUTD3::default()],
#         autd3::link::Nop::new(),
#     )?;
#     let x = 0.;
#     let y = 0.;
#     let z = 0.;
autd.group_send(
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
)?;
#     Ok(())
# }