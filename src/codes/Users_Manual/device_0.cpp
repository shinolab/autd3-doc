//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
auto dev = autd[0];
const auto idx = dev.idx();
const auto rotation = dev.rotation();
const auto x_dir = dev.x_direction();
const auto y_dir = dev.y_direction();
const auto axial_dir = dev.axial_direction();
//~return 0; }