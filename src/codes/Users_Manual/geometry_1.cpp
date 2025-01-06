//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
autd3::ControllerBuilder(
    {autd3::AUTD3(autd3::Point3(-autd3::AUTD3::DEVICE_WIDTH, 0, 0)),
     autd3::AUTD3(autd3::Point3::origin())})
    //~;
    //~return 0; }