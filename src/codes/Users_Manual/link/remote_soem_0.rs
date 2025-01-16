# use autd3::prelude::*;
use autd3_link_soem::RemoteSOEM;

# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::builder([AUTD3::new(Point3::origin())])
#            .open(
RemoteSOEM::builder("172.16.99.104:8080".parse()?)
# )?;
# Ok(())
# }