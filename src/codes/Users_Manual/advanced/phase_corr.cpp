//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;
PhaseCorrection([](const auto&) {
  return [](const auto&) { return Phase::zero(); };
});
//~return 0; }