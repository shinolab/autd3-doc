# use autd3::prelude::*;
# use autd3_emulator::*;
# fn main() {
let emulator = Controller::builder([AUTD3::new(Vector3::zeros())]).into_emulator();
let df = emulator.transducer_table();
dbg!(df);
# }