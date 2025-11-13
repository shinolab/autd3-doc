use autd3_link_ethercrab::{EtherCrab, EtherCrabOption};
# use std::time::Duration;

# fn main() {
# let _ = 
EtherCrab::new(
    |idx, status| {
        eprintln!("Device[{}]: {}", idx, status);
    },
    EtherCrabOption {
        ifname: None,
        state_check_period: Duration::from_millis(100),
        sync0_period: Duration::from_millis(2),
        sync_tolerance: Duration::from_micros(1),
        sync_timeout: Duration::from_secs(10),
    },
);
# }