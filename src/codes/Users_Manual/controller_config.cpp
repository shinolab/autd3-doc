//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~(void)
autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())})
    .with_fallback_parallel_threshold(4)
    .with_fallback_timeout(std::chrono::milliseconds(20))
    .with_send_interval(std::chrono::milliseconds(1))
    .with_receive_interval(std::chrono::milliseconds(1))
    .with_timer_strategy(autd3::controller::timer::TimerStrategy::Spin(
        autd3::controller::timer::SpinSleeper()))
    //~;
    //~return 0; }