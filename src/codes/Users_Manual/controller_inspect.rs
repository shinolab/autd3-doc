# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
let r = autd.inspect(Null {})?;
dbg!(&r[0]); // result of device 0
// &r[0] = Some(
//     GainInspectionResult {
//         name: "Null",
//         data: [
//             Drive {
//                 phase: 0x00,
//                 intensity: 0x00,
//             },
//             ︙
//             Drive {
//                 phase: 0x00,
//                 intensity: 0x00,
//             },
//         ],
//         segment: S0,
//         transition_mode: None,
//     },
// )

# Ok(())
# }
