//~#include<autd3.hpp>
//~#include <iostream>
#include "autd3/link/soem.hpp"

//~int main() {
//~auto autd = autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())})
//~                .open(
autd3::link::SOEM::builder()
    .with_ifname("")
    .with_buf_size(32)
    .with_err_handler([](const uint16_t slave, const autd3::link::Status status, const std::string& msg) {
      switch (status) {
        case autd3::link::Status::Error:
          std::cout << "Error [" << slave << "]: " << msg << std::endl;
          break;
        case autd3::link::Status::Lost:
          std::cout << "Lost [" << slave << "]: " << msg << std::endl;
          // You can also wait for the link to recover, without exiting the
          // process
          exit(-1);
        case autd3::link::Status::StateChanged:
          std::cout << "StateChanged [" << slave << "]: " << msg << std::endl;
          break;
      }
    })
    .with_state_check_interval(std::chrono::milliseconds(100))
    .with_sync0_cycle(2)
    .with_send_cycle(2)
    .with_timer_strategy(autd3::link::TimerStrategy::BusyWait)
    .with_sync_tolerance(std::chrono::microseconds(1))
    .with_sync_timeout(std::chrono::seconds(10))
    //~                    );
    //~return 0; }