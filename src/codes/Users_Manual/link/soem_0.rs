# use std::num::{NonZeroUsize, NonZeroU64};
# use std::time::Duration;
use autd3_link_soem::{SOEM, TimerStrategy, Status, ThreadPriority};
#[cfg(target_os = "windows")]
use autd3_link_soem::ProcessPriority;

# #[allow(unused_variables)]
# fn main() {
# let builder =
SOEM::builder()
    .with_ifname("")
    .with_buf_size(NonZeroUsize::new(32).unwrap())
    .with_err_handler(|slave, status| match status {
        Status::Error => eprintln!("Error [{}]: {}", slave, status),
        Status::Lost => {
            eprintln!("Lost [{}]: {}", slave, status);
            // You can also wait for the link to recover, without exitting the process
            std::process::exit(-1);
        }
        Status::StateChanged => eprintln!("StateChanged [{}]: {}", slave, status),
    })
    .with_state_check_interval(Duration::from_millis(100))
    .with_sync0_cycle(NonZeroU64::new(2).unwrap())
    .with_send_cycle(NonZeroU64::new(2).unwrap())
    .with_timer_strategy(TimerStrategy::BusyWait)
    .with_sync_tolerance(Duration::from_micros(1))
    .with_sync_timeout(Duration::from_secs(10))
    .with_thread_priority(ThreadPriority::Max)
# ;
# #[cfg(target_os = "windows")]
# {
# let builder = 
# builder
    // Only available on Windows 
    .with_process_priority(ProcessPriority::High)
# ;
# }
# }