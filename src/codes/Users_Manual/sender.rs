# use std::time::Duration;
# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
let mut sender = autd.sender(SenderOption {
    send_interval: Duration::from_millis(1),
    receive_interval: Duration::from_millis(1),
    timeout: None,
    parallel: ParallelMode::Auto,
    sleeper: SpinSleeper::default(),
});
# let d = Null {};
sender.send(d)?;
# Ok(())
# }