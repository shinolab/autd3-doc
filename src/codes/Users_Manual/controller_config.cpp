//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~(void)
autd3::ControllerBuilder({autd3::AUTD3(autd3::Point3::origin())})
    .with_default_parallel_threshold(4)
    .with_default_timeout(std::chrono::milliseconds(20))
    .with_send_interval(std::chrono::milliseconds(1))
    .with_receive_interval(std::chrono::milliseconds(1))
    .with_timer_strategy(autd3::controller::timer::TimerStrategy::Spin(
        autd3::controller::timer::SpinSleeper()))
    //~;
    //~return 0; }