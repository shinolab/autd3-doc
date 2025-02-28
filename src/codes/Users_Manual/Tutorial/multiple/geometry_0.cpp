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
                      .pos = Point3(AUTD3::DEVICE_WIDTH, 0, 0),
                      .rot = Quaternion::Identity(),
                  }},
                 std::move(link));
//~return 0; }