//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
autd.send(ReadsFPGAState([](const auto&) { return true; }));

const auto info = autd.fpga_state();
//~return 0; }