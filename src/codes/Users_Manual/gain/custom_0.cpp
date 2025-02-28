//~#include<autd3.hpp>
#include <autd3/gain/custom.hpp>

//~int main() {
//~using namespace autd3;
gain::Custom([](const auto& dev) {
  return [](const auto& tr) {
    return Drive(Phase::zero(), std::numeric_limits<EmitIntensity>::min());
  };
});
//~return 0; }