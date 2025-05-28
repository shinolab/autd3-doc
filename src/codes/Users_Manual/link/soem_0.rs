#[cfg(target_os = "windows")]
use autd3_link_soem::ProcessPriority;
use autd3_link_soem::{Status, SyncMode, ThreadPriority, TimerStrategy, SOEM, SOEMOption};
# use std::num::NonZeroUsize;
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
        buf_size: NonZeroUsize::new(32).unwrap(),
        timer_strategy: TimerStrategy::SpinSleep,
        sync_mode: SyncMode::DC, // DO NOT CHANGE
        ifname: String::new(),
        state_check_interval: Duration::from_millis(100),
        sync0_cycle: Duration::from_millis(1),
        send_cycle: Duration::from_millis(1),
        thread_priority: ThreadPriority::Max,
        #[cfg(target_os = "windows")]
        process_priority: ProcessPriority::High,
        sync_tolerance: Duration::from_micros(1),
        sync_timeout: Duration::from_secs(10),
    },
);
# }