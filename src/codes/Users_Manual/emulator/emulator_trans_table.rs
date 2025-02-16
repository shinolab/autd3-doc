# use autd3::prelude::*;
use autd3_emulator::*;

# fn main() {
let emulator = Emulator::new([AUTD3::default()]);
let df = emulator.transducer_table();
dbg!(df);
# }