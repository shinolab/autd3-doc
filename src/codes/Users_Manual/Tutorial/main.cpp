#include <autd3_link_soem.hpp>
#include <iostream>

#include "autd3.hpp"

int main() try {
  auto autd = autd3::Controller::open(
      {autd3::AUTD3{
          .pos = autd3::Point3::origin(),
          .rot = autd3::Quaternion::Identity(),
      }},
      autd3::link::SOEM(
          [](const uint16_t slave, const autd3::link::Status status) {
            std::cout << "slave [" << slave << "]: " << status << std::endl;
            if (status == autd3::link::Status::Lost()) exit(-1);
          },
          autd3::link::SOEMOption{}));

  const auto firm_version = autd.firmware_version();
  std::copy(firm_version.begin(), firm_version.end(),
            std::ostream_iterator<autd3::FirmwareVersion>(std::cout, "\n"));

  autd.send(autd3::Silencer{});

  autd3::Focus g(autd.center() + autd3::Vector3(0, 0, 150),
                 autd3::FocusOption{});
  autd3::Sine m(150 * autd3::Hz, autd3::SineOption{});

  autd.send((m, g));

  std::cout << "press enter to finish..." << std::endl;
  std::cin.ignore();

  autd.close();

  return 0;
} catch (std::exception& ex) {
  std::cerr << ex.what() << std::endl;
}