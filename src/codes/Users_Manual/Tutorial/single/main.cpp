#include <iostream>

#include "autd3.hpp"
#include "autd3/link/ethercrab.hpp"

using namespace autd3;

int main() try {
  auto autd = Controller::open(
      {AUTD3{
          .pos = Point3::origin(),
          .rot = Quaternion::Identity(),
      }},
      link::EtherCrab(
          [](const uint16_t idx, const link::Status status) {
            std::cout << "Device[" << idx << "]: " << status << std::endl;
          },
          link::EtherCrabOption{}));

  const auto firm_version = autd.firmware_version();
  std::copy(firm_version.begin(), firm_version.end(),
            std::ostream_iterator<FirmwareVersion>(std::cout, "\n"));

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