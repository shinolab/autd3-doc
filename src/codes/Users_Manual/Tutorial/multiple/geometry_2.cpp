//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~link::Nop link;
Controller::open({AUTD3{
                      .pos = Point3::origin(),
                      .rot = Quaternion::Identity(),
                  },
                  AUTD3{
                      .pos = Point3(0, 0, AUTD3::DEVICE_WIDTH),
                      .rot = EulerAngles::ZYZ(0. * rad, pi / 2.0 * rad,
                                              0. * rad),
                  }},
                 std::move(link));
//~return 0; }