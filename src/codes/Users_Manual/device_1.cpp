//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
//~{
auto tr = autd[0][0];
//~}
//~{
for (auto& tr : autd[0]) {
  // do something
}
//~}
//~return 0; }