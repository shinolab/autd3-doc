//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd = autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
auto sender = autd.sender(autd3::SenderOption{
    .send_interval = std::chrono::milliseconds(1),
    .receive_interval = std::chrono::milliseconds(1),
    .timeout = std::nullopt,
    .parallel = autd3::ParallelMode::Auto,
    .sleeper = autd3::SpinSleeper(),
});
//~const autd3::Null d;
sender.send(d);
//~return 0; }