# use autd3::prelude::*;
# 
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::builder([AUTD3::new(Point3::origin())])
#    .open(autd3::link::Nop::builder()).await?;
let tr = &autd[0][0];
for tr in &autd[0] {
    // do something
}
# Ok(())
# }