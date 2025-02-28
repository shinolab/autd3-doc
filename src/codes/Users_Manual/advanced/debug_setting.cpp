//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
autd.send(DebugSettings([](const auto& dev, const auto& gpio) {
  return gpio == GPIOOut::O0 ? DebugType::BaseSignal : DebugType::None;
}));
//~return 0; }