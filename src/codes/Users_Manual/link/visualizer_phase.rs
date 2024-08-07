# use autd3::prelude::*;
use autd3_link_visualizer::{Visualizer, PlotConfig};

use std::path::Path;

# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
let mut autd = Controller::builder([AUTD3::new(Vector3::zeros())])
    .open(Visualizer::builder()).await?;

let center = autd.geometry().center() + Vector3::new(0., 0., 150.0 * mm);
let g = Focus::new(center);
autd.send(g).await?;

autd.link().plot_phase(
    PlotConfig {
        fname: Path::new("phase.png").into(),
        ..PlotConfig::default()
    },
    Segment::S0,
    0
)?;
# autd.close().await?;
# Ok(())
# }
