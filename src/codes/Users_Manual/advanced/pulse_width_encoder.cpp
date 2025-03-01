//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~#include<vector>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
PulseWidthEncoder([](const auto& dev) {
  return [](const auto i) { return 0; };
});
//~return 0; }