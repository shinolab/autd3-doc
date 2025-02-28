//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
//~{
auto dev = autd[0];
//~}
//~{
for (auto& dev : autd) {
  // do something
}
//~}
//~return 0; }