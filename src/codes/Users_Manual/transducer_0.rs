# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
let tr = &autd[0][0];
let idx = tr.idx();
let dev_idx = tr.dev_idx();
let position = tr.position();
# Ok(())
# }