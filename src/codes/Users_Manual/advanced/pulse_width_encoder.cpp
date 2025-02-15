//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~#include<vector>
//~int main() {
//~auto autd =
//~autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
autd.send(autd3::PulseWidthEncoder([](const auto& dev) {
  return [](const auto i) { return 0; };
}));
//~return 0; }