//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Point3::origin())}).open(autd3::link::Nop::builder());
//~autd3::Static m;
//~autd3::Null g;
autd.send((m, g).with_parallel_threshold(0));
//~return 0; }