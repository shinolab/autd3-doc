# use std::time::Duration;
# use autd3::prelude::*;
use autd3::controller::timer::{TimerStrategy, SpinSleeper};

# #[allow(unused_variables)]
# fn main() {
# let _ = 
Controller::builder([AUTD3::new(Vector3::zeros())])
    .with_default_parallel_threshold(4)
    .with_default_timeout(Duration::from_millis(20))
    .with_send_interval(Duration::from_millis(1))
    .with_receive_interval(Duration::from_millis(1))
    .with_timer_strategy(TimerStrategy::Spin(SpinSleeper::default()))
# ;
# }