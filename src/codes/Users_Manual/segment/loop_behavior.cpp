//~#include<autd3.hpp>
//~int main() {

autd3::WithLoopBehavior(autd3::Static{}, autd3::LoopBehavior::Infinite(),
                        autd3::Segment::S1, autd3::TransitionMode::Immediate());

autd3::WithLoopBehavior(autd3::Static{}, autd3::LoopBehavior::Finite(1),
                        autd3::Segment::S1, autd3::TransitionMode::SyncIdx());
//~return 0; }