//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Point3::origin())}).open(autd3::link::Nop::builder());
//~{
auto tr = autd[0][0];
//~}
//~{
for (auto& tr : autd[0]) {
  // do something
}
//~}
//~return 0; }