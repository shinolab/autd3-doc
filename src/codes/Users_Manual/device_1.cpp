//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
//~{
auto tr = autd[0][0];
//~}
//~{
for (auto& tr : autd[0]) {
  // do something
}
//~}
//~return 0; }