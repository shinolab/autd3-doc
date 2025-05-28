# use autd3_gain_holo::*;
# use nalgebra::ComplexField;
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct AbsGreedyObjectiveFn;

impl GreedyObjectiveFn for AbsGreedyObjectiveFn {
    fn objective_func(current: Complex, target: Amplitude) -> f32 {
        (target.pascal() - current.abs()).abs()
    }
}
# fn main() {}