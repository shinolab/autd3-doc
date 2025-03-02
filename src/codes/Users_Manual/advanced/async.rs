use autd3::prelude::*;
use autd3_link_soem::{SOEM, SOEMOption, Status};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut autd = autd3::r#async::Controller::open(
        [AUTD3 {
            pos: Point3::origin(),
            rot: UnitQuaternion::identity(),
        }],
        SOEM::new(
            |slave, status| {
                eprintln!("slave[{}]: {}", slave, status);
                if status == Status::Lost {
                    std::process::exit(-1);
                }
            },
            SOEMOption::default(),
        ),
    )
    .await?;

    autd.firmware_version().await?.iter().for_each(|firm_info| {
        println!("{}", firm_info);
    });

    autd.send(Silencer::default()).await?;

    let g = Focus {
        pos: autd.center() + Vector3::new(0., 0., 150.0 * mm),
        option: FocusOption::default(),
    };

    let m = Sine {
        freq: 150 * Hz,
        option: SineOption::default(),
    };

    autd.send((m, g)).await?;

    println!("press enter to quit...");
    let mut _s = String::new();
    std::io::stdin().read_line(&mut _s)?;

    autd.close().await?;

    Ok(())
}