//~#include<chrono>
//~#include<autd3.hpp>
//~int main() {
const auto time_intensity = std::chrono::microseconds(250);
const auto time_phase = std::chrono::microseconds(250);
const auto config =
    autd3::Silencer::from_completion_time(time_intensity, time_phase);
//~return 0; }