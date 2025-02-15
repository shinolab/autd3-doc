//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
autd.send(autd3::DebugSettings([](const auto& dev, const auto& gpio) {
  return gpio == autd3::GPIOOut::O0 ? autd3::DebugType::BaseSignal
                                    : autd3::DebugType::None;
}));
//~return 0; }