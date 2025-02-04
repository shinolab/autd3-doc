# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
autd.send(DebugSettings::new(|_dev, gpio| if gpio == GPIOOut::O0 {
                                         DebugType::BaseSignal
                                     } else {
                                         DebugType::None
                                     }))?;
# Ok(())
# }