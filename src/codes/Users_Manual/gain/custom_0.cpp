//~#include<autd3.hpp>
#include <autd3/gain/custom.hpp>

//~int main() {
autd3::gain::Custom([](const auto& dev) {
  return [](const auto& tr) {
    return autd3::Drive(autd3::Phase::zero(),
                        std::numeric_limits<autd3::EmitIntensity>::min());
  };
});
//~return 0; }