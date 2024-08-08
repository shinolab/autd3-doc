# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
# let s = 
SamplingConfig::new_nearest(4000.0 * Hz)
# ;
// or
# let s = 
SamplingConfig::new_nearest(std::time::Duration::from_micros(250))
# ;
# }