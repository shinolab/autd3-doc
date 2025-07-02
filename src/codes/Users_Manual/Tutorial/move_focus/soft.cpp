//~#include <chrono>
//~#include <thread>
//~#include "autd3.hpp"
//~#include "autd3/link/nop.hpp"
//~int main() {
//~auto autd = autd3::Controller::open({autd3::AUTD3{.pos =
//~autd3::Point3::origin(), .rot = autd3::Quaternion::Identity(),}},
//~autd3::link::Nop{});
autd.send(autd3::Sine(150 * autd3::Hz, autd3::SineOption{}));

const autd3::Point3 center = autd.center() + autd3::Vector3(0., 0., 150.);
while (true) {
  autd.send(
      autd3::Focus{center + autd3::Vector3(20., 0., 0.), autd3::FocusOption{}});

  std::this_thread::sleep_for(std::chrono::milliseconds(1000));

  autd.send(
      autd3::Focus{center - autd3::Vector3(20., 0., 0.), autd3::FocusOption{}});

  std::this_thread::sleep_for(std::chrono::milliseconds(1000));
}
//~return 0;
//~}