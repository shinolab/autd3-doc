//~#include<autd3.hpp>
//~int main() {
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
autd3::WithSegment{
    autd3::Focus{autd3::Point3(x, y, z),
                 autd3::FocusOption{.intensity = autd3::Intensity(0x80)}},
    autd3::Segment::S1, autd3::TransitionMode::Immediate()};
//~return 0; }