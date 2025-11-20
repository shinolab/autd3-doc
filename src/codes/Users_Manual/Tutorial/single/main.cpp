#include <iostream>

#include "autd3.hpp"
#include "autd3_link_ethercrab.hpp"

using namespace autd3;

int main() try {
  auto autd =
      Controller::open({AUTD3{
                           .pos = Point3::origin(),
                           .rot = Quaternion::Identity(),
                       }},
                       link::EtherCrab(
                           [](const uint16_t idx, const link::Status status) {
                             std::cout << std::format("Device[{}]: ", idx)
                                       << status << std::endl;
                           },
                           link::EtherCrabOption{}));

  for (auto&& firm : autd.firmware_version()) std::cout << firm << std::endl;

  autd.send(Silencer{});

  Focus g(autd.center() + Vector3(0, 0, 150), FocusOption{});
  Sine m(150 * Hz, SineOption{});

  autd.send((m, g));

  std::cout << "press enter to finish..." << std::endl;
  std::cin.ignore();

  autd.close();

  return 0;
} catch (std::exception& ex) {
  std::cerr << ex.what() << std::endl;
}