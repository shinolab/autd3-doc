//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
autd.send(PhaseCorrection([](const auto&) {
  return [](const auto&) { return Phase::zero(); };
}));
//~return 0; }