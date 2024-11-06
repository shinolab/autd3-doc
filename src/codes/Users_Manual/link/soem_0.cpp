//~#include<autd3.hpp>
//~#include <iostream>
#include <autd3_link_soem.hpp>

//~int main() {
//~(void)
autd3::link::SOEM::builder()
    .with_ifname("")
    .with_buf_size(32)
    .with_err_handler([](const uint16_t slave,
                         const autd3::link::Status status) {
      std::cout << "slave [" << slave << "]: " << status << std::endl;
      if (status == autd3::link::Status::Lost()) {
        // You can also wait for the link to recover, without exiting the
        // process
        exit(-1);
      }
    })
    .with_sync0_cycle(std::chrono::milliseconds(1))
    .with_send_cycle(std::chrono::milliseconds(1))
    .with_timer_strategy(autd3::link::TimerStrategy::SpinSleep)
    .with_state_check_interval(std::chrono::milliseconds(100))
    .with_sync_tolerance(std::chrono::microseconds(1))
    .with_sync_timeout(std::chrono::seconds(10))
    .with_thread_priority(autd3::link::ThreadPriority::Max)
    .with_process_priority(autd3::link::ProcessPriority::High)
    //~;
    //~return 0; }