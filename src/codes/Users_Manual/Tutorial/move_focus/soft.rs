# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::open([AUTD3::default()], Nop::new())?;
autd.send(Sine {
    freq: 150 * Hz,
    option: SineOption::default(),
})?;

let center = autd.center() + Vector3::new(0.0, 0.0, 150. * mm);
loop {
    autd.send(Focus {
        pos: center + Vector3::new(20. * mm, 0.0, 0.0),
        option: FocusOption::default(),
    })?;

    std::thread::sleep(std::time::Duration::from_secs(1));

    autd.send(Focus {
        pos: center - Vector3::new(20. * mm, 0.0, 0.0),
        option: FocusOption::default(),
    })?;

    std::thread::sleep(std::time::Duration::from_secs(1));
}
# }