//~#include <iostream>
#include <autd3_link_ethercrab.hpp>

//~int main() {
//~using namespace autd3;
link::EtherCrab(
    [](const uint16_t idx, const link::Status status) {
      std::cout << "Device[" << idx << "]: " << status << std::endl;
    },
    link::EtherCrabOption{
        .ifname = std::nullopt,
        .state_check_period = std::chrono::milliseconds(100),
        .sync0_period = std::chrono::milliseconds(2),
        .sync_tolerance = std::chrono::microseconds(1),
        .sync_timeout = std::chrono::seconds(10),
    });
//~return 0; }