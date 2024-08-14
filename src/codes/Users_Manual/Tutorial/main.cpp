#include <iostream>

#include "autd3.hpp"
#include "autd3/link/soem.hpp"

int main() try {
  auto autd =
      autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())})
          .open(autd3::link::SOEM::builder().with_err_handler([](const uint16_t slave, const autd3::link::Status status, const std::string& msg) {
            switch (status) {
              case autd3::link::Status::Error:
                std::cout << "Error [" << slave << "]: " << msg << std::endl;
                break;
              case autd3::link::Status::Lost:
                std::cout << "Lost [" << slave << "]: " << msg << std::endl;
                exit(-1);
              case autd3::link::Status::StateChanged:
                std::cout << "StateChanged [" << slave << "]: " << msg << std::endl;
                break;
            }
          }));

  const auto firm_version = autd.firmware_version();
  std::copy(firm_version.begin(), firm_version.end(), std::ostream_iterator<autd3::FirmwareVersion>(std::cout, "\n"));

  autd.send(autd3::Silencer());

  const autd3::Vector3 focus = autd.geometry().center() + autd3::Vector3(0, 0, 150);
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