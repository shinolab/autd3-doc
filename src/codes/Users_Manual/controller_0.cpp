//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
autd.send(autd3::ReadsFPGAState([](const auto&) { return true; }));

const auto info = autd.fpga_state();
//~return 0; }