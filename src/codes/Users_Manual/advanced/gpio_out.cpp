//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
GPIOOutputs([](const auto& dev,
               const auto& gpio) -> std::optional<GPIOOutputType> {
  if (gpio == GPIOOut::O0)
    return GPIOOutputType::BaseSignal;
  else
    return std::nullopt;
});
//~return 0; }