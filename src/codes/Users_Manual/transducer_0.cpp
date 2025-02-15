//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
const auto tr = autd[0][0];
const auto idx = tr.idx();
const auto dev_idx = tr.dev_idx();
const auto position = tr.position();
//~return 0; }