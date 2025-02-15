# use autd3::prelude::*;
# #[allow(unused_variables)] 
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
let tr = &autd[0][0];
for tr in &autd[0] {
    // do something
}
# Ok(())
# }