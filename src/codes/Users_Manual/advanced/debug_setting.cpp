//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
DebugSettings([](const auto& dev, const auto& gpio) {
  return gpio == GPIOOut::O0 ? DebugType::BaseSignal : DebugType::None;
});
//~return 0; }