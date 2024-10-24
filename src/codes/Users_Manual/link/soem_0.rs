# use std::num::NonZeroUsize;
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
    .with_err_handler(|slave, status| {
        eprintln!("slave [{}]: {}", slave, status);
        if status == Status::Lost {
            // You can also wait for the link to recover, without exitting the process
            std::process::exit(-1);
        }
    })
    .with_state_check_interval(Duration::from_millis(100))
    .with_sync0_cycle(Duration::from_millis(1))
    .with_send_cycle(Duration::from_millis(1))
    .with_timer_strategy(TimerStrategy::SpinSleep)
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