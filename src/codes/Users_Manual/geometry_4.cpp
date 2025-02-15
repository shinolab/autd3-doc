//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
//~{
auto dev = autd[0];
//~}
//~{
for (auto& dev : autd) {
  // do something
}
//~}
//~return 0; }