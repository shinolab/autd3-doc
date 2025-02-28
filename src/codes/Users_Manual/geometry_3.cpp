//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
const auto num_dev = autd.num_devices();
const auto num_tr = autd.num_transducers();
const auto center = autd.center();
//~return 0; }