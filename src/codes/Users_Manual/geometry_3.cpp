//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Point3::origin())}).open(autd3::link::Nop::builder());
const auto num_dev = autd.num_devices();
const auto num_tr = autd.num_transducers();
const auto center = autd.center();
//~return 0; }