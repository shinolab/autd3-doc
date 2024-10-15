# use std::time::Duration;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
# let _ = 
Controller::builder([AUTD3::new(Vector3::zeros())])
    .with_parallel_threshold(4)
    .with_send_interval(Duration::from_millis(1))
    .with_receive_interval(Duration::from_millis(1))
# ;
# #[cfg(target_os = "windows")]
# {
# let _ = 
# Controller::builder([AUTD3::new(Vector3::zeros())])
    // Only available on Windows 
    .with_timer_resolution(std::num::NonZeroU32::new(1))
# ;
# }
# }