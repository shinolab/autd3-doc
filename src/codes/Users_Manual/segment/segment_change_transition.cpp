//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::Controller::open({autd3::AUTD3{}}, autd3::link::Nop{});
autd.send(autd3::SwapSegment::Modulation(autd3::Segment::S1,
                                         autd3::TransitionMode::Immediate()));
//~return 0; }