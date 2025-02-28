//~#include<autd3.hpp>
//~int main() {
//~using namespace autd3;

WithLoopBehavior(Static{}, LoopBehavior::Infinite(), Segment::S1,
                 TransitionMode::Immediate());

WithLoopBehavior(Static{}, LoopBehavior::Finite(1), Segment::S1,
                 TransitionMode::SyncIdx());
//~return 0; }