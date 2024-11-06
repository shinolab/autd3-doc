#include <autd3_link_soem.hpp>
#include <iostream>

#include "autd3.hpp"

int main() try {
  auto autd =
      autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())})
          .open(autd3::link::SOEM::builder().with_err_handler(
              [](const uint16_t slave, const autd3::link::Status status) {
                std::cout << "slave [" << slave << "]: " << status << std::endl;
                if (status == autd3::link::Status::Lost()) exit(-1);
              }));

  const auto firm_version = autd.firmware_version();
  std::copy(firm_version.begin(), firm_version.end(),
            std::ostream_iterator<autd3::FirmwareVersion>(std::cout, "\n"));

  autd.send(autd3::Silencer());

  const autd3::Vector3 focus = autd.center() + autd3::Vector3(0, 0, 150);
  autd3::gain::Focus g(focus);

  autd3::modulation::Sine m(150 * autd3::Hz);

  autd.send((m, g));

  std::cout << "press enter to finish..." << std::endl;
  std::cin.ignore();

  autd.close();

  return 0;
} catch (std::exception& ex) {
  std::cerr << ex.what() << std::endl;
}