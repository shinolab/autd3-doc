//~#include <iostream>
#include <autd3_link_soem.hpp>

//~int main() {
//~using namespace autd3;
link::SOEM(
    [](const uint16_t slave, const link::Status status) {
      std::cout << "slave [" << slave << "]: " << status << std::endl;
      if (status == link::Status::Lost()) {
        exit(-1);
      }
    },
    link::SOEMOption{.buf_size = 16,
                     .ifname = "",
                     .state_check_interval = std::chrono::milliseconds(100),
                     .sync0_cycle = std::chrono::milliseconds(1),
                     .send_cycle = std::chrono::milliseconds(1),
                     .thread_priority = link::ThreadPriority::Max(),
                     .process_priority = link::ProcessPriority::High,
                     .sync_tolerance = std::chrono::microseconds(1),
                     .sync_timeout = std::chrono::seconds(10),
                     .affinity = std::nullopt

    });
//~return 0; }