# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
autd.send(SwapSegment::Modulation(Segment::S1, TransitionMode::Immediate))?;
# Ok(())
# }