//~#include<autd3.hpp>
//~int main() {
const auto steps_intensity = 10;
const auto steps_phase = 10;
const auto config =
    autd3::Silencer::from_completion_steps(steps_intensity, steps_phase)
        .with_strict_mode(false);
//~return 0; }