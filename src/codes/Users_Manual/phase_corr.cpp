//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
autd.send(autd3::PhaseCorrection([](const auto&) {
  return [](const auto&) { return autd3::Phase(0x00); };
}));
//~return 0; }