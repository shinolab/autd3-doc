use autd3_link_soem::{Status, SOEM, SOEMOption};
# use std::time::Duration;

# fn main() {
# let _ = 
SOEM::new(
    |slave, status| {
        eprintln!("slave [{}]: {}", slave, status);
        if status == Status::Lost {
            std::process::exit(-1);
        }
    },
    SOEMOption {
        ifname: None,
        state_check_interval: Duration::from_millis(100),
        sync0_cycle: Duration::from_millis(1),
        sync_tolerance: Duration::from_micros(1),
        sync_timeout: Duration::from_secs(10),
    },
);
# }