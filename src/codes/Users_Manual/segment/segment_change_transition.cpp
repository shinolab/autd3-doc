//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~using namespace autd3;
//~auto autd =
//~Controller::open({AUTD3{}}, link::Nop{});
autd.send(SwapSegment::Modulation(Segment::S1, TransitionMode::Immediate()));
//~return 0; }