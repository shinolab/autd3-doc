# extern crate autd3;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main()  {
let m = autd3::modulation::Square::new(150 * Hz)
        .with_duty(0.5);
# }