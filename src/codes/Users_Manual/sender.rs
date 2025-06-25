# use autd3::prelude::*;
# use std::time::Duration;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], autd3::link::Nop::new())?;
let mut sender = autd.sender(
    SenderOption {
        send_interval: Duration::from_millis(1),
        receive_interval: Duration::from_millis(1),
        timeout: None,
        parallel: ParallelMode::Auto,
        strict: true
    },
    FixedSchedule::default(),
);
# let d = Null {};
sender.send(d)?;
# Ok(())
# }