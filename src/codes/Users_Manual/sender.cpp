//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd = Controller::open({AUTD3{}}, link::Nop{});
auto sender =
    autd.sender(SenderOption{.send_interval = std::chrono::milliseconds(1),
                             .receive_interval = std::chrono::milliseconds(1),
                             .timeout = std::nullopt,
                             .parallel = ParallelMode::Auto},
                SpinSleeper());
//~const Null d;
sender.send(d);
//~return 0; }