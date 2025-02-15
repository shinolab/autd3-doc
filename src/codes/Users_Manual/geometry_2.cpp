//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~autd3::link::Nop link;
autd3::Controller::open(
    {autd3::AUTD3{
         .pos = autd3::Point3::origin(),
         .rot = autd3::Quaternion::Identity(),
     },
     autd3::AUTD3{
         .pos = autd3::Point3(0, 0, autd3::AUTD3::DEVICE_WIDTH),
         .rot = autd3::EulerAngles::ZYZ(
             0. * autd3::rad, autd3::pi / 2.0 * autd3::rad, 0. * autd3::rad),
     }},
    std::move(link));
//~return 0; }