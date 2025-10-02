use autd3::prelude::*;
use autd3_link_ethercrab::{EtherCrab, EtherCrabOption};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Open controller with EtherCrab link
    // Here, the AUTD3 device is placed at the origin
    let mut autd = Controller::open(
        [AUTD3 {
            pos: Point3::origin(),
            rot: UnitQuaternion::identity(),
        }],
        EtherCrab::new(
            // The first argument is a callback that is called when error occurs
            |idx, status| {
                eprintln!("Device[{}]: {}", idx, status);
            },
            // The second argument is a option of EtherCrab link.
            EtherCrabOption::default(),
        ),
    )?;

    // Check firmware version
    // This code assumes that the version is v10 or later.
    autd.firmware_version()?.iter().for_each(|firm_info| {
        println!("{}", firm_info);
    });

    // Enable silencer
    // Note that this is enabled by default, so it is not actually necessary
    // To disable, send Silencer::disable()
    autd.send(Silencer::default())?;

    // A focus at 150mm directly above the center of the device
    let g = Focus {
        pos: autd.center() + Vector3::new(0., 0., 150.0 * mm),
        option: FocusOption::default(),
    };

    // 150 Hz sine wave modulation
    let m = Sine {
        freq: 150 * Hz,
        option: SineOption::default(),
    };

    // Send data
    autd.send((m, g))?;

    println!("press enter to quit...");
    let mut _s = String::new();
    std::io::stdin().read_line(&mut _s)?;

    // Close controller
    autd.close()?;

    Ok(())
}
