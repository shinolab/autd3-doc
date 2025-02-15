//~#include <iostream>
#include <autd3_link_soem.hpp>

//~int main() {
autd3::link::SOEM(
    [](const uint16_t slave, const autd3::link::Status status) {
      std::cout << "slave [" << slave << "]: " << status << std::endl;
      if (status == autd3::link::Status::Lost()) {
        exit(-1);
      }
    },
    autd3::link::SOEMOption{
        .buf_size = 32,
        .timer_strategy = autd3::link::TimerStrategy::SpinSleep,
        .sync_mode = autd3::link::SyncMode::DC,
        .ifname = "",
        .state_check_interval = std::chrono::milliseconds(100),
        .sync0_cycle = std::chrono::milliseconds(1),
        .send_cycle = std::chrono::milliseconds(1),
        .thread_priority = autd3::link::ThreadPriority::Max(),
        .process_priority = autd3::link::ProcessPriority::High,
        .sync_tolerance = std::chrono::microseconds(1),
        .sync_timeout = std::chrono::seconds(10),

    });
//~return 0; }