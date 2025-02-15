# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
let dev = &autd[0];
for dev in &autd {
    // do something
}
# Ok(())
# }